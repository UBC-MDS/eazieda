# eazieda 

![](https://github.com/UBC-MDS/eazieda/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/eazieda/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/eazieda) ![Release](https://img.shields.io/github/v/release/UBC-MDS/eazieda) [![Documentation Status](https://readthedocs.org/projects/eazieda/badge/?version=latest)](https://eazieda.readthedocs.io/en/latest/?badge=latest)

Almost every data analysis project involves the process of doing some exploratory data analysis(EDA) and data preprocessing. Usually they serve as a very crucial and inevitable step in a data analysis workflow. There are some very common tasks in EDA, which can include:

- checking for missing values
- detecting outliers 
- plotting correlation plots between features
- plotting histograms/bar plots for each individual features 

Typically these steps are followed by some preprocessing like imputation and dealing with outliers. All of those steps together may require lots of coding effort and can be repeated for several projects. To solve this issue, we designed the Python package `eazieda` that wraps all of those lines of code into four convenient functions that will allow you to quickly and easily carry out EDA along with some simple preprocessing using just a few lines of code!

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple eazieda
```

## Features

1.  `missing_detect`: This function will take in a dataframe and generate a table listing the number of missing values and the percentage of missing values for each column. 
2.  `missing_impute`: This function will take in a dataframe and generate a imputed dataframe based on some simple imputation method. The imputation methods can also be customized by the user.
3.  `outliers_detect` : This function will take in a pandas series and will return a boolean numpy array containing all the indices of outliers as `True`, given by certain method that the users can customize.
4.  `corr_plot`: This function will take in a dataframe and a list of feature names to generate a correlation plot for the given list of features.
5.  `remove_outliers`: This function will take in a pandas series and an boolean numpy array with the outliers marked as `True` and removes them. It returns the series without the outliers. This can be done in place in which case it will return None.
6.  `histograms`: This function will take in a dataframe and a list of feature names to generates histograms for numeric features and bar plots for categorical features

## Dependencies

We use the common Python stack:

-   [python](https://www.python.org/)
-   [pandas](https://pandas.pydata.org/)
-   [numpy](https://numpy.org/)
-   [altair](https://altair-viz.github.io/)
-   [vega-datasets](https://github.com/vega/vega-datasets)
-   [scipy](https://www.scipy.org/)
-   [scikit-learn](https://scikit-learn.org/stable/)

For versioning and managing our package - we use [`poetry`](https://python-poetry.org/). More information on determining dependency versions can be found [here](https://python-poetry.org/docs/basic-usage/#installing-dependencies)

## Usage

For ideas on how to use `eazieda` in a project please see our [Usage](https://eazieda.readthedocs.io/en/latest/usage.html) section on ReadTheDocs.

## Documentation

The official documentation is hosted on Read the Docs: https://eazieda.readthedocs.io/en/latest/

## Similar Work

We recognize EDA (exploratory data analysis) and preprocessing packages are common in the Python open source ecosystem. Our package aims to do a few things very well, and be light weight. A non exhaustive list of EDA helper packages in Python include:

- [`pandasprofiling`](https://github.com/pandas-profiling/pandas-profiling)
    - One of the most function packed packages for automatic EDA. Produces a large HTML report accounting for statistics column by column, missing values, correlation checks, histograms etc. 
- [`sweetviz`](https://github.com/fbdesignpro/sweetviz)
    - This package produces very clean visuals detailing breakdowns in descriptive statistics and can do so with train/test sets for model building workflows.
- [`ExploriPy`](https://github.com/exploripy/exploripy)
    - This packages does the most common EDA tasks but also adds in the ability to do statistical testing using analysis of variance (ANOVA), Chi Square test of independence etc.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/eazieda/graphs/contributors).

|  	 Core contributor| Github.com username| 
|---------|---|
|  Vignesh Lakshmi Rajakumar |  @vigneshrajakumar| 
|   Dustin Andrews|  @dbandrews| 
|  Arash Shamseddini | @arashshams| 
|  Yuyan Guo | @yuyanguo| 

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
