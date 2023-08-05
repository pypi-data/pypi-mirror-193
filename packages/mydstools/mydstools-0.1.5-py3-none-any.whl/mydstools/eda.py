# This module is part of mydstools.
# Please refer to https://github.com/antobzzll/dstoolbox

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def distribution_analysis(series: pd.Series, 
                          label: str = None, 
                          binwidth: int = None):
    """
    Function that combines `distribution_stats()` and `distribution_plots()`.

    Args:
        series (pd.Series): Input pandas.Series
        label (str, optional): Label that describes the series. Defaults to None.
        binwidth (int, optional): Width of the histogram bins. Defaults to None.
    """
    if not label:
        label = series.name
    distribution_plots(series, label, binwidth)

    stats = distribution_stats(series)
    for k, v in stats.items():
        print(k, "\t", v)


def distribution_plots(series: pd.Series, label: str = None, binwidth=None):
    """
    Creates a distribution plot for a given series.
    It takes in two parameters: the series and an optional label. 
    The code then creates two subplots with a boxplot and a histogram 
    with kernel density estimation on the right. The binwidth parameter 
    can be used to adjust the bin size of the histogram.

    Args:
        series (pd.Series): Input pandas.Series
        label (str, optional): Label that describes the series. Defaults to None.
        binwidth ([type], optional): Width of the histogram bins. Defaults to None.
    """
    if not label:
        label = series.name
    # distribution plots
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(ax=ax[0], x=series)
    sns.histplot(ax=ax[1], x=series, binwidth=binwidth, kde=True)
    plt.suptitle(f"Distribution of {label}")
    plt.show()


def distribution_stats(series: pd.Series):
    """
    Returns a dictionary with the most common statistics for 
    a given distribution.

    Args:
        series (pd.Series): [description]

    Returns:
        [type]: [description]
    """
    stats = series.describe()

    iqr = stats['75%'] - stats['25%']
    stats['IQR'] = iqr
    low_threshold = stats['25%'] - (1.5 * iqr)
    if low_threshold >= stats['min']:
        stats['lo-wh'] = low_threshold
    stats['hi-wh'] = stats['75%'] + (1.5 * iqr)
    stats['skew'] = series.skew()

    return stats


def obj_vars_unique(df: pd.DataFrame, verbose=False):
    """
    Creates a dictionary or prints the dataframe's unique values for object
    variables.

    Args:
        df (pd.DataFrame): input DataFrame
        verbose (bool, optional): If True, prints unique values. Defaults to False.

    Returns:
        dict: dictionnary of column names and unique values.
    """
    cat_vars = [var for var in df.columns if df[var].dtype in ['object']]
    cat_vars_unique = {}

    for v in cat_vars:
        uniques = df[v].unique()
        cat_vars_unique[v] = uniques
        if verbose:
            print(f"{v}: {uniques}")

    if not verbose:
        return cat_vars_unique


def plot_corr(df: pd.DataFrame, var: str = None):
    """
    The function calculates the correlation between the variables in the 
    DataFrame and creates a heatmap to visualize it. If the string variable 
    is specified, it will create a heatmap that shows the features correlating 
    with that variable. Otherwise, it will create a heatmap of all variables 
    in the DataFrame.

    Args:
        df (pd.DataFrame): input dataframe
        var (str, optional): name of the variable to focus on. Defaults to None.
    """
    corr = df.corr()
    if var:
        heatmap = sns.heatmap(corr[[var]].sort_values(by=var, ascending=False)[1:],
                              vmin=-1, vmax=1, annot=True, cmap='BrBG')
        heatmap.set_title(f'Features correlating with `{var}`')
    else:
        sns.heatmap(corr, vmin=-1, vmax=1,
                    # mask=mask,
                    annot=True, cmap='BrBG')
    plt.show()


def perc_missing_values(df: pd.DataFrame):
    """
    The function calculates the percentage of missing values in the DataFrame 
    and returns a list of the columns with non-zero missing values, 
    sorted in descending order.

    Args:
        df (pd.DataFrame): input dataframe

    Returns:
        list: list of the columns with non-zero missing values
    """
    missing = df.isnull().sum().sort_values(ascending=False)/df.shape[0]
    return missing[missing != 0]


def check_column(column: pd.Series):
    """
    This code takes in a pandas series as an argument and prints out 
    information about the column. It prints out the data type, the number 
    of null values and non-null values, and if the data type is int or float 
    it will print out summary statistics. If the data type is not int or 
    float it will print out the number of unique values and list them.

    Args:
        column (pd.Series): input series
    """
    n_unique = len(column.unique())
    nulls = column.isnull().sum()
    non_nulls = column.shape[0] - nulls
    print(f'Dtype: {column.dtype}')
    print(f'NULL values: {nulls} ({nulls/column.shape[0]})')
    print(f'NON-NULL values: {non_nulls} ({non_nulls/column.shape[0]})')

    if column.dtype in (int, float):
        print(column.describe())
    else:
        print(f'Unique values: {n_unique} ({n_unique/non_nulls})')
        print(column.unique())


def cond_prob(df_data: pd.DataFrame, outcome: tuple, events: dict = {}) -> float:
    """
    Calculates the conditional probability of the outcome given the events in the DataFrame.
    
    Parameters:
    df_data (pd.DataFrame): The DataFrame containing the data.
    outcome (tuple): The outcome of interest represented as a tuple of column name and value, e.g., ("exam", 1).
    events (dict): The events of interest represented as a dictionary of column names and values, e.g., {"study": 1}.
    
    Returns:
    float: The conditional probability of the outcome given the events.
    """
    
    # Filter the DataFrame based on the events
    for feature, value in events.items():
        df_data = df_data[df_data[feature] == value]

    # Calculate the conditional probability of the outcome given the events
    prob = df_data[df_data[outcome[0]] == outcome[1]].shape[0] / df_data.shape[0]

    return prob

def tukeyhsd(df: pd.DataFrame, cat_var: str, target_var: str):
    """
    tukeyhsd() is a function that performs Tukey's Honest Significant Difference (HSD) test on a given dataframe. 
    It takes two arguments: df (a pandas DataFrame) and cat_var and target_var (strings representing the categorical variable and the target variable respectively). 
    The function groups the dataframe by the categorical variable, then performs the Tukey HSD test on each group of the target variable. 
    The results of the test are printed. 

    Args:
        df (pd.DataFrame): [description]
        cat_var (str): [description]
        target_var (str): [description]
    """
    series = []
    labels = []

    for n, s in df.groupby(cat_var)[target_var]:
        series.extend(s)
        labels += [n] * len(s)
    series = np.array(series)

    tukey_results = pairwise_tukeyhsd(series, labels)
    print(tukey_results)