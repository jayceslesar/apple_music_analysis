import pandas as pd
from collections import Counter


def top_monthly_songs(path):
    df = pd.read_csv(path)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    years = [2018, 2019]
    songs_of_the_month = {}
    for year in years:
        for month in months:
            sub_df = df[(df['Year'] == year) & (df['Month Name'] == month)]
            songs_list = sub_df['Content Name'].to_list()
            artist_list = sub_df['Artist Name'].to_list()
            event_end_time_list = sub_df['Event End Timestamp'].to_list()
            fixed_songs = []
            fixed_artists = []
            fixed_event_end_time = []
            for song in range(len(songs_list)):
                fixed_songs.append(
                    songs_list[song].encode('utf8', 'namereplace'))
                fixed_artists.append(
                    artist_list[song].encode('utf8', 'namereplace'))
                fixed_event_end_time.append(event_end_time_list[song])

            fixed_songs_for_real = []
            fixed_artists_for_real = []
            fixed_event_end_time_for_real = []
            for i in range(len(fixed_songs)):
                try:
                    print(fixed_songs[i].decode("latin-1"))
                    fixed_songs_for_real.append(
                        fixed_songs[i].decode("latin-1"))

                    print(fixed_artists[i].decode("latin-1"))
                    fixed_artists_for_real.append(
                        fixed_artists[i].decode("latin-1"))
                    fixed_event_end_time_for_real.append(
                        fixed_event_end_time[i])
                except:
                    print('bad')
            stats = [fixed_songs_for_real[i] + ' - ' + fixed_artists_for_real[i]
                     for i in range(len(fixed_artists_for_real))]
            songs_of_the_month[month + ' - ' +
                               str(year)] = Counter(stats).most_common(1)

    for key in list(songs_of_the_month):
        if len(songs_of_the_month[key]) < 1:
            del songs_of_the_month[key]
    # return as dataframe
    rows = []
    for key in songs_of_the_month:
        row_to_add = []
        date = key.replace(' ', '').split('-')
        row_to_add.append(date[1])
        row_to_add.append(date[0])
        info = list(songs_of_the_month[key][0])
        song_name_title = info[0].split(' - ')
        song = song_name_title[0]
        row_to_add.append(song)
        artist = song_name_title[1]
        row_to_add.append(artist)
        plays = info[1]
        row_to_add.append(plays)
        combined_date = str(date[1]) + '-' + str(date[0])
        row_to_add.append(combined_date)
        rows.append(row_to_add)
    month_df = pd.DataFrame(
        rows, columns=['year', 'month', 'name', 'artist', 'plays', 'date_described'])
    return month_df


path = r'D:\apple_music_analysis\apple_music_viz\no_bads_extra_good.csv'

top_monthly_songs(path).to_csv('test.csv')
