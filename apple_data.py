# making a data class where we can call functions to look at the data in a certain way
import reclean
import date_funcs
from collections import Counter
import pandas as pd
import album_art


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
    def year_in_review_songs(self):
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
        return return_data

    def top_five_songs_year_dash(self):
        cols = ['song', 'artist', 'plays',
                'album_art_rgb', 'image_link', 'song_artist']
        songs, artists, plays, album_art_rgb, image_link, song_artist = [], [], [], [], [],  []
        top_five = self.year_in_review_songs(self)['top_five_songs']
        i = 0
        for song in top_five:
            songs.append(song[0].split('-')[0][:-1])
            artists.append(song[0].split('-')[1][1:])
            search = song[0].split('-')[0][:-1] + ' ' + \
                song[0].split('-')[1][1:]
            plays.append(song[1])
            album_art_rgb.append(album_art.compute_top_image_color(search))
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
                'y': str(df['plays'].to_list()[i]*.945/max(df['plays'].to_list())),
                'sizex': '0.2',
                'sizey': '0.3',
                'xanchor': 'center',
                'yanchor': 'bottom'
            }
            x_ref += .2
            images.append(curr_img)
        retun_data = {}
        retun_data['graph'] = to_graph
        retun_data['imgs'] = images
        return retun_data

    @staticmethod
    def year_in_review_artists(self):
        return_data = {}
        year = max(self.valid_years)
        df = self.data.loc[(self.data['Year'] == year)]
        return_data['top_five_artists'] = Counter(
            df['True Name'].to_list()).most_common(5)
        return_data['top_five_artists'] = Counter(
            df['Artist Name'].to_list()).most_common(5)
        return_data['top_five_genres'] = Counter(
            df['Genre'].to_list()).most_common(5)
        return_data['mins_total'] = format(date_funcs.mins_total(df), ',d')
        return_data['plays_total'] = len(df)
        return return_data
