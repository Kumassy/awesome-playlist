# coding:utf-8

from gmusicapi import Mobileclient
import os
import json
import pandas as pd
from IPython import embed

# api = Mobileclient()
# api.login(os.environ['GMUSIC_USER'], os.environ['GMUSIC_PW'], Mobileclient.FROM_MAC_ADDRESS)
#
# search_result = api.search("サクラあっぱれーしょん")
#
# playlist = api.create_playlist("てすとてすと")
# api.add_songs_to_playlist(playlist, search_result['song_hits'][0]['track']['storeId'])

# print(json.dumps(search_result['song_hits']))

df = pd.read_csv('anison.csv', quotechar='"', escapechar="\\")
embed()
# print df[0]
