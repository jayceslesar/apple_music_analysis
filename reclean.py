# recleaning with pandas in attempt to keep as most data as possible
# with a focus on keeping complete data
import pandas as pd
import math


# takes in a path to a dataframe
# remove all rows that have a missing value in [Content Name, Artist Name, Event End Timestamp, Event Start Timestamp,]
def active_clean(path):
    cols_to_check = ['Content Name', 'Artist Name',
                     'Event Start Timestamp', 'Event End Timestamp']
    rows_to_drop = []
    df = pd.read_csv(path, encoding='latin1')
    for col in cols_to_check:
        curr_col_bools = list(pd.isnull(df[col]))
        for i in range(len(curr_col_bools)):
            if curr_col_bools[i] == True:
                rows_to_drop.append(i)
    drop_these = list(set(rows_to_drop))
    df = df.drop(df.index[drop_these])
    return df


path = r'D:\apple_music_data\apple_music_data.csv'
df = active_clean(path)
df.to_csv('apple_super_clean.csv')
