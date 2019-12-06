import pandas as pd
import numpy as np
from collections import Counter
import date_funcs


def monthly_music_stats(path):
    try:
        df = pd.read_csv(path, encoding='latin1')
    except FileNotFoundError:
        print('No file found with ' + path)
        return
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    years = [2018, 2019]
    music_stats = {}
    for year in years:
        for month in months:
            sub_df = df.loc[(df['Month Name'] == month)]
            sub_df = sub_df.loc[sub_df['Year'] == year]
            if len(sub_df) == 0:
                continue
            artists = sub_df['Artist Name'].to_list()
            songs = sub_df['Content Name'].to_list()
            date_funcs.extract_dates(sub_df)
            plays_total = len(artists)
            music_stats[month + '-' + str(year)] = {}
            top_artist_and_count = Counter(artists).most_common(1)[0]
            top_artist = top_artist_and_count[0]
            top_song_and_count = Counter(songs).most_common(1)[0]
            artist_df = sub_df.loc[sub_df['Artist Name'] == top_artist]
            top_artist_song_list = artist_df['Content Name'].to_list()
            top_artist_song_count = Counter(
                top_artist_song_list).most_common(1)[0]
            music_stats[month + '-' +
                        str(year)]['top_song_and_count'] = top_song_and_count
            music_stats[month + '-' +
                        str(year)]['top_artist_song_count'] = top_artist_song_count
            music_stats[month + '-' +
                        str(year)]['top_artist_and_count'] = top_artist_and_count
            music_stats[month + '-' +
                        str(year)]['plays_total'] = plays_total
    return music_stats


path = r'D:\apple_music_data\no_bads_extra_good.csv'
x = monthly_music_stats(path)
print(x)
