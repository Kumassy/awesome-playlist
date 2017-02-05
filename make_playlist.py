# coding:utf-8

from gmusicapi import Mobileclient
import os
import json

api = Mobileclient()
api.login(os.environ['GMUSIC_USER'], os.environ['GMUSIC_PW'], Mobileclient.FROM_MAC_ADDRESS)

search_result = api.search("サクラあっぱれーしょん")

playlist = api.create_playlist("てすとてすと")
# print(search_result['song_hits'])
# print(search_result['song_hits'][0])
# print(search_result['song_hits'][0]['track']['nid'])
# api.add_songs_to_playlist(playlist, search_result['song_hits'][0]['track']['nid'])
api.add_songs_to_playlist(playlist, search_result['song_hits'][0]['track']['storeId'])


# print(json.dumps(search_result['song_hits']))
