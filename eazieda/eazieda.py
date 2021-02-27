import pandas as pd
import altair as alt
import numpy as np


def corr_plot(data, features, method="pearson", plot_width=600, plot_height=400):
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
        The corrolation method
        Other corrolation methods are "spearman" or "kendall"


    plot_width: int, default = 600
        The width of the plot


    plot_height: int, default = 400
        The heigh of the plot


    Returns
    -------
    `altair plot`
        An interactive altair correlation plot


    Examples
    --------
    >>> import pandas as pd
    >>> import altair as alt
    >>> import numpy as np
    >>> from eazieda.corr_plot import corr_plot
    >>> from vega_datasets import data
    >>> df = data.iris()
    >>> corr_plot(df, ["petal_length", "petal_width", "sepal_length"])
    """

    return corr_plot
