# recleaning with pandas in attempt to keep as most data as possible
# with a focus on keeping complete data
import pandas as pd
import datetime


# takes in a path to a dataframe
# remove all rows that have a missing value in [Content Name, Artist Name, Event End Timestamp, Event Start Timestamp,]
def active_clean(path):
    cols_to_check = ['Content Name', 'Artist Name',
                     'Event Start Timestamp', 'Event End Timestamp', 'Client IP Address', 'Genre']
    rows_to_drop = []
    df = pd.read_csv(path, encoding='latin1')
    for col in cols_to_check:
        curr_col_bools = list(pd.isnull(df[col]))
        for i in range(len(curr_col_bools)):
            if curr_col_bools[i] == True:
                rows_to_drop.append(i)
    drop_these = list(set(rows_to_drop))
    df = df.drop(df.index[drop_these])
    trash_cols = []
    for col in df.columns:
        if col not in cols_to_check:
            trash_cols.append(col)
    df = df.drop(columns=trash_cols)
    song_artist = []
    artists = df['Artist Name'].to_list()
    songs = df['Content Name'].to_list()
    for i in range(len(songs)):
        song_artist.append(songs[i] + ' - ' + artists[i])
    df['True Name'] = song_artist
    years = []
    months_num = []
    months = []
    weekdays = []
    dates = df['Event Start Timestamp'].tolist()
    for date in dates:
        date_parts = date[:10].split('-')
        years.append(date_parts[0])
        months_num.append(date_parts[1])
        curr_date = datetime.datetime(
            int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
        weekdays.append(curr_date.strftime('%A'))
        months.append(curr_date.strftime('%b'))
    df['Year'] = years
    df['Month Num'] = months_num
    df['Month Name'] = months
    df['Weekday'] = weekdays
    # add weather daa (IE sunny, rainy...)
    return df
