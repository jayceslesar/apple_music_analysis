# making a data class where we can call functions to look at the data in a certain way
import reclean
import date_funcs
from collections import Counter
import pandas as pd
import album_art

# ! TODO: rename vars
# ! TODO: clean up


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

    @staticmethod
    def week_in_review_songs(self, month):
        most_recent = self.data.iloc[-1]
        most_recent_date = most_recent['Year'] + '-' + \
            most_recent['Month Num'] + '-' + most_recent['Weekday Num']
        dates = date_funcs.past_week_dates(most_recent_date)
        better_dates = []
        for date in dates:
            curr = str(date).split('-')
            better_dates.append([curr[0], curr[1], curr[2]])
        better_dates = reversed(better_dates)
        dfs = []
        for date in better_dates:
            df = self.data.loc[(self.data['Year'] == date[0])]
            df = df.loc[(df['Month Num'] == date[1])]
            df = df.loc[(df['Weekday Num'] == date[2])]
            dfs.append(df)
        df = pd.concat(dfs, axis=0)
        NUM = 5
        return_data = {}
        return_data['top_five_songs'] = Counter(
            df['True Name'].to_list()).most_common(NUM)
        return_data['top_five_artists'] = Counter(
            df['Artist Name'].to_list()).most_common(NUM)
        return_data['top_five_genres'] = Counter(
            df['Genre'].to_list()).most_common(NUM)
        return_data['mins_total'] = format(date_funcs.mins_total(df), ',d')
        return_data['plays_total'] = len(df)
        return return_data

    @staticmethod
    def month_in_review_songs(self, month):
        NUM = 5
        return_data = {}
        year = max(self.valid_years)
        df = self.data.loc[(self.data['Year'] == year)]
        df = df.loc[(df['Month Name'] == month)]
        return_data['top_five_songs'] = Counter(
            df['True Name'].to_list()).most_common(NUM)
        return_data['top_five_artists'] = Counter(
            df['Artist Name'].to_list()).most_common(NUM)
        return_data['top_five_genres'] = Counter(
            df['Genre'].to_list()).most_common(NUM)
        return_data['mins_total'] = format(date_funcs.mins_total(df), ',d')
        return_data['plays_total'] = len(df)
        return return_data

    @staticmethod
    def year_in_review_songs(self, year):
        NUM = 5
        return_data = {}
        df = self.data.loc[(self.data['Year'] == year)]
        return_data['top_five_songs'] = Counter(
            df['True Name'].to_list()).most_common(NUM)
        return_data['top_five_artists'] = Counter(
            df['Artist Name'].to_list()).most_common(NUM)
        return_data['top_five_genres'] = Counter(
            df['Genre'].to_list()).most_common(NUM)
        return_data['mins_total'] = format(date_funcs.mins_total(df), ',d')
        return_data['plays_total'] = len(df)
        return return_data

    def top_five_songs_month_or_year_dash(self, month_or_year_or_week, song_or_artist):
        if len(month_or_year_or_week) == 3:
            type = 'month'
        if len(month_or_year_or_week) == 4:
            type = 'year'
        if month_or_year_or_week == 'week':
            type = 'week'
        GRAPH_HEIGHT = 0.945
        cols = ['song', 'artist', 'plays',
                'album_art_rgb', 'image_link', 'song_artist']
        songs, artists, plays, album_art_rgb, image_link, song_artist = [
        ], [], [], [], [], []
        if type == 'year':
            data = self.year_in_review_songs(self, month_or_year_or_week)
        if type == 'month':
            data = self.month_in_review_songs(
                self, month_or_year_or_week)
        if type == 'week':
            data = self.week_in_review_songs(
                self, month_or_year_or_week)
        top_five = data['top_five_songs']
        i = 0
        for song in top_five:
            songs.append(song[0].split('-')[0][:-1])
            artists.append(song[0].split('-')[1][1:])
            search = song[0].split('-')[0][:-1] + ' ' + \
                song[0].split('-')[1][1:]
            search = search.encode('raw_unicode_escape').decode('utf-8')
            search = album_art.fix(search)
            plays.append(song[1])
            album_art_rgb.append(
                album_art.compute_top_image_color(search))
            image_link.append(album_art.get_art(search))
            song_artist.append(songs[i] + ' - ' + artists[i])
            i += 1
        to_add = [songs, artists, plays,
                  album_art_rgb, image_link, song_artist]
        df = pd.DataFrame(columns=cols)
        for col in range(len(cols)):
            df[cols[col]] = to_add[col]
        to_graph = []
        images = []
        x_ref = 0.1
        for i in range(len(df)):
            curr = {
                'x': ['<b>' + df['song_artist'].to_list()[i] + '<b>'],
                'y': [str(df['plays'].to_list()[i])],
                'type': 'bar',
                'name': '<b>' + df['song_artist'].to_list()[i] + '<b>',
                'width': '.5',
                'marker': {
                    'color': df['album_art_rgb'].to_list()[i]
                }
            }
            to_graph.append(curr)
            curr_img = {
                'source': df['image_link'].to_list()[i],
                'xref': 'paper',
                'yref': 'paper',
                'x': str(x_ref),
                'y': str(df['plays'].to_list()[i]*GRAPH_HEIGHT/max(df['plays'].to_list())),
                'sizex': '0.2',
                'sizey': '0.3',
                'xanchor': 'center',
                'yanchor': 'bottom'
            }
            x_ref += .2
            images.append(curr_img)
        return_data = {}
        return_data['graph'] = to_graph
        return_data['imgs'] = images
        return_data['type'] = type
        if type == 'month':
            return_data['month'] = month_or_year_or_week
            return_data['year'] = max(self.valid_years)
        if type == 'year':
            return_data['year'] = month_or_year_or_week
        return_data['mins_total'] = data['mins_total']
        return return_data

    @staticmethod
    def year_in_review_artists(self):
        return_data = {}
        year = max(self.valid_years)
        df = self.data.loc[(self.data['Year'] == year)]
        return_data['true_name'] = Counter(
            df['True Name'].to_list()).most_common(5)
        return_data['top_five_artists'] = Counter(
            df['Artist Name'].to_list()).most_common(5)
        return_data['top_five_genres'] = Counter(
            df['Genre'].to_list()).most_common(5)
        return_data['mins_total'] = format(date_funcs.mins_total(df), ',d')
        return_data['plays_total'] = len(df)
        return return_data

       # def top_five_year_dash(self, type):
