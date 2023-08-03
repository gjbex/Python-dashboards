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
    return pd.read_csv(file_name, parse_dates=['start_time'])

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

    # filter dataframe based on the selected users

    # use column layout for start and end date/time widgets

    # add checkbox to toggle displaying plots

    # filter dataframe based on the date range

    # if plot should be shown, do so
        # define columns in main page for plots
        
        # add a bar plot showing the number of jobs per day

        # add a bar plot showing the number of jobs per user

    # display the data on main pane
