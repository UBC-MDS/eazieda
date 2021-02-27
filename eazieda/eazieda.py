import pandas as pd


def outliers(s, method = "zscore", remove = False):
    """
    Detects outliers in a pandas series

    Parameters
    ----------
    s : pandas.Series
        Pandas Series that has the data for which the outliers need to be found
    method : str
        The algorithm/method used for outlier detection. One of 'zscore',  'iforest', 'dbscan', 'iqr'
    remove : bool
        in-place removal of the outliers

    Returns
    -------
    pandas.Series
        series of outliers

    Examples
    --------
    >>> from eazieda import eazieda
    >>> s = pd.Series([1,2,3,4,5,6,100, 101])
    >>> eazieda.outliers(s)
    0    100
    1    101
    dtype: int64
    """
    pass