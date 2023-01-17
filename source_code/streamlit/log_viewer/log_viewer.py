#!/usr/bin/env python

import argparse
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def read_data(file_name):
    '''read data from the given file name, and return a dataframe

    Parameters
    ----------
    file_name: str
        file name of the CSV file that contains the log data

    Returns
    -------
    pandas.Dataframe
        dataframe that represents the data
    '''
    df = pd.read_csv(file_name, parse_dates=['start_time'])
    return df

if __name__ == '__main__':
    # parse command line arguments
    arg_parser = argparse.ArgumentParser(description='Log viewer')
    arg_parser.add_argument('log_file', help='log file to view')
    options = arg_parser.parse_args()

    # read the data
    log_df = read_data(options.log_file)

    # configure page options
    st.set_page_config(
        page_title='Log viewer',
        page_icon=':bar_chart:',
        layout='wide'
    )

    # create sidebar
    st.sidebar.header = 'Filters'

    # add control to select users, default to empty list, which
    # means all users
    users = st.sidebar.multiselect(
        'select the user(s)',
        options=sorted(log_df.user.unique()),
        default=[],
    )

    # filter dataframe based on the selected users
    selection_df = log_df.copy()
    if users:
        selection_df = selection_df.query('user== @users')

    # use column layout for start and end date/time widgets
    date_col, time_col = st.sidebar.columns(2)
    with date_col:
        start_date = st.date_input(
            ' time window start',
            value=selection_df.start_time.min(),
            min_value=selection_df.start_time.min(),
            max_value=selection_df.start_time.max()
        )
        end_date = st.date_input(
            ' time window end',
            value=selection_df.start_time.max(),
            min_value=selection_df.start_time.min(),
            max_value=selection_df.start_time.max()
        )
    with time_col:
        start_time = st.time_input(
            '',
            value=datetime.time(0, 0, 0)
        )
        end_time = st.time_input(
            '',
            value=datetime.time(23, 59, 59)
        )

    # add checkbox to toggle displaying plots
    show_plots = st.sidebar.checkbox('show plots', value=True)

    # filter dataframe based on the date range
    begin = f'{start_date.strftime("%Y-%m-%d")} {start_time.strftime("%H:%M:%S")}'
    end = f'{end_date.strftime("%Y-%m-%d")} {end_time.strftime("%H:%M:%S")}'
    selection_df = selection_df.query(f'"{begin}" <= start_time <= "{end}"')
    
    # if plots should be shown, do so
    if show_plots:
        # define columns in main page for plots
        left_col, right_col = st.columns(2)

        # bar plot that displays the number of jobs per day
        with left_col:
            st.markdown('**nr. of jobs per day**')
            figure, axes = plt.subplots()
            df = selection_df[['start_time']].groupby(selection_df.start_time.dt.date).count()
            axes.bar(df.index, df.start_time)
            axes.set_xticklabels(axes.get_xticklabels(),
                                 rotation=45, ha='right')
            st.pyplot(figure)

        # bar plot that displays the number of jobs per user
        with right_col:
            st.markdown('**nr. of jobs per user**')
            figure, axes = plt.subplots()
            df = selection_df[['user', 'id']].groupby('user').count()
            axes.bar(df.index, df.id)
            axes.set_xticklabels(axes.get_xticklabels(),
                                 rotation=45, ha='right')
            st.pyplot(figure)

    # display the data on main pane
    st.dataframe(selection_df)
