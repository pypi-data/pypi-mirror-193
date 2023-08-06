"""The `compare` module contains different types of comparer classes for
fixed locations (PointComparer), or locations moving in space (TrackComparer).

These Comparers are constructed by extracting data from the combination of observation and model results

Examples
--------
>>> mr = ModelResult("Oresund2D.dfsu", item=0)
>>> o1 = PointObservation("klagshamn.dfs0", item=0, x=366844, y=6154291, name="Klagshamn")
>>> con = Connector(o1, mr)
>>> comparer = con.extract()
"""
from collections.abc import Mapping, Iterable, Sequence
from typing import Dict, List, Optional, Union
import warnings
from inspect import getmembers, isfunction
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from copy import deepcopy

import mikeio
import fmskill.metrics as mtr
from .observation import PointObservation, TrackObservation
from .plot import scatter, taylor_diagram, TaylorPoint
from .skill import AggregatedSkill
from .spatial import SpatialSkill
from .settings import options, register_option, reset_option

register_option(
    "metrics.list",
    [mtr.bias, mtr.rmse, mtr.urmse, mtr.mae, mtr.cc, mtr.si, mtr.r2],
    doc="Default metrics list to be used in skill tables if specific metrics are not provided.",
)


def _interp_time(df: pd.DataFrame, new_time: pd.DatetimeIndex) -> pd.DataFrame:
    """Interpolate time series to new time index"""
    new_df = (
        df.reindex(df.index.union(new_time))
        .interpolate(method="time", limit_area="inside")
        .reindex(new_time)
    )
    return new_df


TimeDeltaTypes = Union[float, int, np.timedelta64, pd.Timedelta, timedelta]


def _time_delta_to_pd_timedelta(time_delta: TimeDeltaTypes) -> pd.Timedelta:
    if isinstance(time_delta, (timedelta, np.timedelta64)):
        time_delta = pd.Timedelta(time_delta)
    elif np.isscalar(time_delta):
        # assume seconds
        time_delta = pd.Timedelta(time_delta, "s")
    return time_delta


def _remove_model_gaps(
    df: pd.DataFrame,
    mod_index: pd.DatetimeIndex,
    max_gap: TimeDeltaTypes,
) -> pd.DataFrame:
    """Remove model gaps longer than max_gap from dataframe"""
    max_gap = _time_delta_to_pd_timedelta(max_gap)
    valid_time = _get_valid_query_time(mod_index, df.index, max_gap)
    return df.loc[valid_time]


def _get_valid_query_time(
    mod_index: pd.DatetimeIndex, obs_index: pd.DatetimeIndex, max_gap: pd.Timedelta
):
    # init dataframe of available timesteps and their index
    df = pd.DataFrame(index=mod_index)
    df["idx"] = range(len(df))

    # for query times get available left and right index of source times
    df = _interp_time(df, obs_index).dropna()
    df["idxa"] = np.floor(df.idx).astype(int)
    df["idxb"] = np.ceil(df.idx).astype(int)

    # time of left and right source times and time delta
    df["ta"] = mod_index[df.idxa]
    df["tb"] = mod_index[df.idxb]
    df["dt"] = df.tb - df.ta

    # valid query times where time delta is less than max_gap
    valid_idx = df.dt <= max_gap
    return valid_idx


class BaseComparer:
    """Abstract base class for all comparers, only used to inherit from, not to be used directly"""

    @property
    def n_points(self) -> int:
        """number of compared points"""
        return len(self.df)

    @property
    def start(self) -> datetime:
        """start datetime of compared data"""
        return self.df.index[0].to_pydatetime()

    @property
    def end(self) -> datetime:
        """end datetime of compared data"""
        return self.df.index[-1].to_pydatetime()

    @property
    def x(self) -> float:
        return self.observation.x

    @property
    def y(self) -> float:
        return self.observation.y

    @property
    def name(self) -> str:
        """name of comparer (=observation)"""
        return self.observation.name

    @property
    def residual(self):
        # TODO
        return self.mod - np.vstack(self.obs)

    @property
    def obs(self) -> np.ndarray:
        return self.df[self.obs_name].values

    @property
    def mod(self) -> np.ndarray:
        return self.df[self.mod_names].values

    @property
    def n_models(self) -> int:
        return len(self.mod_names)

    @property
    def mod_names(self) -> List[str]:
        return self._mod_names  # list(self.mod_data.keys())

    @property
    def n_variables(self) -> int:
        return len(self._var_names)

    @property
    def all_df(self) -> pd.DataFrame:
        if self._all_df is None:
            self._construct_all_df()
        return self._all_df

    @property
    def metrics(self):
        return options.metrics.list

    @metrics.setter
    def metrics(self, values) -> None:
        if values is None:
            reset_option("metrics.list")
        else:
            options.metrics.list = self._parse_metric(values)

    def __add__(self, other: "BaseComparer") -> "ComparerCollection":

        if not isinstance(other, BaseComparer):
            raise TypeError(f"Cannot add {type(other)} to {type(self)}")

        if (
            isinstance(self, SingleObsComparer)
            and isinstance(other, SingleObsComparer)
            and (self.name == other.name)
        ):
            assert type(self) == type(other)
            missing_models = set(self.mod_names) - set(other.mod_names)
            if len(missing_models) == 0:
                # same obs name and same model names
                cc = self.copy()
                cc.df = pd.concat([cc.df, other.df])
                cc.df = cc.df[~cc.df.index.duplicated(keep="last")]  # 'first'

            else:
                cols = ["x", "y"] if isinstance(self, TrackComparer) else []
                mod_data = [self.df[cols + [m]] for m in self.mod_names]
                for m in other.mod_names:
                    mod_data.append(other.df[cols + [m]])

                cls = self.__class__
                cc = cls.__new__(cls)
                cc.__init__(self.observation, mod_data)
        else:
            cc = ComparerCollection()
            cc.add_comparer(self)
            cc.add_comparer(other)

        return cc

    def _all_df_template(self):
        template = {
            "model": pd.Series([], dtype="category"),
            "observation": pd.Series([], dtype="category"),
        }
        if self.n_variables > 1:
            template["variable"] = pd.Series([], dtype="category")

        template["x"] = pd.Series([], dtype="float")
        template["y"] = pd.Series([], dtype="float")
        template["mod_val"] = pd.Series([], dtype="float")
        template["obs_val"] = pd.Series([], dtype="float")
        res = pd.DataFrame(template)
        return res

    def _construct_all_df(self):
        # TODO: var_name
        res = self._all_df_template()
        frames = []
        cols = res.keys()
        for j in range(self.n_models):
            mod_name = self.mod_names[j]
            df = self.df[[mod_name]].copy()
            df.columns = ["mod_val"]
            df["model"] = mod_name
            df["observation"] = self.observation.name
            if self.n_variables > 1:
                df["variable"] = self.observation.variable_name
            df["x"] = self.x
            df["y"] = self.y
            df["obs_val"] = self.obs
            frames.append(df[cols])

        if len(frames) > 0:
            res = pd.concat(frames)

        self._all_df = res.sort_index()

    def __init__(self, observation, modeldata=None):

        # self._metrics = options.metrics.list
        self.obs_name = "Observation"
        self._obs_names: List[str]
        self._mod_names: List[str]
        self._mod_colors = [
            "#1f78b4",
            "#33a02c",
            "#ff7f00",
            "#93509E",
            "#63CEFF",
            "#fdbf6f",
            "#004165",
            "#8B8D8E",
            "#0098DB",
            "#61C250",
            "#a6cee3",
            "#b2df8a",
            "#fb9a99",
            "#cab2d6",
            "#003f5c",
            "#2f4b7c",
            "#665191",
            "#e31a1c",
        ]

        self._resi_color = "#8B8D8E"
        self._obs_unit_text = ""
        #      darkblue: #004165
        #      midblue:  #0098DB,
        #      gray:     #8B8D8E,
        #      lightblue:#63CEFF,
        #      green:    #61C250
        #      purple:   #93509E
        self.mod_data = None
        self.df = None
        self._all_df = None

        self._mod_start = pd.Timestamp.max
        self._mod_end = pd.Timestamp.min

        self.observation = deepcopy(observation)
        self._obs_unit_text = self.observation._unit_text()
        self.mod_data = {}
        self._obs_names = [observation.name]
        self._var_names = [observation.variable_name]
        self._itemInfos = [observation.itemInfo]

        if modeldata is not None:
            self.add_modeldata(modeldata)

    def add_modeldata(self, modeldata):
        if modeldata is None:
            warnings.warn("Cannot add 'None' modeldata")
            return

        if isinstance(modeldata, list):
            for data in modeldata:
                self.add_modeldata(data)
            return

        if isinstance(modeldata, mikeio.Dataset):
            mod_df = modeldata.to_dataframe()
        elif isinstance(modeldata, pd.DataFrame):
            # TODO: add validation
            mod_df = modeldata
        else:
            raise ValueError(
                f"Unknown modeldata type '{type(modeldata)}' (mikeio.Dataset or pd.DataFrame)"
            )
        if len(mod_df) == 0:
            warnings.warn("Cannot add zero-length modeldata")
            return

        mod_name = mod_df.columns[-1]
        self.mod_data[mod_name] = mod_df
        self._mod_names = list(self.mod_data.keys())

        time = mod_df.index.round(freq="100us")  # 0.0001s accuracy
        mod_df.index = pd.DatetimeIndex(time, freq="infer")

        if mod_df.index[0] < self._mod_start:
            self._mod_start = mod_df.index[0].to_pydatetime()
        if mod_df.index[-1] > self._mod_end:
            self._mod_end = mod_df.index[-1].to_pydatetime()

    def __repr__(self):
        out = []
        out.append(f"<{type(self).__name__}>")
        out.append(f"Observation: {self.observation.name}, n_points={self.n_points}")
        for model in self.mod_names:
            out.append(f" Model: {model}, rmse={self.score(model=model):.3f}")
        return str.join("\n", out)

    def _get_obs_name(self, obs):
        return self._obs_names[self._get_obs_id(obs)]

    def _get_obs_id(self, obs):
        if obs is None or self.n_observations <= 1:
            return 0
        elif isinstance(obs, str):
            if obs in self._obs_names:
                obs_id = self._obs_names.index(obs)
            else:
                raise KeyError(f"obs {obs} could not be found in {self._obs_names}")
        elif isinstance(obs, int):
            if obs < 0:  # Handle negative indices
                obs += self.n_observations
            if obs >= 0 and obs < self.n_observations:
                obs_id = obs
            else:
                raise IndexError(
                    f"obs id {obs} is out of range (0, {self.n_observations-1})"
                )

        else:
            raise TypeError("observation must be None, str or int")
        return obs_id

    def _get_var_name(self, var):
        return self._var_names[self._get_var_id(var)]

    def _get_var_id(self, var):
        if var is None or self.n_variables <= 1:
            return 0
        elif isinstance(var, str):
            if var in self._var_names:
                var_id = self._var_names.index(var)
            else:
                raise KeyError(f"var {var} could not be found in {self._var_names}")
        elif isinstance(var, int):
            if var < 0:  # Handle negative indices
                var += self.n_variables
            if var >= 0 and var < self.n_variables:
                var_id = var
            else:
                raise IndexError(
                    f"var id {var} is out of range (0, {self.n_variables-1})"
                )
        else:
            raise TypeError("variable must be None, str or int")
        return var_id

    def _get_mod_name(self, model):
        return self._mod_names[self._get_mod_id(model)]

    def _get_mod_id(self, model):
        if self.n_models == 0:
            raise ValueError("Cannot select model as comparer contains 0 models!")
        if model is None or self.n_models == 1:
            return 0
        elif isinstance(model, str):
            if model in self.mod_names:
                mod_id = self.mod_names.index(model)
            else:
                raise KeyError(f"model {model} could not be found in {self.mod_names}")
        elif isinstance(model, int):
            if model < 0:  # Handle negative indices
                model += self.n_models
            if model >= 0 and model < self.n_models:
                mod_id = model
            else:
                raise IndexError(
                    f"model id was {model} - must be within 0 and {self.n_models-1}"
                )
        else:
            raise TypeError("model must be None, str or int")
        return mod_id

    def _parse_metric(self, metric, return_list=False):
        if metric is None:
            metric = self.metrics

        if isinstance(metric, str):
            valid_metrics = [
                x[0] for x in getmembers(mtr, isfunction) if x[0][0] != "_"
            ]

            if metric.lower() in valid_metrics:
                metric = getattr(mtr, metric.lower())
            else:
                raise ValueError(
                    f"Invalid metric: {metric}. Valid metrics are {valid_metrics}."
                )
        elif isinstance(metric, Iterable):
            metrics = [self._parse_metric(m) for m in metric]
            return metrics
        elif not callable(metric):
            raise TypeError(
                f"Invalid metric: {metric}. Must be either string or callable."
            )
        if return_list:
            if callable(metric) or isinstance(metric, str):
                metric = [metric]
        return metric

    def skill(
        self,
        by: Union[str, List[str]] = None,
        metrics: list = None,
        model: Union[str, int, List[str], List[int]] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
    ) -> AggregatedSkill:
        """Aggregated skill assessment of model(s)

        Parameters
        ----------
        by : (str, List[str]), optional
            group by column name or by temporal bin via the freq-argument
            (using pandas pd.Grouper(freq)),
            e.g.: 'freq:M' = monthly; 'freq:D' daily
            by default ["model","observation"]
        metrics : list, optional
            list of fmskill.metrics, by default fmskill.options.metrics.list
        model : (str, int, List[str], List[int]), optional
            name or ids of models to be compared, by default all
        observation : (str, int, List[str], List[int])), optional
            name or ids of observations to be compared, by default all
        variable : (str, int, List[str], List[int])), optional
            name or ids of variables to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None

        Returns
        -------
        pd.DataFrame
            skill assessment as a dataframe

        See also
        --------
        sel_df
            a method for filtering/selecting data

        Examples
        --------
        >>> cc = con.extract()
        >>> cc.skill().round(2)
                       n  bias  rmse  urmse   mae    cc    si    r2
        observation
        HKNA         385 -0.20  0.35   0.29  0.25  0.97  0.09  0.99
        EPL           66 -0.08  0.22   0.20  0.18  0.97  0.07  0.99
        c2           113 -0.00  0.35   0.35  0.29  0.97  0.12  0.99

        >>> cc.skill(observation='c2', start='2017-10-28').round(2)
                       n  bias  rmse  urmse   mae    cc    si    r2
        observation
        c2            41  0.33  0.41   0.25  0.36  0.96  0.06  0.99

        >>> cc.skill(by='freq:D').round(2)
                      n  bias  rmse  urmse   mae    cc    si    r2
        2017-10-27  239 -0.15  0.25   0.21  0.20  0.72  0.10  0.98
        2017-10-28  162 -0.07  0.19   0.18  0.16  0.96  0.06  1.00
        2017-10-29  163 -0.21  0.52   0.47  0.42  0.79  0.11  0.99

        >>> df = cc.sel_df(observation=['HKNA','EPL']).copy()
        >>> df['seastate'] = pd.cut(df.obs_val, bins=[0,2,6], labels=['small','large'])
        >>> cc.skill(by=['observation','seastate'], df=df).round(2)
                                n  bias  rmse  urmse   mae    cc    si    r2
        observation seastate
        EPL         small      16  0.02  0.22   0.22  0.17  0.38  0.13  0.98
                    large      50 -0.11  0.22   0.19  0.19  0.98  0.06  0.99
        HKNA        small      61  0.02  0.09   0.09  0.08  0.88  0.05  1.00
                    large     324 -0.23  0.38   0.30  0.28  0.96  0.09  0.99
        """

        metrics = self._parse_metric(metrics, return_list=True)

        df = self.sel_df(
            model=model,
            observation=observation,
            variable=variable,
            start=start,
            end=end,
            area=area,
            df=df,
        )
        if len(df) == 0:
            warnings.warn("No data!")
            return

        n_models = len(df.model.unique())
        n_obs = len(df.observation.unique())
        n_var = len(df.variable.unique()) if (self.n_variables > 1) else 1
        by = self._parse_by(by, n_models, n_obs, n_var)

        res = self._groupby_df(df.drop(columns=["x", "y"]), by, metrics)
        res = self._add_as_field_if_not_in_index(df, skilldf=res)
        return AggregatedSkill(res)

    def _add_as_field_if_not_in_index(
        self, df, skilldf, fields=["model", "observation", "variable"]
    ):
        """Add a field to skilldf if unique in df"""
        for field in reversed(fields):
            if (field == "model") and (self.n_models <= 1):
                continue
            if (field == "variable") and (self.n_variables <= 1):
                continue
            if field not in skilldf.index.names:
                unames = df[field].unique()
                if len(unames) == 1:
                    skilldf.insert(loc=0, column=field, value=unames[0])
        return skilldf

    def _groupby_df(self, df, by, metrics, n_min: int = None):
        def calc_metrics(x):
            row = {}
            row["n"] = len(x)
            for metric in metrics:
                row[metric.__name__] = metric(x.obs_val.values, x.mod_val.values)
            return pd.Series(row)

        # .drop(columns=["x", "y"])

        res = df.groupby(by=by).apply(calc_metrics)

        if n_min:
            # nan for all cols but n
            cols = [col for col in res.columns if not col == "n"]
            res.loc[res.n < n_min, cols] = np.nan

        res["n"] = res["n"].fillna(0)
        res = res.astype({"n": int})

        return res

    def _parse_by(self, by, n_models, n_obs, n_var=1):
        if by is None:
            by = []
            if n_models > 1:
                by.append("model")
            if n_obs > 1:  # or ((n_models == 1) and (n_obs == 1)):
                by.append("observation")
            if n_var > 1:
                by.append("variable")
            if len(by) == 0:
                # default value
                by.append("observation")
            return by

        if isinstance(by, str):
            if by in {"mdl", "mod", "models"}:
                by = "model"
            if by in {"obs", "observations"}:
                by = "observation"
            if by in {"var", "variables", "item"}:
                by = "variable"
            if by[:5] == "freq:":
                freq = by.split(":")[1]
                by = pd.Grouper(freq=freq)
        elif isinstance(by, Iterable):
            by = [self._parse_by(b, n_models, n_obs, n_var) for b in by]
            return by
        else:
            raise ValueError("Invalid by argument. Must be string or list of strings.")
        return by

    def spatial_skill(
        self,
        bins=5,
        binsize: float = None,
        by: Union[str, List[str]] = None,
        metrics: list = None,
        n_min: int = None,
        model: Union[str, int, List[str], List[int]] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
    ):
        """Aggregated spatial skill assessment of model(s) on a regular spatial grid.

        Parameters
        ----------
        bins: int, list of scalars, or IntervalIndex, or tuple of, optional
            criteria to bin x and y by, argument bins to pd.cut(), default 5
            define different bins for x and y a tuple
            e.g.: bins = 5, bins = (5,[2,3,5])
        binsize : float, optional
            bin size for x and y dimension, overwrites bins
            creates bins with reference to round(mean(x)), round(mean(y))
        by : (str, List[str]), optional
            group by column name or by temporal bin via the freq-argument
            (using pandas pd.Grouper(freq)),
            e.g.: 'freq:M' = monthly; 'freq:D' daily
            by default ["model","observation"]
        metrics : list, optional
            list of fmskill.metrics, by default fmskill.options.metrics.list
        n_min : int, optional
            minimum number of observations in a grid cell;
            cells with fewer observations get a score of `np.nan`
        model : (str, int, List[str], List[int]), optional
            name or ids of models to be compared, by default all
        observation : (str, int, List[str], List[int])), optional
            name or ids of observations to be compared, by default all
        variable : (str, int, List[str], List[int])), optional
            name or ids of variables to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None

        Returns
        -------
        xr.Dataset
            skill assessment as a dataset

        See also
        --------
        skill
            a method for aggregated skill assessment

        Examples
        --------
        >>> cc = con.extract()  # with satellite track measurements
        >>> cc.spatial_skill(metrics='bias')
        <xarray.Dataset>
        Dimensions:      (x: 5, y: 5)
        Coordinates:
            observation   'alti'
        * x            (x) float64 -0.436 1.543 3.517 5.492 7.466
        * y            (y) float64 50.6 51.66 52.7 53.75 54.8
        Data variables:
            n            (x, y) int32 3 0 0 14 37 17 50 36 72 ... 0 0 15 20 0 0 0 28 76
            bias         (x, y) float64 -0.02626 nan nan ... nan 0.06785 -0.1143

        >>> ds = cc.spatial_skill(binsize=0.5)
        >>> ds.coords
        Coordinates:
            observation   'alti'
        * x            (x) float64 -1.5 -0.5 0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5
        * y            (y) float64 51.5 52.5 53.5 54.5 55.5 56.5
        """

        metrics = self._parse_metric(metrics, return_list=True)

        df = self.sel_df(
            model=model,
            observation=observation,
            variable=variable,
            start=start,
            end=end,
            area=area,
            df=df,
        )
        if len(df) == 0:
            warnings.warn("No data!")
            return

        df = self._add_spatial_grid_to_df(df=df, bins=bins, binsize=binsize)

        n_models = len(df.model.unique())
        n_obs = len(df.observation.unique())
        by = self._parse_by(by, n_models, n_obs)
        if isinstance(by, str) or (not isinstance(by, Iterable)):
            by = [by]
        if not "x" in by:
            by.insert(0, "x")
        if not "y" in by:
            by.insert(0, "y")

        res = self._groupby_df(
            df.drop(columns=["x", "y"]).rename(columns=dict(xBin="x", yBin="y")),
            by,
            metrics,
            n_min,
        )

        ss = SpatialSkill(res.to_xarray().squeeze())
        return ss

    def _add_spatial_grid_to_df(self, df, bins, binsize):
        if binsize is None:
            # bins from bins
            if isinstance(bins, tuple):
                bins_x = bins[0]
                bins_y = bins[1]
            else:
                bins_x = bins
                bins_y = bins
        else:
            # bins from binsize
            x_ptp = df.x.values.ptp()
            y_ptp = df.y.values.ptp()
            nx = int(np.ceil(x_ptp / binsize))
            ny = int(np.ceil(y_ptp / binsize))
            x_mean = np.round(df.x.mean())
            y_mean = np.round(df.y.mean())
            bins_x = np.arange(
                x_mean - nx / 2 * binsize, x_mean + (nx / 2 + 1) * binsize, binsize
            )
            bins_y = np.arange(
                y_mean - ny / 2 * binsize, y_mean + (ny / 2 + 1) * binsize, binsize
            )
        # cut and get bin centre
        df["xBin"] = pd.cut(df.x, bins=bins_x)
        df["xBin"] = df["xBin"].apply(lambda x: x.mid)
        df["yBin"] = pd.cut(df.y, bins=bins_y)
        df["yBin"] = df["yBin"].apply(lambda x: x.mid)

        return df

    def sel_df(
        self,
        model: Union[str, int, List[str], List[int]] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
    ) -> pd.DataFrame:
        """Select/filter data from all the compared data.
        Used by compare.scatter and compare.skill to select data.

        Parameters
        ----------
        model : (str, int, List[str], List[int]), optional
            name or ids of models to be compared, by default all
        observation : (str, int, List[str], List[int])), optional
            name or ids of observations to be compared, by default all
        variable : (str, int, List[str], List[int])), optional
            name or ids of variables to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None

        Returns
        -------
        pd.DataFrame
            selected data in a dataframe with columns (mod_name,obs_name,x,y,mod_val,obs_val)

        See also
        --------
        skill
            a method for aggregated skill assessment
        scatter
            a method for plotting compared data

        Examples
        --------
        >>> cc = con.extract()
        >>> dfsub = cc.sel_df(observation=['EPL','HKNA'])
        >>> dfsub = cc.sel_df(model=0)
        >>> dfsub = cc.sel_df(start='2017-10-1', end='2017-11-1')
        >>> dfsub = cc.sel_df(area=[0.5,52.5,5,54])

        >>> cc.sel_df(observation='c2', start='2017-10-28').head(3)
                           model observation      x       y   mod_val  obs_val
        2017-10-28 01:00:00 SW_1         EPL  3.276  51.999  1.644092     1.82
        2017-10-28 02:00:00 SW_1         EPL  3.276  51.999  1.755809     1.86
        2017-10-28 03:00:00 SW_1         EPL  3.276  51.999  1.867526     2.11
        """
        if df is None:
            df = self.all_df
        if model is not None:
            models = [model] if np.isscalar(model) else model
            models = [self._get_mod_name(m) for m in models]
            df = df[df.model.isin(models)]
        if observation is not None:
            observation = [observation] if np.isscalar(observation) else observation
            observation = [self._get_obs_name(o) for o in observation]
            df = df[df.observation.isin(observation)]
        if (variable is not None) and (self.n_variables > 1):
            variable = [variable] if np.isscalar(variable) else variable
            variable = [self._get_var_name(v) for v in variable]
            df = df[df.variable.isin(variable)]
        if (start is not None) or (end is not None):
            df = df.loc[start:end]
        if area is not None:
            if self._area_is_bbox(area):
                x0, y0, x1, y1 = area
                df = df[(df.x > x0) & (df.x < x1) & (df.y > y0) & (df.y < y1)]
            elif self._area_is_polygon(area):
                polygon = np.array(area)
                xy = np.column_stack((df.x.values, df.y.values))
                mask = self._inside_polygon(polygon, xy)
                df = df[mask]
            else:
                raise ValueError("area supports bbox [x0,y0,x1,y1] and closed polygon")
        return df

    def _area_is_bbox(self, area):
        is_bbox = False
        if area is not None:
            if not np.isscalar(area):
                area = np.array(area)
                if (area.ndim == 1) & (len(area) == 4):
                    if np.all(np.isreal(area)):
                        is_bbox = True
        return is_bbox

    def _area_is_polygon(self, area) -> bool:
        if area is None:
            return False
        if np.isscalar(area):
            return False
        if not np.all(np.isreal(area)):
            return False
        polygon = np.array(area)
        if polygon.ndim > 2:
            return False

        if polygon.ndim == 1:
            if len(polygon) <= 5:
                return False
            if len(polygon) % 2 != 0:
                return False

        if polygon.ndim == 2:
            if polygon.shape[0] < 3:
                return False
            if polygon.shape[1] != 2:
                return False

        return True

    def _inside_polygon(self, polygon, xy):
        import matplotlib.path as mp

        if polygon.ndim == 1:
            polygon = np.column_stack((polygon[0::2], polygon[1::2]))
        return mp.Path(polygon).contains_points(xy)

    def scatter(
        self,
        *,
        bins: Union[int, float, List[int], List[float]] = 20,
        quantiles: Union[int, List[float]] = None,
        show_points: Union[bool, int, float] = None,
        show_hist: bool = None,
        show_density: bool = None,
        backend: str = "matplotlib",
        figsize: List[float] = (8, 8),
        xlim: List[float] = None,
        ylim: List[float] = None,
        reg_method: str = "ols",
        title: str = None,
        xlabel: str = None,
        ylabel: str = None,
        model: Union[str, int] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
        binsize: float = None,
        nbins: int = None,
        skill_table: Union[str, List[str], bool] = None,
        **kwargs,
    ):
        """Scatter plot showing compared data: observation vs modelled
        Optionally, with density histogram.

        Parameters
        ----------
        bins: (int, float, sequence), optional
            bins for the 2D histogram on the background. By default 20 bins.
            if int, represents the number of bins of 2D
            if float, represents the bin size
            if sequence (list of int or float), represents the bin edges
        quantiles: (int, sequence), optional
            number of quantiles for QQ-plot, by default None and will depend on the scatter data length (10, 100 or 1000)
            if int, this is the number of points
            if sequence (list of floats), represents the desired quantiles (from 0 to 1)
        show_points : (bool, int, float), optional
            Should the scatter points be displayed?
            None means: show all points if fewer than 1e4, otherwise show 1e4 sample points, by default None.
            float: fraction of points to show on plot from 0 to 1. eg 0.5 shows 50% of the points.
            int: if 'n' (int) given, then 'n' points will be displayed, randomly selected
        show_hist : bool, optional
            show the data density as a a 2d histogram, by default None
        show_density: bool, optional
            show the data density as a colormap of the scatter, by default None. If both `show_density` and `show_hist`
        are None, then `show_density` is used by default.
            for binning the data, the previous kword `bins=Float` is used
        backend : str, optional
            use "plotly" (interactive) or "matplotlib" backend, by default "matplotlib"
        figsize : tuple, optional
            width and height of the figure, by default (8, 8)
        xlim : tuple, optional
            plot range for the observation (xmin, xmax), by default None
        ylim : tuple, optional
            plot range for the model (ymin, ymax), by default None
        reg_method : str, optional
            method for determining the regression line
            "ols" : ordinary least squares regression
            "odr" : orthogonal distance regression,
            by default "ols"
        title : str, optional
            plot title, by default None
        xlabel : str, optional
            x-label text on plot, by default None
        ylabel : str, optional
            y-label text on plot, by default None
        model : (int, str), optional
            name or id of model to be compared, by default first
        observation : (int, str, List[str], List[int])), optional
            name or ids of observations to be compared, by default None
        variable : (str, int), optional
            name or id of variable to be compared, by default first
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates[x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            show user-provided data instead of the comparers own data, by default None
        skill_table : str, List[str], bool, optional
            list of fmskill.metrics or boolean, if True then by default fmskill.options.metrics.list.
            This kword adds a box at the right of the scatter plot,
            by default False
        kwargs

        Examples
        ------
        >>> comparer.scatter()
        >>> comparer.scatter(bins=0.2, backend='plotly')
        >>> comparer.scatter(show_points=False, title='no points')
        >>> comparer.scatter(xlabel='all observations', ylabel='my model')
        >>> comparer.scatter(model='HKZN_v2', figsize=(10, 10))
        >>> comparer.scatter(observations=['c2','HKNA'])
        """
        # select model
        mod_id = self._get_mod_id(model)
        mod_name = self.mod_names[mod_id]

        # select variable
        var_id = self._get_var_id(variable)
        var_name = self._var_names[var_id]

        # filter data
        df = self.sel_df(
            df=df,
            model=mod_name,
            observation=observation,
            variable=var_name,
            start=start,
            end=end,
            area=area,
        )
        if len(df) == 0:
            raise Exception("No data found in selection")

        x = df.obs_val
        y = df.mod_val

        unit_text = self._obs_unit_text
        if isinstance(self, ComparerCollection):
            unit_text = self[df.observation[0]]._obs_unit_text

        if xlabel is None:
            xlabel = f"Observation, {unit_text}"

        if ylabel is None:
            ylabel = f"Model, {unit_text}"

        if title is None:
            title = f"{self.mod_names[mod_id]} vs {self.name}"

        if skill_table != None:
            # Calculate Skill if it was requested to add as table on the right of plot
            if skill_table == True:
                if isinstance(self, PointComparer) or (
                    isinstance(self, ComparerCollection) and self.n_observations == 1
                ):
                    skill_df = self.skill(
                        df=df, model=model, observation=observation, variable=variable
                    )
                else:
                    skill_df = self.mean_skill(
                        df=df, model=model, observation=observation, variable=variable
                    )

            # Check for units
            try:
                units = unit_text.split("[")[1].split("]")[0]
            except:
                #     Dimensionless
                units = ""
            if skill_table == False:
                skill_df = None
                units = None
        else:
            # skill_table is None
            skill_df = None
            units = None

        ax=scatter(
            x=x,
            y=y,
            bins=bins,
            quantiles=quantiles,
            show_points=show_points,
            show_hist=show_hist,
            show_density=show_density,
            backend=backend,
            figsize=figsize,
            xlim=xlim,
            ylim=ylim,
            reg_method=reg_method,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            skill_df=skill_df,
            units=units,
            binsize=binsize,
            nbins=nbins,
            **kwargs,
        )
        return ax

    def taylor(
        self,
        model: Union[str, int, List[str], List[int]] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
        normalize_std: bool = False,
        aggregate_observations: bool = True,
        figsize: List[float] = (7, 7),
        marker: str = "o",
        marker_size: float = 6.0,
        title: str = "Taylor diagram",
    ):
        """Taylor diagram showing model std and correlation to observation
        in a single-quadrant polar plot, with r=std and theta=arccos(cc).

        Parameters
        ----------
        model : (int, str), optional
            name or id of model to be compared, by default all
        observation : (int, str, List[str], List[int])), optional
            name or ids of observations to be compared, by default all
        variable : (str, int), optional
            name or id of variable to be compared, by default first
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates[x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            show user-provided data instead of the comparers own data, by default None
        normalize_std : bool, optional
            plot model std normalized with observation std, default False
        aggregate_observations : bool, optional
            should multiple observations be aggregated before plotting
            (or shown individually), default True
        figsize : tuple, optional
            width and height of the figure (should be square), by default (7, 7)
        marker : str, optional
            marker type e.g. "x", "*", by default "o"
        marker_size : float, optional
            size of the marker, by default 6
        title : str, optional
            title of the plot, by default "Taylor diagram"

        Examples
        ------
        >>> comparer.taylor()
        >>> comparer.taylor(observation="c2")
        >>> comparer.taylor(start="2017-10-28", figsize=(5,5))

        References
        ----------
        Copin, Y. (2018). https://gist.github.com/ycopin/3342888, Yannick Copin <yannick.copin@laposte.net>
        """

        if (not aggregate_observations) and (not normalize_std):
            raise ValueError(
                "aggregate_observations=False is only possible if normalize_std=True!"
            )

        metrics = [mtr._std_obs, mtr._std_mod, mtr.cc]
        if aggregate_observations:
            s = self.mean_skill(
                model=model,
                observation=observation,
                variable=variable,
                start=start,
                end=end,
                area=area,
                metrics=metrics,
            )
        else:
            s = self.skill(
                model=model,
                observation=observation,
                variable=variable,
                start=start,
                end=end,
                area=area,
                metrics=metrics,
            )
        if s is None:
            return

        df = s.df
        ref_std = 1.0 if normalize_std else df.iloc[0]["_std_obs"]

        if isinstance(df.index, pd.MultiIndex):
            df.index = df.index.map("_".join)

        df = df[["_std_obs", "_std_mod", "cc"]].copy()
        df.columns = ["obs_std", "std", "cc"]
        pts = [
            TaylorPoint(
                r.Index, r.obs_std, r.std, r.cc, marker=marker, marker_size=marker_size
            )
            for r in df.itertuples()
        ]

        taylor_diagram(
            obs_std=ref_std,
            points=pts,
            figsize=figsize,
            normalize_std=normalize_std,
            title=title,
        )


class SingleObsComparer(BaseComparer):
    def __init__(self, observation, model):
        super().__init__(observation, model)

    def __copy__(self):
        return deepcopy(self)

    def copy(self):
        return self.__copy__()

    def _model2obs_interp(self, obs, mod_df: pd.DataFrame, max_model_gap: Optional[TimeDeltaTypes]):
        """interpolate model to measurement time"""
        df = _interp_time(mod_df.dropna(), obs.time)
        df[self.obs_name] = obs.values

        if max_model_gap is not None:
            df = _remove_model_gaps(df, mod_df.dropna().index, max_model_gap)

        return df

    def skill(
        self,
        by: Union[str, List[str]] = None,
        metrics: list = None,
        model: Union[str, int, List[str], List[int]] = None,
        observation=None,  # Only used to have a compatible interface with other skill mehod TODO refactor to a new sel() method
        variable=None,  # Only used to have a compatible interface with other skill mehod TODO refactor to a new sel() method
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
    ) -> AggregatedSkill:
        """Skill assessment of model(s)

        Parameters
        ----------
        by : (str, List[str]), optional
            group by column name or by temporal bin via the freq-argument
            (using pandas pd.Grouper(freq)),
            e.g.: 'freq:M' = monthly; 'freq:D' daily
            by default ["model"]
        metrics : list, optional
            list of fmskill.metrics, by default fmskill.options.metrics.list
        model : (str, int, List[str], List[int]), optional
            name or ids of models to be compared, by default all
        freq : string, optional
            do temporal binning using pandas pd.Grouper(freq),
            typical examples: 'M' = monthly; 'D' daily
            by default None
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None

        Returns
        -------
        AggregatedSkill
            skill assessment object

        See also
        --------
        sel_df
            a method for filtering/selecting data

        Examples
        --------
        >>> cc = con.extract()
        >>> cc['c2'].skill().round(2)
                       n  bias  rmse  urmse   mae    cc    si    r2
        observation
        c2           113 -0.00  0.35   0.35  0.29  0.97  0.12  0.99

        >>> cc['c2'].skill(by='freq:D').round(2)
                     n  bias  rmse  urmse   mae    cc    si    r2
        2017-10-27  72 -0.19  0.31   0.25  0.26  0.48  0.12  0.98
        2017-10-28   0   NaN   NaN    NaN   NaN   NaN   NaN   NaN
        2017-10-29  41  0.33  0.41   0.25  0.36  0.96  0.06  0.99

        >>> df = cc['c2'].sel_df().copy()
        >>> df['Hm0 group'] = pd.cut(df.obs_val, bins=[0,2,6])
        >>> cc['c2'].skill(by='Hm0 group', df=df).round(2)
                    n  bias  rmse  urmse   mae    cc    si    r2
        Hm0 group
        (0, 2]     33 -0.09  0.23   0.22  0.21  0.46  0.12  0.98
        (2, 6]     80  0.03  0.39   0.39  0.33  0.97  0.12  0.99
        """
        # only for improved documentation
        return super().skill(
            model=model,
            by=by,
            start=start,
            end=end,
            area=area,
            df=df,
            metrics=metrics,
        )

    def score(
        self,
        metric=mtr.rmse,
        model: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
    ) -> float:
        """Model skill score

        Parameters
        ----------
        metric : list, optional
            a single metric from fmskill.metrics, by default rmse
        model : (str, int, List[str], List[int]), optional
            name or ids of models to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None

        Returns
        -------
        float
            skill score as a single number (for each model)

        See also
        --------
        skill
            a method for skill assessment returning a pd.DataFrame

        Examples
        --------
        >>> cc = con.extract()
        >>> cc['c2'].score()
        0.3517964910888918

        >>> import fmskill.metrics as mtr
        >>> cc['c2'].score(metric=mtr.mape)
        11.567399646108198
        """
        metric = self._parse_metric(metric)
        if not (callable(metric) or isinstance(metric, str)):
            raise ValueError("metric must be a string or a function")

        s = self.skill(
            metrics=[metric],
            model=model,
            start=start,
            end=end,
            area=area,
            df=df,
        )
        if s is None:
            return
        df = s.df
        values = df[metric.__name__].values
        if len(values) == 1:
            values = values[0]
        return values

    def sel_df(
        self,
        model: Union[str, int, List[str], List[int]] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
    ) -> pd.DataFrame:
        """Select/filter data from all the compared data.
        Used by compare.scatter and compare.skill to select data.

        Parameters
        ----------
        model : (str, int, List[str], List[int]), optional
            name or ids of models to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None

        Returns
        -------
        pd.DataFrame
            selected data in a dataframe with columns (model,observation,x,y,mod_val,obs_val)

        See also
        --------
        skill
            a method for aggregated skill assessment
        scatter
            a method for plotting compared data

        Examples
        --------
        >>> cc = con.extract()
        >>> dfsub = cc['c2'].sel_df(model=0)
        >>> dfsub = cc['c2'].sel_df(start='2017-10-1', end='2017-11-1')
        >>> dfsub = cc['c2'].sel_df(area=[0.5,52.5,5,54])
        """
        # only for improved documentation
        return super().sel_df(
            model=model,
            observation=observation,
            variable=variable,
            start=start,
            end=end,
            area=area,
            df=df,
        )

    def taylor(
        self,
        model: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
        normalize_std: bool = False,
        figsize: List[float] = (7, 7),
        marker: str = "o",
        marker_size: float = 6.0,
        title: str = "Taylor diagram",
    ):
        """Taylor diagram showing model std and correlation to observation
        in a single-quadrant polar plot, with r=std and theta=arccos(cc).

        Parameters
        ----------
        model : (int, str), optional
            name or id of model to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates[x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            show user-provided data instead of the comparers own data, by default None
        normalize_std : bool, optional
            plot model std normalized with observation std, default False
        figsize : tuple, optional
            width and height of the figure (should be square), by default (7, 7)
        marker : str, optional
            marker type e.g. "x", "*", by default "o"
        marker_size : float, optional
            size of the marker, by default 6
        title : str, optional
            title of the plot, by default "Taylor diagram"

        Examples
        ------
        >>> comparer.taylor()
        >>> comparer.taylor(start="2017-10-28", figsize=(5,5))

        References
        ----------
        Copin, Y. (2018). https://gist.github.com/ycopin/3342888, Yannick Copin <yannick.copin@laposte.net>
        """

        metrics = [mtr._std_obs, mtr._std_mod, mtr.cc]
        s = self.skill(
            model=model,
            start=start,
            end=end,
            area=area,
            metrics=metrics,
        )
        if s is None:
            return
        df = s.df
        ref_std = 1.0 if normalize_std else df.iloc[0]["_std_obs"]

        df = df[["_std_obs", "_std_mod", "cc"]].copy()
        df.columns = ["obs_std", "std", "cc"]

        pts = [
            TaylorPoint(
                r.Index, r.obs_std, r.std, r.cc, marker=marker, marker_size=marker_size
            )
            for r in df.itertuples()
        ]

        taylor_diagram(
            obs_std=ref_std,
            points=pts,
            figsize=figsize,
            obs_text=f"Obs: {self.name}",
            normalize_std=normalize_std,
            title=title,
        )

    def remove_bias(self, correct="Model"):
        bias = self.residual.mean(axis=0)
        if correct == "Model":
            for j in range(self.n_models):
                mod_name = self.mod_names[j]
                mod_df = self.mod_data[mod_name]
                mod_df[mod_name] = mod_df.values - bias[j]
            self.df[self.mod_names] = self.mod - bias
        elif correct == "Observation":
            # what if multiple models?
            self.df[self.obs_name] = self.obs + bias
        else:
            raise ValueError(
                f"Unknown correct={correct}. Only know 'Model' and 'Observation'"
            )
        return bias

    def residual_hist(self, bins=100, title=None, color=None, **kwargs):
        """plot histogram of residual values

        Parameters
        ----------
        bins : int, optional
            specification of bins, by default 100
        title : str, optional
            plot title, default: Residuals, [name]
        color : str, optional
            residual color, by default "#8B8D8E"
        kwargs : other keyword arguments to plt.hist()
        """
        color = self._resi_color if color is None else color
        title = f"Residuals, {self.name}" if title is None else title
        plt.hist(self.residual, bins=bins, color=color, **kwargs)
        plt.title(title)
        plt.xlabel(f"Residuals of {self._obs_unit_text}")

    def hist(
        self, *, model=None, bins=100, title=None, density=True, alpha=0.5, **kwargs
    ):
        """Plot histogram of model data and observations.

        Wraps pandas.DataFrame hist() method.

        Parameters
        ----------
        model : (str, int), optional
            name or id of model to be plotted, by default 0
        bins : int, optional
            number of bins, by default 100
        title : str, optional
            plot title, default: [model name] vs [observation name]
        density: bool, optional
            If True, draw and return a probability density
        alpha : float, optional
            alpha transparency fraction, by default 0.5
        kwargs : other keyword arguments to df.hist()

        Returns
        -------
        matplotlib axes

        See also
        --------
        pandas.Series.hist
        matplotlib.axes.Axes.hist

        """
        mod_id = self._get_mod_id(model)
        mod_name = self.mod_names[mod_id]

        title = f"{mod_name} vs {self.name}" if title is None else title

        kwargs["alpha"] = alpha
        kwargs["density"] = density
        ax = self.df[mod_name].hist(bins=bins, color=self._mod_colors[mod_id], **kwargs)
        self.df[self.obs_name].hist(
            bins=bins, color=self.observation.color, ax=ax, **kwargs
        )
        ax.legend([mod_name, self.obs_name])
        plt.title(title)
        plt.xlabel(f"{self._obs_unit_text}")
        if density:
            plt.ylabel("density")
        else:
            plt.ylabel("count")

        return ax


class PointComparer(SingleObsComparer):
    """
    Comparer for observations from fixed locations

    Examples
    --------
    >>> mr = ModelResult("Oresund2D.dfsu", item=0)
    >>> o1 = PointObservation("klagshamn.dfs0", item=0, x=366844, y=6154291, name="Klagshamn")
    >>> con = Connector(o1, mr)
    >>> comparer = con.extract()
    >>> comparer['Klagshamn']
    """

    def __init__(
        self, observation, modeldata, max_model_gap: Optional[TimeDeltaTypes] = None
    ):
        super().__init__(observation, modeldata)
        assert isinstance(observation, PointObservation)
        mod_start = self._mod_start - timedelta(seconds=1)  # avoid rounding err
        mod_end = self._mod_end + timedelta(seconds=1)
        self.observation.df = self.observation.df[mod_start:mod_end]

        if not isinstance(modeldata, list):
            modeldata = [modeldata]
        # max_model_gap = self._parse_max_gap(modeldata, max_model_gap)

        for j, data in enumerate(modeldata):
            df = self._model2obs_interp(self.observation, data, max_model_gap).iloc[
                :, ::-1
            ]
            if j == 0:
                self.df = df
            else:
                self.df[self.mod_names[j]] = df[self.mod_names[j]]

        self.df.index.name = "datetime"
        self.df.dropna(inplace=True)

    def plot_timeseries(
        self, title=None, *, ylim=None, figsize=None, backend="matplotlib", **kwargs
    ):
        """Timeseries plot showing compared data: observation vs modelled

        Parameters
        ----------
        title : str, optional
            plot title, by default None
        ylim : tuple, optional
            plot range for the model (ymin, ymax), by default None
        figsize : (float, float), optional
            figure size, by default None
        backend : str, optional
            use "plotly" (interactive) or "matplotlib" backend, by default "matplotlib"backend:

        Examples
        ------
        >>> comparer.plot_timeseries()
        >>> comparer.plot_timeseries(title="")
        >>> comparer.plot_timeseries(ylim=[0,6])
        >>> comparer.plot_timeseries(backend="plotly")
        >>> comparer.plot_timeseries(backend="plotly", showlegend=False)
        """

        if title is None:
            title = self.name

        if backend == "matplotlib":
            _, ax = plt.subplots(figsize=figsize)
            for j in range(self.n_models):
                key = self.mod_names[j]
                self.mod_data[key].plot(ax=ax, color=self._mod_colors[j])

            ax.scatter(
                self.df.index,
                self.df[[self.obs_name]],
                marker=".",
                color=self.observation.color,
            )
            ax.set_ylabel(self._obs_unit_text)
            ax.legend([*self.mod_names, self.obs_name])
            ax.set_ylim(ylim)
            plt.title(title)
            return ax

        elif backend == "plotly":  # pragma: no cover
            import plotly.graph_objects as go

            mod_scatter_list = []
            for j in range(self.n_models):
                key = self.mod_names[j]
                mod_df = self.mod_data[key]
                mod_scatter_list.append(
                    go.Scatter(
                        x=mod_df.index,
                        y=mod_df.iloc[:, 0],
                        name=key,
                        line=dict(color=self._mod_colors[j]),
                    )
                )

            fig = go.Figure(
                [
                    *mod_scatter_list,
                    go.Scatter(
                        x=self.df.index,
                        y=self.df[self.obs_name],
                        name=self.obs_name,
                        mode="markers",
                        marker=dict(color=self.observation.color),
                    ),
                ]
            )

            fig.update_layout(title=title, yaxis_title=self._obs_unit_text, **kwargs)
            fig.update_yaxes(range=ylim)

            fig.show()
        else:
            raise ValueError(f"Plotting backend: {backend} not supported")


class TrackComparer(SingleObsComparer):
    """
    Comparer for observations from changing locations i.e. `TrackObservation`

    Examples
    --------
    >>> mr = ModelResult("HKZN_local_2017.dfsu", item=2)
    >>> c2 = TrackObservation("Alti_c2_Dutch.dfs0", item=3, name="c2")
    >>> con = Connector(c2, mr)
    >>> comparer = con.extract()
    >>> comparer['c2']
    """

    @property
    def x(self):
        return self.df.iloc[:, 0]

    @property
    def y(self):
        return self.df.iloc[:, 1]

    def __init__(self, observation, modeldata, max_model_gap: float = None):
        super().__init__(observation, modeldata)
        assert isinstance(observation, TrackObservation)
        self.observation.df = self.observation.df[self._mod_start : self._mod_end]

        if not isinstance(modeldata, list):
            modeldata = [modeldata]
        # max_model_gap = self._parse_max_gap(modeldata, max_model_gap)

        for j, data in enumerate(modeldata):
            df = self._model2obs_interp(self.observation, data, max_model_gap)
            # rename first columns to x, y
            df.columns = ["x", "y", *list(df.columns)[2:]]
            if (len(df) > 0) and (len(df) == len(self.observation.df)):
                ok = self._obs_mod_xy_distance_acceptable(df, self.observation.df)
                # set model to NaN if too far away from obs location
                df.loc[~ok, self.mod_names[j]] = np.nan
                if sum(ok) == 0:
                    warnings.warn(
                        "no (spatial) overlap between model and observation points"
                    )
            if j == 0:
                # change order of obs and model
                cols = ["x", "y", self.obs_name, self.mod_names[j]]
                self.df = df[cols]
            else:
                self.df[self.mod_names[j]] = df[self.mod_names[j]]

        self.df.index.name = "datetime"
        self.df = self.df.dropna()

    def _obs_mod_xy_distance_acceptable(self, df_mod, df_obs):
        mod_xy = df_mod.loc[:, ["x", "y"]].values
        obs_xy = df_obs.iloc[:, :2].values
        d_xy = np.sqrt(np.sum((obs_xy - mod_xy) ** 2, axis=1))
        tol_xy = self._minimal_accepted_distance(obs_xy)
        return d_xy < tol_xy

    @staticmethod
    def _minimal_accepted_distance(obs_xy):
        # all consequtive distances
        vec = np.sqrt(np.sum(np.diff(obs_xy, axis=0), axis=1) ** 2)
        # fraction of small quantile
        return 0.5 * np.quantile(vec, 0.1)


class ComparerCollection(Mapping, Sequence, BaseComparer):
    """
    Collection of comparers, constructed by calling the `ModelResult.extract` method.

    Examples
    --------
    >>> mr = ModelResult("Oresund2D.dfsu", item=0)
    >>> o1 = PointObservation("klagshamn.dfs0", item=0, x=366844, y=6154291, name="Klagshamn")
    >>> o2 = PointObservation("drogden.dfs0", item=0, x=355568.0, y=6156863.0)
    >>> con = Connector()
    >>> con.add(o1, mr)
    >>> con.add(o2, mr)
    >>> comparer = con.extract()

    """

    @property
    def name(self) -> str:
        return "Observations"

    @property
    def n_points(self) -> int:
        """number of compared points"""
        return len(self.all_df)

    @property
    def start(self) -> datetime:
        """start datetime of compared data"""
        return self._start

    @property
    def end(self) -> datetime:
        """end datetime of compared data"""
        return self._end

    @property
    def var_names(self):
        """List of variable names"""
        return self._var_names

    @var_names.setter
    def var_names(self, value):
        if np.isscalar(value):
            value = [value]
        if len(value) != self.n_variables:
            raise ValueError(f"Length of var_names must be {self.n_variables}")
        for var_id, new_var in enumerate(value):
            for c in self.comparers.values():
                if c._var_names[0] == self.var_names[var_id]:
                    c.observation.variable_name = new_var
                    c._var_names = [new_var]
        if self.n_variables > 1:
            if self._all_df is not None:
                self._all_df["variable"]
                for old_var, new_var in zip(self.var_names, value):
                    self._all_df.loc[
                        self._all_df.variable == old_var, "variable"
                    ] = new_var
        self._var_names = value

    @property
    def obs_names(self):
        """List of observation names"""
        return self._obs_names

    @property
    def n_observations(self) -> int:
        """Number of observations"""
        return self.n_comparers

    @property
    def n_comparers(self) -> int:
        """Number of comparers"""
        return len(self.comparers)

    def _construct_all_df(self):
        # TODO: var_name
        res = self._all_df_template()
        frames = []
        cols = res.keys()
        for cmp in self.comparers.values():
            for j in range(cmp.n_models):
                mod_name = cmp.mod_names[j]
                df = cmp.df[[mod_name]].copy()
                df.columns = ["mod_val"]
                df["model"] = mod_name
                df["observation"] = cmp.observation.name
                if self.n_variables > 1:
                    df["variable"] = cmp.observation.variable_name
                df["x"] = cmp.x
                df["y"] = cmp.y
                df["obs_val"] = cmp.obs
                frames.append(df[cols])
        if len(frames) > 0:
            res = pd.concat(frames)
        self._all_df = res.sort_index()
        self._all_df.index.name = "datetime"

    def __init__(self, comparers=None):
        # super().__init__(observation=None, modeldata=None)  # Not possible since init signature is different compared to BaseComparer
        # self._metrics = options.metrics.list
        self._all_df = None
        self._start = datetime(2900, 1, 1)
        self._end = datetime(1, 1, 1)
        self._mod_names = []
        self._obs_names = []
        self._var_names = []
        self._itemInfos = []

        self.comparers = {}

        if comparers is not None:
            for c in comparers:
                if c is not None:
                    self._add_comparer(c)

    def __repr__(self):
        out = []
        out.append(f"<{type(self).__name__}>")
        for key, value in self.comparers.items():
            out.append(f"{type(value).__name__}: {key}")
        return str.join("\n", out)

    def __getitem__(self, x):
        if isinstance(x, slice):
            cmps = [self[xi] for xi in range(*x.indices(len(self)))]
            cc = ComparerCollection(cmps)
            return cc

        if isinstance(x, int):
            x = self._get_obs_name(x)

        return self.comparers[x]

    def __len__(self) -> int:
        return len(self.comparers)

    def __iter__(self):
        return iter(self.comparers.values())

    def __copy__(self):
        cls = self.__class__
        cp = cls.__new__(cls)
        cp.__init__()
        for c in self.comparers.values():
            cp.add_comparer(c)
        return cp

    def copy(self):
        return self.__copy__()

    def add_comparer(self, comparer: BaseComparer):
        """Add another Comparer to this collection.

        Parameters
        ----------
        comparer : (PointComparer, TrackComparer, ComparerCollection)
            Comparer to add to this collection
        """
        if isinstance(comparer, ComparerCollection):
            for c in comparer:
                self._add_comparer(c)
        else:
            self._add_comparer(comparer)

    def _add_comparer(self, comparer: SingleObsComparer):
        if comparer.name in self.comparers:
            # comparer with this name already exists!
            # maybe the user is trying to add a new model
            # or a new time period
            self.comparers[comparer.name] = self.comparers[comparer.name] + comparer
        else:
            self.comparers[comparer.name] = comparer

        for mod_name in comparer.mod_names:
            if mod_name not in self._mod_names:
                self._mod_names.append(mod_name)
        self._obs_names.append(comparer.observation.name)
        if comparer.observation.variable_name not in self._var_names:
            self._var_names.append(comparer.observation.variable_name)

        # check if already in...
        self._itemInfos.append(comparer.observation.itemInfo)

        if comparer.start < self.start:
            self._start = comparer.start
        if comparer.end > self.end:
            self._end = comparer.end
        self._obs_unit_text = comparer.observation._unit_text()

        self._all_df = None

    def hist(
        self,
        bins=100,
        model: Union[str, int] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
        title: str = None,
        density=True,
        alpha: float = 0.5,
        **kwargs,
    ):
        """Plot histogram of specific model and all observations.

        Wraps pandas.DataFrame hist() method.

        Parameters
        ----------
        bins : int, optional
            number of bins, by default 100
        model : (str, int), optional
            name or id of specific model to be plotted, by default 0
        observation : (str, int, List[str], List[int])), optional
            name or ids of observations to be compared, by default all
        variable : (str, int, List[str], List[int])), optional
            name or ids of variables to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None
        title : str, optional
            plot title, default: observation name
        density: bool, optional
            If True, draw and return a probability density
        alpha : float, optional
            alpha transparency fraction, by default 0.5
        kwargs : other keyword arguments to df.hist()

        Returns
        -------
        matplotlib axes

        See also
        --------
        pandas.Series.hist
        matplotlib.axes.Axes.hist
        """
        mod_id = self._get_mod_id(model)
        mod_name = self.mod_names[mod_id]

        # filter data
        df = self.sel_df(
            df=df,
            model=mod_name,
            observation=observation,
            variable=variable,
            start=start,
            end=end,
            area=area,
        )
        if len(df) == 0:
            warnings.warn("No data!")
            return

        title = f"{mod_name} vs Observations" if title is None else title

        kwargs["alpha"] = alpha
        kwargs["density"] = density
        ax = df.mod_val.hist(bins=bins, color=self[0]._mod_colors[mod_id], **kwargs)
        df.obs_val.hist(bins=bins, color=self[0].observation.color, ax=ax, **kwargs)
        ax.legend([mod_name, "observations"])
        plt.title(title)
        plt.xlabel(f"{self._obs_unit_text}")

        if density:
            plt.ylabel("density")
        else:
            plt.ylabel("count")

        return ax

    def mean_skill(
        self,
        *,
        weights: Union[str, List[float], Dict[str, float]] = None,
        metrics: list = None,
        model: Union[str, int, List[str], List[int]] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
    ) -> AggregatedSkill:
        """Weighted mean of skills

        First, the skill is calculated per observation,
        the weighted mean of the skills is then found.

        .. warning::
            This method is NOT the mean skill of all observational points! (mean_skill_points)

        Parameters
        ----------
        weights : (str, List(float), Dict(str, float)), optional
            None: use observations weight attribute
            "equal": giving all observations equal weight,
            "points": giving all points equal weight,
            list of weights e.g. [0.3, 0.3, 0.4] per observation,
            dictionary of observations with special weigths, others will be set to 1.0
            by default None (i.e. observations weight attribute if assigned else "equal")
        metrics : list, optional
            list of fmskill.metrics, by default fmskill.options.metrics.list
        model : (str, int, List[str], List[int]), optional
            name or ids of models to be compared, by default all
        observation : (str, int, List[str], List[int])), optional
            name or ids of observations to be compared, by default all
        variable : (str, int, List[str], List[int])), optional
            name or ids of variables to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None

        Returns
        -------
        AggregatedSkill
            mean skill assessment as a skill object

        See also
        --------
        skill
            skill assessment per observation
        mean_skill_points
            skill assessment pooling all observation points together

        Examples
        --------
        >>> cc = con.extract()
        >>> cc.mean_skill().round(2)
                      n  bias  rmse  urmse   mae    cc    si    r2
        HKZN_local  564 -0.09  0.31   0.28  0.24  0.97  0.09  0.99
        >>> s = cc.mean_skill(weights="equal")
        >>> s = cc.mean_skill(weights="points")
        >>> s = cc.mean_skill(weights={"EPL": 2.0}) # more weight on EPL, others=1.0
        """

        # filter data
        df = self.sel_df(
            df=df,
            model=model,
            observation=observation,
            variable=variable,
            start=start,
            end=end,
            area=area,
        )
        if len(df) == 0:
            warnings.warn("No data!")
            return

        mod_names = df.model.unique()
        obs_names = df.observation.unique()
        var_names = self.var_names
        if self.n_variables > 1:
            var_names = df.variable.unique()
        n_models = len(mod_names)

        # skill assessment
        metrics = self._parse_metric(metrics, return_list=True)
        s = self.skill(df=df, metrics=metrics)
        if s is None:
            return
        skilldf = s.df

        # weights
        weights = self._parse_weights(weights, obs_names)
        skilldf["weights"] = (
            skilldf.n if weights is None else np.tile(weights, n_models)
        )

        weighted_mean = lambda x: np.average(x, weights=skilldf.loc[x.index, "weights"])

        # group by
        by = self._mean_skill_by(skilldf, mod_names, var_names)
        agg = {"n": np.sum}
        for metric in metrics:
            agg[metric.__name__] = weighted_mean
        res = skilldf.groupby(by).agg(agg)

        # output
        res = self._add_as_field_if_not_in_index(df, res, fields=["model", "variable"])
        return AggregatedSkill(res.astype({"n": int}))

    def mean_skill_points(
        self,
        *,
        metrics: list = None,
        model: Union[str, int, List[str], List[int]] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
    ) -> AggregatedSkill:
        """Mean skill of all observational points

        All data points are pooled (disregarding which observation they belong to),
        the skill is then found (for each model).

        .. note::
            No weighting can be applied with this method,
            use mean_skill() if you need to apply weighting

        .. warning::
            This method is NOT the mean of skills (mean_skill)

        Parameters
        ----------
        metrics : list, optional
            list of fmskill.metrics, by default fmskill.options.metrics.list
        model : (str, int, List[str], List[int]), optional
            name or ids of models to be compared, by default all
        observation : (str, int, List[str], List[int])), optional
            name or ids of observations to be compared, by default all
        variable : (str, int, List[str], List[int])), optional
            name or ids of variables to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None

        Returns
        -------
        AggregatedSkill
            mean skill assessment as a skill object

        See also
        --------
        skill
            skill assessment per observation
        mean_skill
            weighted mean of skills (not the same as this method)

        Examples
        --------
        >>> cc = con.extract()
        >>> cc.mean_skill_points()
        """

        # filter data
        df = self.sel_df(
            df=df,
            model=model,
            observation=observation,
            variable=variable,
            start=start,
            end=end,
            area=area,
        )
        if len(df) == 0:
            warnings.warn("No data!")
            return

        dfall = df.copy()
        dfall["observation"] = "all"
        return self.skill(df=dfall, metrics=metrics)

    def _mean_skill_by(self, skilldf, mod_names, var_names):
        by = []
        if len(mod_names) > 1:
            by.append("model")
        if len(var_names) > 1:
            by.append("variable")
        if len(by) == 0:
            if (self.n_variables > 1) and ("variable" in skilldf):
                by.append("variable")
            elif "model" in skilldf:
                by.append("model")
            else:
                by = [mod_names[0]] * len(skilldf)
        return by

    def _parse_weights(self, weights, observations):

        if observations is None:
            observations = self._obs_names
        else:
            observations = [observations] if np.isscalar(observations) else observations
            observations = [self._get_obs_name(o) for o in observations]
        n_obs = len(observations)

        if weights is None:
            # get weights from observation objects
            # default is equal weight to all
            weights = [self.comparers[o].observation.weight for o in observations]
        else:
            if isinstance(weights, int):
                weights = np.ones(n_obs)  # equal weight to all
            elif isinstance(weights, dict):
                w_dict = weights
                weights = [w_dict.get(name, 1.0) for name in (self.obs_names)]

            elif isinstance(weights, str):
                if weights.lower() == "equal":
                    weights = np.ones(n_obs)  # equal weight to all
                elif "point" in weights.lower():
                    weights = None  # no weight => use n_points
                else:
                    raise ValueError(
                        "unknown weights argument (None, 'equal', 'points', or list of floats)"
                    )
            elif not np.isscalar(weights):
                if n_obs == 1:
                    if len(weights) > 1:
                        warnings.warn(
                            "Cannot apply multiple weights to one observation"
                        )
                    weights = [1.0]
                if not len(weights) == n_obs:
                    raise ValueError(
                        f"weights must have same length as observations: {observations}"
                    )
        if weights is not None:
            assert len(weights) == n_obs
        return weights

    def score(
        self,
        *,
        weights: Union[str, List[float], Dict[str, float]] = None,
        metric=mtr.rmse,
        model: Union[str, int, List[str], List[int]] = None,
        observation: Union[str, int, List[str], List[int]] = None,
        variable: Union[str, int, List[str], List[int]] = None,
        start: Union[str, datetime] = None,
        end: Union[str, datetime] = None,
        area: List[float] = None,
        df: pd.DataFrame = None,
    ) -> float:
        """Weighted mean score of model(s) over all observations

        Wrapping mean_skill() with a single metric.

        NOTE: will take simple mean over different variables

        Parameters
        ----------
        weights : (str, List(float), Dict(str, float)), optional
            None: use observations weight attribute
            "equal": giving all observations equal weight,
            "points": giving all points equal weight,
            list of weights e.g. [0.3, 0.3, 0.4] per observation,
            dictionary of observations with special weigths, others will be set to 1.0
            by default None (i.e. observations weight attribute if assigned else "equal")
        metric : list, optional
            a single metric from fmskill.metrics, by default rmse
        model : (str, int, List[str], List[int]), optional
            name or ids of models to be compared, by default all
        observation : (str, int, List[str], List[int])), optional
            name or ids of observations to be compared, by default all
        variable : (str, int, List[str], List[int])), optional
            name or ids of variables to be compared, by default all
        start : (str, datetime), optional
            start time of comparison, by default None
        end : (str, datetime), optional
            end time of comparison, by default None
        area : list(float), optional
            bbox coordinates [x0, y0, x1, y1],
            or polygon coordinates [x0, y0, x1, y1, ..., xn, yn],
            by default None
        df : pd.dataframe, optional
            user-provided data instead of the comparers own data, by default None

        Returns
        -------
        float
            mean of skills score as a single number (for each model)

        See also
        --------
        skill
            skill assessment per observation
        mean_skill
            weighted mean of skills assessment
        mean_skill_points
            skill assessment pooling all observation points together

        Examples
        --------
        >>> cc = con.extract()
        >>> cc.score()
        0.30681206
        >>> cc.score(weights=[0.1,0.1,0.8])
        0.3383011631797379

        >>> cc.score(weights='points', metric="mape")
        8.414442957854142
        """
        metric = self._parse_metric(metric)
        if not (callable(metric) or isinstance(metric, str)):
            raise ValueError("metric must be a string or a function")

        if model is None:
            models = self._mod_names
        else:
            models = [model] if np.isscalar(model) else model
            models = [self._get_mod_name(m) for m in models]
        n_models = len(models)

        skill = self.mean_skill(
            weights=weights,
            metrics=[metric],
            model=models,
            observation=observation,
            variable=variable,
            start=start,
            end=end,
            area=area,
            df=df,
        )
        if skill is None:
            return

        df = skill.df

        if n_models == 1:
            score = df[metric.__name__].values.mean()
        else:
            score = {}
            for model in models:
                mtr_val = df.loc[model][metric.__name__]
                if not np.isscalar(mtr_val):
                    # e.g. mean over different variables!
                    mtr_val = mtr_val.values.mean()
                score[model] = mtr_val

        return score
