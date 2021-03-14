=====
Usage
=====

To generate correlation plots for your data frame, import the ``corr_plot`` function from the ``eazieda.corr_plot`` module::

    from eazieda.corr_plot import corr_plot

Then pass your data frame (``df``) and the columns you want to generate the plots for::

    corr_plot(df, ['column1','column2','column3'])

This will give you an interactive correlation plot implemented in altair
*Make sure to pass at least two columns to get the correlation!*

To generate histograms and bar plots from your data, import the ``histograms`` function from the ``eazieda.histograms`` module::

    from eazieda.histograms import histograms

Then pass your data frame (``df``) and the columns you want to generate the plots for::

    histograms(df, ['numeric_column', 'categorical_column'],num_cols=2)

This will give you a combined histogram (for numeric columns) and bar plot (for categorical columns) implemented in altair.
You can control the number of columns using ``num_cols`` and the plot dimensions with ``plot_width`` and ``plot_height``

To detect missing data in your dataframe, import the ``missing_detect`` function from the ``eazieda.missing_detect`` module::

    from eazieda.missing_detect import missing_detect

To detect the missing data, do this::

    df = pd.DataFrame([[1, "x"], [np.nan, "y"], [2, np.nan], [3, "y"]],
    columns = ['a', 'b'])
    missing_detect(df)

You will get a data frame back which has the number of missing values and their corresponding percentage

To deal with missing data in your dataframe, import the ``missing_impute`` function from the ``eazieda.missing_impute`` module::

    from eazieda.missing_impute import missing_impute

To impute the missing data, do this::

    df = pd.DataFrame([[1, "x"], [np.nan, "y"], [2, np.nan], [3, "y"]],
    columns = ['a', 'b'])
    missing_impute(df)

You will get an imputed data frame back. 
You can control the type of imputation with ``method_num`` and ``method_non_num``

To detect outliers in your data, import the ``outliers_detect`` function from the ``eazieda.outliers_detect`` module::

    from eazieda.outliers_detect import outliers_detect

To detect the outliers do this::

    s = pd.Series([1,1,1,1,1,1,1,1,1,1,1e14])
    outliers_detect(s)

You can control the method used to detect the outliers with ``method``. You can choose one of ``iforest``, ``iqr`` or ``zscore``

To remove outliers in your data, import the ``remove_outliers`` function from the ``eazieda.outliers_detect`` module::

    from eazieda.outliers_detect import remove_outliers

To remove the outliers, do this::

    s = pd.Series([1,1e14])
    outliers = np.array([False,,True])
    s_without_outliers = remove_outliers(s, outliers)

You can choose to do the removal in place with ``inplace=True``
