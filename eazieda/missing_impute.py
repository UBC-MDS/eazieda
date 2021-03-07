import pandas as pd
import numpy as np

def missing_impute(data, method_num="mean", method_non_num="most_frequent"):

    """
    Return the imputed version of data based on the methods selected

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        A Pandas Dataframe for which the missing values need to be detected

    method_num : str, default = "mean"
        The method used for imputing numerical missing values
        One of 'drop', mean', 'median'

    method_non_num: str, default = "most_frequent"
        The method used for imputing non-numerical missing values 
        One of 'drop', 'most_frequent'

    Returns
    -------
    pandas.core.frame.DataFrame
        A imputed dataframe

    Examples
    --------
    >>> from eazieda.missing_impute import missing_impute
    >>> df = pd.DataFrame([[1, "x"], [np.nan, "y"], [2, np.nan], [3, "y"]], columns = ['a', 'b'])
    >>> missing_impute(df)
        a	b
    0	1	x
    1	2   y
    2   2   y
    3   3	y
    """
    
    # Tests whether input data is of pd.DataFrame type
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Please pass in a Pandas DataFrame for `data`")
        
    # Tests whether input method_num is one of the option
    if not method_num in ['drop', 'mean', 'median']:
        raise ValueError("Please enter one the following option: 'drop', 'mean', 'median'")
        
    # Tests whether input method_non_num is one of the option
    if not method_non_num in ['drop', 'most_frequent']:
        raise ValueError("Please enter one the the option: 'drop', 'most_frequent'")
    
    # filter out the numerical columns and non-numerical columns
    num_columns = data.select_dtypes(include=np.number).columns.tolist()
    non_num_columns = [col for col in data.columns if col not in num_columns]
    
    imputed_df = data.copy()
    
    # impute for numerical columns:
    if method_num == "drop":
        imputed_df = imputed_df.dropna(axis=0, subset = num_columns)
    else: 
        for num_column in num_columns:
            if method_num == "mean":
                imputed_df[num_columns] = imputed_df[num_columns].replace(np.nan, imputed_df[num_columns].mean())
            elif method_num == "median":
                imputed_df[num_columns] = imputed_df[num_columns].replace(np.nan, imputed_df[num_columns].median())
                    
    # impute for non-numrical columns:
    if method_non_num == "drop":
        imputed_df = imputed_df.dropna(axis=0, subset = non_num_columns)
    else:
        for non_num_column in non_num_columns:
            most_frequent = imputed_df[non_num_column].value_counts().sort_values(ascending=False).index[0]
            imputed_df[non_num_column] = imputed_df[non_num_column].replace(np.nan, most_frequent)

    return imputed_df.reset_index()

