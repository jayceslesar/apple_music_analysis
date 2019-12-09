import dash_stuff
import apple_data
import pandas as pd


path = r'D:\apple_music_data\first_maybe_good.csv'
data = apple_data.AppleData(path).top_five_songs_year_dash()
dash_stuff.dash_test(data)
