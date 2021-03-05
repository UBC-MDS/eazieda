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
    s = hi_zscore_series

    outliers = outliers_detect_zscore(s)

    expected_output = np.array([False, False, False, False, False, False, False, False, False, False, True])

    assert np.array_equal(expected_output, outliers)

def test_outliers_detect_iqr(simple_series):
    s = simple_series

    outliers = outliers_detect_iqr(s)

    expected_output = np.array([False, False, False, False, False,  True])

    assert np.array_equal(expected_output, outliers)

def test_outliers_detect_iforest(simple_series):
    s = simple_series

    outliers = outliers_detect_iforest(s)

    expected_output = np.array([False, False, False, False, False,  True])

    assert np.array_equal(expected_output, outliers)

def test_remove_outliers(simple_series_and_array):
    s, outliers = simple_series_and_array
    remove_outliers(s, outliers)

    expected_output = pd.Series([1,2,1,2,1])

    assert expected_output.equals(s)

def test_detect_outliers_integration_zscore_false(hi_zscore_series):
    s = hi_zscore_series.copy()
    outliers = outliers_detect(s, method="zscore", remove=False)
    expected_output = np.array([False, False, False, False, False, False, False, False, False, False, True])
    expected_s = hi_zscore_series

    assert np.array_equal(expected_output, outliers)
    # make sure nothing was removed
    assert expected_s.equals(s)

def test_detect_outliers_integration_zscore_true(hi_zscore_series):
    s = hi_zscore_series.copy()
    outliers = outliers_detect(s, method="zscore", remove=True)
    expected_output = np.array([False, False, False, False, False, False, False, False, False, False, True])
    expected_s = hi_zscore_series.iloc[:-1]

    assert np.array_equal(expected_output, outliers)
    assert expected_s.equals(s)

def test_detect_outliers_integration_iqr_false(simple_series):
    s = simple_series.copy()
    outliers = outliers_detect(s, method="iqr", remove=False)
    expected_output = np.array([False, False, False, False, False,  True])
    expected_s = simple_series

    assert np.array_equal(expected_output, outliers)
    # make sure nothing was removed
    assert expected_s.equals(s)

def test_detect_outliers_integration_iqr_true(simple_series):
    s = simple_series.copy()
    outliers = outliers_detect(s, method="iqr", remove=True)
    expected_output = np.array([False, False, False, False, False,  True])
    expected_s = simple_series.iloc[:-1]

    assert np.array_equal(expected_output, outliers)
    assert expected_s.equals(s)

def test_detect_outliers_integration_iforest_false(simple_series):
    s = simple_series.copy()
    outliers = outliers_detect(s, method="iforest", remove=False)
    expected_output = np.array([False, False, False, False, False,  True])
    expected_s = simple_series

    assert np.array_equal(expected_output, outliers)
    # make sure nothing was removed
    assert expected_s.equals(s)

def test_detect_outliers_integration_iforest_true(simple_series):
    s = simple_series.copy()
    outliers = outliers_detect(s, method="iforest", remove=True)
    expected_output = np.array([False, False, False, False, False,  True])
    expected_s = simple_series.iloc[:-1]

    assert np.array_equal(expected_output, outliers)
    assert expected_s.equals(s)