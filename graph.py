import dash_stuff
import apple_data
import pandas as pd


path = r'D:\apple_music_data\first_maybe_good.csv'
data = apple_data.AppleData(path)
dash_stuff.dash_test(data.top_five_songs_month_or_year_dash('2019', 'song'))
