from eazieda.missing_detect import missing_detect
import pandas as pd
import numpy as np
from pytest import raises, fixture


@fixture
def df_missing():
    df = pd.DataFrame(
        [[1, "x"], [np.nan, "y"], [2, np.nan], [3, "y"]], columns=["a", "b"]
    )
    return df


def test_missing_detect(df_missing):

    expected_output = pd.DataFrame(
        data={"n_missing": [1, 1], "percent": [0.25, 0.25]}, index=["a", "b"]
    )

    missing_output = missing_detect(df_missing)

    assert pd.DataFrame.equals(missing_output, expected_output)

    # Tests whether an integer input raises TypeError
    with raises(TypeError):
        missing_detect(5)

    # Tests whether a string input raises TypeError
    with raises(TypeError):
        missing_detect(5)
