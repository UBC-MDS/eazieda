import pandas as pd
import altair as alt
import numpy as np
import scipy
from vega_datasets import data

def corr_plot(
        data,
        features=None,
        method="pearson",
        plot_width=500,
        plot_height=400):
    """
    Generates a correlation plot for a list of features in a given dataframe

    Parameters
    ----------
    data: pandas.core.frame.DataFrame
        The input dataframe
    features: list, default = None
        A list of strings that represents feature names
        len(features) >=2 
        None returns plot of all numeric features
    
    method: str, default = "pearson"
        The correlation method
        Other correlation methods are "spearman" or "kendall"

    plot_width: int, default = 500
        The width of the plot

    plot_height: int, default = 400
        The height of the plot

    Returns
    -------
    `altair plot`
        An interactive altair correlation plot

    Examples
    --------
    >>> from eazieda.corr_plot import corr_plot
    >>> from vega_datasets import data
    >>> df = data.iris()
    >>> corr_plot(df, ["petal_length", "petal_width", "sepal_length"], "pearson")
    """
    # Defining numeric_features list
    numeric_features = ["int16", "int32", "int64", "float16", "float32", "float64"]

    # Cheking user's inputs
    
    # Tests whether input data is of pd.DataFrame type
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Please pass in a Pandas DataFrame for `data`")
    
    # Tests whether input features is of the type list
    if features!=None:
        if not isinstance(features, list):
            raise TypeError("Please pass in a list for `features`")
            
    # Tests whether input features has at least two features
    if features!=None:   
        if len(features) < 2 :
            raise ValueError("At least two features should be selected")
    
    # Tests whether input method is of the type str
    if not isinstance(method, str):
        raise TypeError("Please pass in a str for `method`")
        
    # Tests whether input method is one of the 3 available options      
    if method not in ("pearson", "spearman", "kendall"):
        raise Exception(
            "Please pick a correlation method: 'pearson', 'spearman' or 'kendall'"
        )
        
    # Tests whether input plot width and height are of the type int   
    if (not isinstance(plot_width, int)) or (not isinstance(plot_height, int)):
        raise TypeError("Both plot_width and plot_height must be integers")
        
    # Subsetting the data dataframe
    if features == None:
        if data.select_dtypes(include=numeric_features).shape[1] < 2:
            raise ValueError("Dataftame should have at least two numerical features")
        data = data.select_dtypes(include=numeric_features)
    else:
        if data[features].select_dtypes(np.number).shape[1] < 2:
            raise ValueError("Dataftame should have at least two numerical features")
        data = data[features].select_dtypes(include=np.number)
        
    # Creating corr_df dataframe    
    corr_df = data.corr(method).stack().reset_index(name='corr')
    corr_df.loc[corr_df['corr'] == 1, 'corr'] = 0
    corr_df['abs'] = corr_df['corr'].abs()
    
    # Correlation plot 
    corr_plot = alt.Chart(corr_df, title=f"{method} Correlations Plot for Numerical Features").mark_circle().encode(
    x= alt.X('level_0', title='Numerical Features'),
    y = alt.Y('level_1', title='Numerical Features'),
    size=alt.Size('abs', title='Correlation Size'),
    color=alt.Color('corr', title='Correlation', scale=alt.Scale(scheme='blueorange')),
    tooltip=alt.Tooltip('corr')).properties(width=plot_width, height=plot_height)
    
    return corr_plot 
