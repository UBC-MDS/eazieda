import pandas as pd
import altair as alt
import numpy as np


def corr_plot(
        data,
        features,
        method="pearson",
        plot_width=600,
        plot_height=400):
    """
    Generates a correlation plot for a list of features in a given dataframe

    Parameters
    ----------
    data: pandas.core.frame.DataFrame
        The input dataframe


    features: list
        A list of strings that represents numerical feature names
        len(features) >=2 


    method: str, default = "pearson"
        The correlation method
        Other correlation methods are "spearman" or "kendall"


    plot_width: int, default = 600
        The width of the plot


    plot_height: int, default = 400
        The height of the plot


    Returns
    -------
    `altair plot`
        An interactive altair correlation plot


    Examples
    --------
    >>> from eazieda.eazieda import corr_plot
    >>> from vega_datasets import data
    >>> df = data.iris()
    >>> corr_plot(df, ["petal_length", "petal_width", "sepal_length"])
    """
    pass


def outliers(s, method="zscore", remove=False):
    """
    Detects outliers in a pandas series

    Parameters
    ----------
    s : pandas.core.series.Series
        Pandas Series for which the outliers need to be found
    method : str, default = "zscore"
        The algorithm/method used for outlier detection. 
        One of 'zscore',  'iforest', 'dbscan', 'iqr'
    remove : bool, default = False
        in-place removal of the outliers

    Returns
    -------
    pandas.core.series.Series
        series of outliers

    Examples
    --------
    >>> from eazieda.eazieda import outliers
    >>> s = pd.Series([1,2,3,4,5,6,100, 101])
    >>> outliers(s)
    0    100
    1    101
    dtype: int64
    """
    pass


def categorical_histograms(data, features, plot_width=600, plot_height=400):
    """
    Generates histograms for numeric and bar plots for categorical features

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        A Pandas Dataframe
    features : list
        A list of strings that represents numerical feature names
    plot_width: int, default = 600
        The width of the plot
    plot_height: int, default = 400
        The height of the plot

    Returns
    -------
    `altair plot`
        A combined altair correlation plot

    Examples
    --------
    >>> from eazieda.eazieda import categorical_histograms
    >>> from vega_datasets import data
    >>> df = data.iris()
    >>> categorical_histograms(df, ["petal_length",
    >>>  "petal_width", "sepal_length"])
    """
    pass


def missing_imputed(
        data,
        impute=False,
        method_num="mean",
        method_non_num="most_frequent"
        ):
    """
    Return the number/percentage of missing values for each column 
    in the dataframe as well as giving the 
    choice of imputing the missing values in place

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        A Pandas Dataframe for which the missing values need to be detected
    impute : bool, default = False
        Whether to impute the missing values in place.
    method_num : str, default = "mean"
        The method used for imputing numerical missing values. 
        This is only 
        applicable if impute=True.
        One of 'drop', mean', 'median'
    method_non_num: str, default = "most_frequent"
        The method used for imputing non-numerical missing values. 
        This is only applicable if impute=True.
        One of 'drop', 'most_frequent'

    Returns
    -------
    pandas.core.frame.DataFrame
        A dataframe contains two columns: the number of missing values and 
        the percentage of missing values for each column

    Examples
    --------
    >>> from eazieda.eazieda import missing_imputed
    >>> df = pd.DataFrame([[1, "x"], [np.nan, "y"], [2, np.nan],
    >>> [3, "y"]], columns = ['a', 'b'])
    >>> missing_imputedz(df)
        n_missing	percent
    a	1	        25%
    b	1	        25%
    """
    pass
