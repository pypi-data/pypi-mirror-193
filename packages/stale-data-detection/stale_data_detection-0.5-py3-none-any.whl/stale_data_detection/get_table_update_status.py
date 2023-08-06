"""
    Python utility function to detect column with last updated date values from 
    Hive tables 
"""

import pandas as pd
import numpy as np
from datetime import datetime

def get_table_update_status(df):
    """
    Args:
        df (pd.DataFrame)

    Returns:
        update_status: dictionary that contains column names as keys 
                        and latest update dates as values
    """
    update_status = {}
    update_columns = get_datetime_fields(df)

    for col in update_columns:
        # remove DOB column
        if is_dob_col(df, col):
            continue

        lastest_date = df[col].max().strftime('%Y-%m-%d %H:%M:%S')
        # ignore columns that contain future date
        if datetime.now() > lastest_date:
            update_status[col] = df[col].max().strftime('%Y-%m-%d %H:%M:%S')

    return update_status

def get_datetime_fields(df):
    """
    Args:
        df (pd.DataFrame)

    Returns:
        relevant_cols: list of columns that likely contain update date info
    """
    # see if column is convertible to datetime format
    relevant_cols = []
    for col in df.columns:
        if df[col].dtype == 'object' and not (df[col] == '').all():
            try:
                df[col] = pd.to_datetime(df[col])
            except (ValueError, OverflowError):
                pass
    
    # add column that contains datetime or date values
    for col in df.select_dtypes(include=[np.datetime64]):
        if not (df[col].isna().all()):
            dt = df[col]
            # ignore columns that contain timestamp only
            if not (dt.dt.date == pd.Timestamp('now').date()).all():
                relevant_cols.append(col)
    return relevant_cols


def is_dob_col(df, col):
    """
    Summary: Check whether a column in a DataFrame is date of birth column or not
    Args:
        df (pd.DataFrame): Pandas DataFrame
        col (str): column name

    Return: True if it is a dob column, False otherwise
    """

    # find the range of the values
    min_date = df[col].min()
    max_date = df[col].max()

    # check if column contains dates outside of this range
    # if it is, it's unlikely to be a dob column
    if min_date.year < 1930 or max_date.year > pd.Timestamp.today().year:
        return False

    # check the distribution of values
    # DOB are likely to be uniformly distributed accross months and days of the year
    # but not accross year. If the column has that characteristic, it's more likely
    # to be a DOB column
    by_month_day = df[col].dt.strftime("%m-%d").value_counts(normalize=True)
    by_year = df[col].dt.year.value_counts(normalize=True)

    # check if avg % of dates that occur each month-day combination > 0.05
    # or avg % of dates that occur each year is < 10% -> not likely a DOB column
    # mean frequency for month-day is supposed to be low for DOB
    # and higher for year
    if by_month_day.mean() > 0.05 or by_year.mean() < 0.1:
        return False

    
