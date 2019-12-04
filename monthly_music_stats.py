import pandas as pd
import numpy as np
from collections import Counter


def monthly_music_stats(path):
    df = pd.read_csv(path, encoding='latin1')
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    years = [2018, 2019]
    music_stats = {}
    for year in years:
        for month in months:
            music_stats[month + '-' + str(year)] = {}
            sub_df = df.loc[(df['Month Name'] == month)]
            sub_df = sub_df.loc[sub_df['Year'] == year]
            artists = sub_df['Artist Name'].to_list()
            songs = sub_df['Content Name'].to_list()
            plays_total = len(artists)
            if len(sub_df) == 0:
                continue
            top_artist_and_count = Counter(artists).most_common(1)[0]
            top_artist = top_artist_and_count[0]
            top_song_and_count = Counter(songs).most_common(1)[0]
            top_artist_song_list = sub_df.loc[sub_df['Artist Name']
                                              == top_artist]['Content Name'].to_list()
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
