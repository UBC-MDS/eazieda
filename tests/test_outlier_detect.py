import pandas as pd
import numpy as np
import pytest

from eazieda.outliers_detect import outliers_detect
from eazieda.outliers_detect import outliers_detect_zscore
from eazieda.outliers_detect import outliers_detect_iforest
from eazieda.outliers_detect import outliers_detect_iqr
from eazieda.outliers_detect import remove_outliers

@pytest.fixture
def hi_zscore_series():
    l = [1] * 10
    l.append(1e14)
    return pd.Series(l)

@pytest.fixture
def simple_series():
    return pd.Series([1,2,1,2,1, 1000])

@pytest.fixture
def simple_series_and_array():
    return (pd.Series([1,2,1,2,1, 1000]), np.array([False, False, False, False, False,  True]))

def test_outliers_detect_zscore(hi_zscore_series):
    """
    Normal case, zscore
    """
    s = hi_zscore_series

    outliers = outliers_detect_zscore(s)

    expected_output = np.array([False, False, False, False, False, False, False, False, False, False, True])

    assert np.array_equal(expected_output, outliers)

def test_outliers_detect_iqr(simple_series):
    """
    Normal case, iqr
    """
    s = simple_series

    outliers = outliers_detect_iqr(s)

    expected_output = np.array([False, False, False, False, False,  True])

    assert np.array_equal(expected_output, outliers)

def test_outliers_detect_iforest(simple_series):
    """
    Normal case, iforest
    """
    s = simple_series

    outliers = outliers_detect_iforest(s)

    expected_output = np.array([False, False, False, False, False,  True])

    assert np.array_equal(expected_output, outliers)

def test_remove_outliers_inplace(simple_series_and_array):
    """
    remove outliers in place. Should modify the original series
    """
    s, outliers = simple_series_and_array
    remove_outliers(s, outliers, inplace=True)

    expected_output = pd.Series([1,2,1,2,1])

    assert expected_output.equals(s)

def test_remove_outlier_not_inplace(simple_series_and_array):
    """
    remove outliers in place. Should not modify the original series
    """
    s, outliers = simple_series_and_array
    output = remove_outliers(s, outliers, inplace=False)

    expected_output = pd.Series([1,2,1,2,1])
    assert expected_output.equals(output)

def test_detect_outliers_integration_zscore_false(hi_zscore_series):
    """
    Integration test for zscore
    """
    s = hi_zscore_series.copy()
    outliers = outliers_detect(s, method="zscore")
    expected_output = np.array([False, False, False, False, False, False, False, False, False, False, True])
    expected_s = hi_zscore_series

    assert np.array_equal(expected_output, outliers)

def test_detect_outliers_integration_iqr_false(simple_series):
    """
    Integration test for iqr
    """
    s = simple_series.copy()
    outliers = outliers_detect(s, method="iqr")
    expected_output = np.array([False, False, False, False, False,  True])
    expected_s = simple_series

    assert np.array_equal(expected_output, outliers)
    # make sure nothing was removed
    assert expected_s.equals(s)

def test_detect_outliers_integration_iforest_false(simple_series):
    """
    Integration test for iforest
    """
    s = simple_series.copy()
    outliers = outliers_detect(s, method="iforest")
    expected_output = np.array([False, False, False, False, False,  True])
    expected_s = simple_series

    assert np.array_equal(expected_output, outliers)
    # make sure nothing was removed
    assert expected_s.equals(s)

def test_incorrect_input_detect():
    """
    Error handling for non-series input
    """
    with pytest.raises(TypeError):
        outliers_detect(12)

def test_incorrect_method_detect(simple_series):
    """
    Error handling for wrong method input
    """
    with pytest.raises(ValueError):
        outliers_detect(simple_series, method='test')

def test_incorrecttype_remove():
    """
    Error handling for non-series input
    """
    with pytest.raises(TypeError):
        remove_outliers(12, np.array([True]))

def test_incorrect_outliers_type_remove(simple_series):
    """
    Error handling for non-series input
    """
    with pytest.raises(TypeError):
        remove_outliers(simple_series, "test")
