import numpy as np

from scipy import stats
from sklearn.ensemble import IsolationForest


def outliers_detect(s, method="zscore", remove=False):
    """
    Detects outliers in a pandas series

    Parameters
    ----------
    s : pandas.core.series.Series
        Pandas Series for which the outliers need to be found

    method : str, default = "zscore"
        The algorithm/method used for outlier detection.
        One of 'zscore',  'iforest', 'iqr'

    remove : bool, default = False
        in-place removal of the outliers

    Returns
    -------
    numpy.array
        Boolean array with same length as the input,
        indices of outlier marked.

    Examples
    --------
    >>> from eazieda.outliers_detect import outliers_detect_zscore
    >>> s = pd.Series([1,1,1,1,1,1,1,1,1,1,1e14])
    >>> outliers_detect_zscore(s)
    array([False, False, False, False, False, False, False, False, False,
        True])
    """
    if method == "zscore":
        outliers = outliers_detect_zscore(s)
    elif method == "iqr":
        outliers = outliers_detect_iqr(s)
    elif method == "iforest":
        outliers = outliers_detect_iforest(s)

    if remove:
        remove_outliers(s, outliers)

    return outliers


def outliers_detect_iforest(s):
    """
    Detects outliers in a pandas series using isolation forests

    Parameters
    ----------
    s : pandas.core.series.Series
        Pandas Series for which the outliers need to be found

    Returns
    -------
    numpy.array
        Boolean array with same length as the input,
        indices of outlier marked.

    Examples
    --------
    >>> from eazieda.outliers_detect import outliers_detect_iqr
    >>> s = pd.Series([1,2,1,2,1, 1000])
    >>> outliers_detect_iforest(s)
    array([False, False, False, False, False,  True])
    """
    iforest = IsolationForest().fit(s.values.reshape(-1, 1))
    return iforest.predict(s.values.reshape(-1, 1)) == -1


def outliers_detect_iqr(s, factor=1.5):
    """
    Detects outliers in a pandas series using inter-quantile ranges

    Parameters
    ----------
    s : pandas.core.series.Series
        Pandas Series for which the outliers need to be found

    factor : int
        iqr factor used for outliers

    Returns
    -------
    numpy.array
        Boolean array with same length as the input,
        indices of outlier marked.

    Examples
    --------
    >>> from eazieda.outliers_detect import outliers_detect_iqr
    >>> s = pd.Series([1,2,1,2,1, 1000])
    >>> outliers_detect_zscore(s)
    array([False, False, False, False, False,  True])
    """
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    inter_quantile_range = q3 - q1
    return (
        (s < (q1 - 1.5 * inter_quantile_range)) |
        (s > (q3 + 1.5 * inter_quantile_range))
    ).values


def outliers_detect_zscore(s, threshold=3):
    """
    Detects outliers in a pandas series using zscores

    Parameters
    ----------
    s : pandas.core.series.Series
        Pandas Series for which the outliers need to be found

    threshold : int
        zscore threshold used for outliers

    Returns
    -------
    numpy.array
        Boolean array with same length as the input,
        indices of outlier marked.

    Examples
    --------
    >>> from eazieda.outliers_detect import outliers_detect_zscore
    >>> s = pd.Series([1,1,1,1,1,1,1,1,1,1,1e14])
    >>> outliers_detect_zscore(s)
    array([False, False, False, False, False, False, False, False, False,
        True])
    """
    z = np.abs(stats.zscore(s))
    return z > threshold


def remove_outliers(s, outliers):
    """
    Drops outliers from the given series

    Parameters
    ----------
    s : pandas.core.series.Series
        Pandas Series for which the outliers need to be found

    outliers : numpy.array
        boolean numpy array with the same length as s.
        Outliers should be marked with True.

    Returns
    -------
    None

    Examples
    --------
    >>> from eazieda.outliers_detect import outliers_detect_zscore
    >>> s = pd.Series([1,1e14])
    >>> outliers = np.array([False,,True])
    >>> remove_outliers(s, outliers)
    >>> s
    0    1.0
    dtype: float64
    """
    s.drop(s.index[outliers], inplace=True)
