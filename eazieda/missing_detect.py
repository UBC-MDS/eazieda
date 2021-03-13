import pandas as pd


def missing_detect(data):
    """
    Return the number/percentage of missing values for each column
    in the dataframe

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        A Pandas Dataframe for which the missing values need to be detected

    Returns
    -------
    pandas.core.frame.DataFrame
        A dataframe containing two columns: the number of missing values and
        the percentage of missing values for each column

    Examples
    --------
    >>> from eazieda.missing_detect import missing_detect
    >>> df = pd.DataFrame([[1, "x"], [np.nan, "y"], [2, np.nan], [3, "y"]],
    >>> columns = ['a', 'b'])
    >>> missing_detect(df)
        n_missing	percent
    a	1	        25%
    b	1	        25%
    """
    # Tests whether input data is of pd.DataFrame type
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Please pass in a Pandas DataFrame for `data`")

    missing_count = pd.DataFrame(data.isnull().sum(), columns=["n_missing"])
    missing_count["percent"] = missing_count["n_missing"] / data.shape[0]

    return missing_count
