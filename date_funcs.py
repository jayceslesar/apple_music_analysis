# script for testing
import datetime
import pandas as pd
import numpy as np


def extract_dates(dates_list):
    return_dates = []
    for date in dates_list:
        date = date.split('T')
        norm_date = date[0].split('-')
        time_date = date[1].split(':')
        year = int(norm_date[0])
        month = int(norm_date[1])
        day = int(norm_date[2])
        hour = int(time_date[0])
        minute = int(time_date[1])
        second = int(time_date[2][:2])
        times = datetime.datetime(year, month, day, hour, minute, second)
        return_dates.append(times)
    return return_dates


def minutes_played(start_time, end_time):
    return end_time - start_time


def total_mins(timedeltas):
    return sum(timedeltas, datetime.timedelta())
