"""
    Function to flag tables for PanelRx that are considered stale
"""
import getpass
import sys
sys.path.insert(0, f'/users/{getpass.getuser()}/boa')
import boa
from boa.utils import query_db
from datetime import datetime
import pandas as pd
import numpy as np
from get_table_update_status import get_table_update_status

CHECK_FIELD = 'transient_lastDdlTime'
CHECK_COLUMN = 'prpt_name'
CHECK_PERIOD = 14

def is_stale_table(table_name: str, check_period=CHECK_PERIOD):
    """
    Summary: determine whether the table is stale

    Args:
        table_name (str): table name in string format
        check_period (int): number of days out-of-date to flag a table as stale. Default 14 days
    Returns:
        Table staleness status with reason
    """
    # get table metadata lastest update date
    table_status = get_table_last_modified_date(table_name)
    
    if not table_status:
        return {'stale': 'table not found/not have access'}

    # get column lastest update date
    columns_status = get_columns_update_date(table_name)
    if len(columns_status)>0:
        last_updated_col = max(columns_status, key=columns_status.get)
        col_last_date = datetime.strptime(columns_status[last_updated_col], '%Y-%m-%d %H:%M:%S')
    else:
        col_last_date = table_status   
        last_updated_col = '' 

    # run staleness check 
    return staleness_check(table_status, col_last_date, last_updated_col, check_period)


def staleness_check(table_status, col_last_date, col_name, check_period):
    """
    Summary: Rule based checking whether a table is stale
    Args:
        table_status (datetime): table metadata last update date
        col_last_date (datetime): column most recent update date
        col_name (str): name of column that contain that most recent update date
        check_period (int): number of days out-of-date to flag a table as stale

    Returns:
        staleness status of table with the reason.
    """
    # define rule for staleness check
    datediff =  col_last_date - table_status
    # compare between column last update date and current date
    # if column has not been update for too long (check_period), flag table as stale
    if datediff.days >= 0 and col_name !='':
        datediff_now = (datetime.now()-col_last_date).days
        if datediff_now > check_period:
            return {'stale':f'column {col_name} has not been update for {datediff_now} days since {col_last_date}'}
        else:
            return {'not stale':f'column {col_name} last update was on {col_last_date}'}
    else:
        # check if metadata is updated but table content is not updated
        # flag table as stale if that happened 
        if datediff.days < -check_period:
            diff = abs(datediff.days)
            return {'stale':f'table column {col_name} has not been updated for {diff} days compared to metadata'} 
        else:
            # compare between metadata last update date and current date
            # if metadata has not been update for too long (check_period), flag table as stale
            datediff_now = (datetime.now()-table_status).days 
            if datediff_now > check_period:
                return {'stale':f'table metadata has not been update for {datediff_now} days since {table_status}'}
            else: 
                return {'not stale':f'table metadata last update on {table_status}'}


def flag_tables(table_list):
    """
    Summary: determine stale tables from list of table name

    Args:
        table_list (List[str]): list of table name

    Returns:
        list of tables that failed any of the rules
    """
    stale_list = {}
    # loop through tables list and check for staleness
    for table_name in table_list:
        table_status = is_stale_table(table_name)
        if 'stale' in table_status:
            stale_list[table_name] = table_status['stale']
    return stale_list

def get_columns_update_date(table_name: str):
    """
    Summary: get columns latest update dates from table name

    Args:
        table_name (str): table name

    Returns:
        dictionary that contains column names as keys 
        and latest update dates as values
    """
    # get columns update date
    try:
        df = get_table_dataframe(table_name)
        return get_table_update_status(df)
    except Exception as e:
        return []
    


def get_table_last_modified_date(table_name: str, check_field = CHECK_FIELD, check_column = CHECK_COLUMN):
    """
    Summary: get table metadata and return latest modified date

    Args:
        table_name (str): table name

    Returns:
        last_modified_date (datetime): table last modified date 
    """

    # query to get table metadata last update date
    sql_query = f"""
    SHOW TBLPROPERTIES {table_name} ('{check_field}')
    """
    try:
        # get the table metadata and extract last updated date
        df = query_db(sql_query, db='hive', use_arrow=False, return_df=True)
        last_modified_date = datetime.fromtimestamp(int(df[check_column][0]))
        return last_modified_date
    except Exception as e:
        print("Table not found")
        return None


def get_table_dataframe(table_name: str):
    """
    Summary: connect to db and get table content given table name

    Args:
        table_name (str): table name

    Returns:
        df (pd.DataFrame): table content as DataFrame
    """
    # construct query to read table content to dataframe
    sql_query = f'''
    SELECT * FROM {table_name}
    ORDER BY RAND()
    LIMIT 10000
    ''' 

    try:
        # use boa to read table into pd.DataFrame
        df = query_db(sql_query, db='hive', use_arrow=False, return_df=True)
        return df
    except Exception as e:
        print("Table not found")
        return None

