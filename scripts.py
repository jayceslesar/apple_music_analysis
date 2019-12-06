import pandas as pd
import date_funcs


def mins_total(df):
    times = []
    ends = date_funcs.extract_dates(df['Event End Timestamp'].to_list())
    starts = date_funcs.extract_dates(df['Event Start Timestamp'].to_list())
    for i in range(len(ends)):
        times.append(date_funcs.minutes_played(starts[i], ends[i]))
    total_seconds = 0
    for time in times:
        total_seconds += time.seconds
    mins = int(round(total_seconds/60, 0))
    return mins


path = r'D:\apple_music_data\apple_super_clean.csv'
print(mins_total(path))
