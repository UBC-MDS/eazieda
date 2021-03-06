from eazieda.missing_impute import missing_impute
import pandas as pd
import numpy as np
from pytest import raises, fixture


@fixture
def df_miss():
    df = pd.DataFrame(
        [[1.0, "x"], [np.nan, "y"], [2.0, np.nan], [3.0, "y"]],
        columns=["a", "b"],
    )
    return df


@fixture
def df_miss_2():
    df = pd.DataFrame(
        [[1.0, "x"], [np.nan, "y"], [2.0, np.nan], [3.0, "y"], [4.0, "y"]],
        columns=["a", "b"],
    )
    return df


def test_missing_impute(df_miss, df_miss_2):

    # Test with default arguments
    expected_output_default = pd.DataFrame(
        data={"a": [1.0, 2.0, 2.0, 3.0], "b": ["x", "y", "y", "y"]}
    ).reset_index(drop=True)

    missing_output_default = missing_impute(df_miss)

    assert pd.DataFrame.equals(missing_output_default, expected_output_default)

    # Test with two drop arguments selected at the same time
    expected_output_two_drop = pd.DataFrame(
        data={"a": [1.0, 3.0], "b": ["x", "y"]}
    ).reset_index(drop=True)

    missing_output_two_drop = missing_impute(
        df_miss, method_num="drop", method_non_num="drop"
    )

    assert pd.DataFrame.equals(
        missing_output_two_drop, expected_output_two_drop
    )

    # Test with method_num="mean", method_non_num="drop"
    expected_output_one_drop = pd.DataFrame(
        data={"a": [1.0, 2.0, 3.0], "b": ["x", "y", "y"]}
    ).reset_index(drop=True)

    missing_output_one_drop = missing_impute(df_miss, method_non_num="drop")

    assert pd.DataFrame.equals(
        expected_output_one_drop, missing_output_one_drop
    )

    # Test with method_num="median", method_non_num="most_frequent"
    expected_output_median = pd.DataFrame(
        data={"a": [1.0, 2.0, 2.0, 3.0], "b": ["x", "y", "y", "y"]}
    ).reset_index(drop=True)
    missing_output_median = missing_impute(df_miss, method_num="median")

    assert pd.DataFrame.equals(missing_output_median, expected_output_median)

    # Test with method_num="median", method_non_num="drop"
    expected_output_median_drop = pd.DataFrame(
        data={"a": [1.0, 2.0, 3.0], "b": ["x", "y", "y"]}
    ).reset_index(drop=True)
    missing_output_median_drop = missing_impute(
        df_miss, method_num="median", method_non_num="drop"
    )

    assert pd.DataFrame.equals(
        missing_output_median_drop, expected_output_median_drop
    )

    # Test with method_num="drop", method_non_num="most_frequent"
    expected_output_drop_freq = pd.DataFrame(
        [[1.0, "x"], [2.0, "y"], [3.0, "y"], [4.0, "y"]], columns=["a", "b"],
    ).reset_index(drop=True)
    missing_output_drop_freq = missing_impute(
        df_miss_2, method_num="drop", method_non_num="most_frequent"
    )

    assert pd.DataFrame.equals(
        missing_output_drop_freq, expected_output_drop_freq
    )

    # Test whether a not dataframe input raises TypeError
    with raises(TypeError):
        missing_impute(5)

    # Test whether invaild input of method_num raises ValueError
    with raises(ValueError):
        missing_impute(df_miss, method_num="mea")

    # Test whether invaild input of method_non_num raises ValueError
    with raises(ValueError):
        missing_impute(df_miss, method_num="mean", method_non_num="most_freq")
