from eazieda import __version__
from eazieda import corr_plot
from vega_datasets import data
import pandas as pd
import altair as alt
import numpy as np
import scipy
from pytest import raises, fixture


def test_version():
    assert __version__ == "0.1.0"

def test_corr_plot():

    """
    Test function to check the output of corr_plot function.
    
    """
    
    # Creating test inputs for the test function
    input_data = pd.DataFrame(
        {
            "Title": ["Finding Nemo", "Dunkirk", "Denial"],
            "vote_average": [3.86, 4.11, 3.62],
            "vote_count": [33887, 282, 68],
            "vote_std": [0.87, 0.78, 0.82],
        })
    
    
    plot_test = corr_plot.corr_plot(input_data, features=None)

    data_test = np.array([1, 2, 3, 4, 5])

    features_test1 = ["vote_average", "vote_count", "vote_std"]
    
    features_test2 = ["Title"]
    
    features_test3 = ["Title", "vote_count", "vote_std"]
    
    features_test4 = "vote_average"
    
    features_test5 = ["vote_average"]

         
     # Tests whether output is of Altair object
    assert "altair" in str(type(plot_test)), "Output is not an Altair object"
    
    # Tests whether plot mark is circle 
    assert plot_test.to_dict()["mark"] == "circle", "Mark should be of type 'circle'."
    
    # Tests whether plot title starts with selected method
    assert plot_test.to_dict()["title"][0] in ("p","s","k",), "The plot title is not as expected."
    
    
    # Tests whether a not dataframe input raises TypeError
    with raises(TypeError):
        corr_plot.corr_plot(data_test, features_test1)
        
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
        corr_plot.corr_plot(input_data, plot_width="width", plot_height="height")
        
    # Tests whether a method not from available options raises Exception
    with raises(Exception):
        corr_plot.corr_plot(input_data, method="laplace")


