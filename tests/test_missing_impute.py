from eazieda import __version__
from eazieda import missing_impute
import pandas as pd
import numpy as np
from pytest import raises, fixture


def test_version():
    assert __version__ == "0.1.0"

@fixture
def df_miss():
    df = pd.DataFrame([[1, "x"], [np.nan, "y"], [2, np.nan], [3, "y"]], columns = ['a', 'b'])
    return df

def test_missing_impute(df_miss):
    
    # Test with default arguments
    expected_output_default = pd.DataFrame(data = {'a': [1, 2, 2, 3], 'b': ['x', 'y', 'y', 'y']})
    
    missing_output_default = missing_impute(df_miss)
    
    assert pd.DataFrame.equals(missing_output_default, expected_output_default)
    
    # Test with two drop arguments selected at the same time
    expected_output_two_drop = pd.DataFrame(data = {'a': [1, 3], 'b': ['x', 'y']})
    
    missing_output_two_drop = missing_impute(df_miss, method_num="drop", method_non_num="drop")
    
    assert pd.DataFrame.equals(missing_output_two_drop, expected_output_two_drop)
    
    
    # Test with only one drop argument is selected
    expected_output_one_drop = pd.DataFrame(data = {'a': [1, 2, 3], 'b': ['x', 'y', 'y']})
    
    missing_output_one_drop = missing_impute(df_miss, method_non_num="drop")
    
    assert pd.DataFrame.equals(expected_output_one_drop, missing_output_one_drop)
    
    # Test with method_num="median" 
    expected_output_median = pd.DataFrame(data = {'a': [1, 2, 2, 3], 'b': ['x', 'y', 'y', 'y']})
    missing_output_median = missing_impute(df_miss, method_num="median")
    
    assert pd.DataFrame.equals(missing_output_median, expected_output_median)
    
    # Test whether a not dataframe input raises TypeError
    with raises(TypeError):
        missing_impute(5)
        
    # Test whether invaild input of method_num raises ValueError
    with raises(ValueError):
        missing_impute(df_miss, method_num="mea")
        
    # Test whether invaild input of method_non_num raises ValueError   
    with raises(ValueError):
        missing_impute(df_miss, method_num="mean", method_non_num="most_freq")
        

