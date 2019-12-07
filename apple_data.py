# making a data class where we can call functions to look at the data in a certain way
import reclean
import date_funcs
from collections import Counter
import pandas as pd
import album_art
import plotly.express as px
import plotly.graph_objects as go


class AppleData:
    def __init__(self, path):
        self.data = reclean.active_clean(path)
        self.valid_years = list(set(self.data['Year'].to_list()))

    def mins_total(self, year):
        df = self.data.loc[(self.data['Year'] == year)]
        try:
            self.valid_years.index(year)
            return format(date_funcs.mins_total(df), ',d')
        except ValueError:
            print(year + ' is not in the dataset.  Pick from valid years.')
            print('Valid Years: ' + str(sorted(self.valid_years)))
            return

    def year_in_review(self):
        return_data = {}
        year = max(self.valid_years)
        df = self.data.loc[(self.data['Year'] == year)]
        return_data['top_five_songs'] = Counter(
            df['True Name'].to_list()).most_common(5)
        return_data['top_five_artists'] = Counter(
            df['Artist Name'].to_list()).most_common(5)
        return_data['top_five_genres'] = Counter(
            df['Genre'].to_list()).most_common(5)
        return_data['mins_total'] = format(date_funcs.mins_total(df), ',d')
        return_data['plays_total'] = len(df)
        self.return_data = return_data

    def top_five_songs_dash(self):
        cols = ['song', 'artist', 'plays', 'image', 'song_artist']
        songs = []
        artists = []
        plays = []
        album_art_links = []
        song_artist = []
        top_five = self.return_data['top_five_songs']
        i = 0
        for song in top_five:
            songs.append(song[0].split('-')[0][:-1])
            artists.append(song[0].split('-')[1][1:])
            search = song[0].split('-')[0][:-1] + ' ' + \
                song[0].split('-')[1][1:]
            plays.append(song[1])
            album_art_links.append(album_art.get_art(search))
            song_artist.append(songs[i] + ' - ' + artists[i])
            i += 1
        to_add = [songs, artists, plays, album_art_links, song_artist]
        df = pd.DataFrame(columns=cols)
        for col in range(len(cols)):
            df[cols[col]] = to_add[col]
        fig = px.bar(df, x='song_artist', y='plays',
                     hover_data=['artist'], color='song',
                     labels={'plays': 'num plays'}, height=800)
        fig.show()


path = r'D:\apple_music_data\first_maybe_good.csv'

test = AppleData(path)
test.year_in_review()
print(test.top_five_songs_dash())
