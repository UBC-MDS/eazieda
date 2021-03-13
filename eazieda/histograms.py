import pandas as pd
import altair as alt
import numpy as np


def histograms(data, features, plot_width=100, plot_height=100, num_cols=2):
    """
    Generates histograms for numeric features and
    bar plots for categorical features

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        A Pandas Dataframe

    features : list
        A list of strings that represents feature names

    plot_width: int
        The width of each features sub plot. Default = 100

    plot_height: int
        The height of each features sub plot. Default = 100

    num_cols : int
        The number of columns in the final grid of plots. Default = 2

    Returns
    -------
    `altair plot`
        A combined altair correlation plot

    Examples
    --------
    >>> from eazieda.histograms import histograms
    >>> from vega_datasets import data
    >>> df = data.iris()
    >>> histograms(df, ['petalLength', 'petalWidth', 'sepalLength'],
    >>> num_cols=2)
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Please pass in a Pandas DataFrame for `data`")
    elif len(set(features).intersection(set(data.columns))) != len(features):
        raise ValueError("All features must be present in dataframe")
    elif (not isinstance(plot_width, int)) or (
        not isinstance(plot_height, int)
    ):
        raise ValueError("plot_width and plot_height must be integer")

    # Use data types to determine which columns to plot on which chart
    numeric_cols = set(
        data.select_dtypes(include=np.number).columns
    ).intersection(features)
    cat_cols = set(
        data.select_dtypes(include=["category", "object"]).columns
    ).intersection(features)

    numeric_chart = (
        alt.Chart(data)
        .transform_fold(list(numeric_cols), as_=["Numeric Features", "value"])
        .mark_bar()
        .encode(alt.X("value:Q", title="value", bin=True), y="count()")
        .properties(width=plot_width, height=plot_height)
        .facet(facet="Numeric Features:N", columns=num_cols)
        .resolve_scale(x="independent")
    )

    # data.sample done here due to Altair referencing same data frame
    # otherwise and causing errors
    # in concatenation later
    categorical_chart = (
        alt.Chart(data.sample(data.shape[0], random_state=42))
        .transform_fold(list(cat_cols), as_=["Categorical Features", "value"])
        .mark_bar()
        .encode(alt.X("value:N"), y="count()")
        .properties(width=plot_width, height=plot_height)
        .facet(facet="Categorical Features:N", columns=num_cols)
    )

    final_chart = numeric_chart & categorical_chart
    final_chart.title = "Histograms for Numeric and Categorical Features"

    return final_chart
