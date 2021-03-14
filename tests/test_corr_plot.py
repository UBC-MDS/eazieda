from eazieda import corr_plot
import pandas as pd
import numpy as np
from pytest import raises, fixture


@fixture
def input_data():
    # Creating test inputs for the test function
    input_data = pd.DataFrame(
        {
            "Title": ["Finding Nemo", "Dunkirk", "Denial"],
            "vote_average": [3.86, 4.11, 3.62],
            "vote_count": [33887, 282, 68],
            "vote_std": [0.87, 0.78, 0.82],
        }
    )
    return input_data


@fixture
def plot_test(input_data):
    plot_test = corr_plot.corr_plot(input_data, features=None)
    return plot_test


def test_corr_plot(input_data, plot_test):

    """
    Test function to check the output of corr_plot function.
    """

    array_test = np.array([1, 2, 3, 4, 5])

    features_test1 = ["vote_average", "vote_count", "vote_std"]

    features_test4 = "vote_average"

    features_test5 = ["vote_average"]

    # Tests whether output is of Altair object
    assert "altair" in str(type(plot_test)), "Output is not an Altair object"

    assert "altair" in str(
        type(
            corr_plot.corr_plot(
                input_data.loc[:, ["vote_count", "vote_std", "Title"]],
                features=["vote_count", "vote_std", "Title"],
            )
        )
    )

    # Tests whether plot mark is circle
    assert (
        plot_test.to_dict()["mark"] == "circle"
    ), "Mark should be of type 'circle'."

    # Tests whether plot title starts with selected method
    assert plot_test.to_dict()["title"][0] in (
        "p",
        "s",
        "k",
    ), "The plot title is not as expected."

    # Tests whether a not dataframe input raises TypeError
    with raises(TypeError):
        corr_plot.corr_plot(array_test, features_test1)

    # Tests whether a not list features raises TypeError
    with raises(TypeError):
        corr_plot.corr_plot(input_data, features_test4)

    # Tests whether a list of a single feature raises ValueError
    with raises(ValueError):
        corr_plot.corr_plot(input_data, features_test5)

    # Tests whether a not str method raises TypeError
    with raises(TypeError):
        corr_plot.corr_plot(input_data, method=5)

    # Tests whether a not int plot_width and plot_height raises TypeError
    with raises(TypeError):
        corr_plot.corr_plot(
            input_data, plot_width="width", plot_height="height"
        )

    # Tests whether a method not from available options raises Exception
    with raises(Exception):
        corr_plot.corr_plot(input_data, method="laplace")


def test_corr_plot_subsetting_errors(input_data):
    with raises(ValueError):
        corr_plot.corr_plot(input_data.loc[:, ["vote_count"]])

    with raises(ValueError):
        corr_plot.corr_plot(
            input_data.loc[:, ["vote_count", "Title"]],
            features=["vote_count", "Title"],
        )

    with raises(ValueError):
        corr_plot.corr_plot(
            input_data.loc[:, ["vote_count", "Title"]],
            features=["vote_count", "Title"],
        )
