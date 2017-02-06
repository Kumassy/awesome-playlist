# coding:utf-8

from gmusicapi import Mobileclient
import os
import json
import pandas as pd
from IPython import embed
from logging import getLogger, StreamHandler, FileHandler, DEBUG, Formatter
import random
import time
import re


def is_invalid_artist(artist):
    return re.search(r"インストゥルメンタル", artist)

def filter_song(song_list, title, artist):
    t = filter((lambda song: re.search(title.decode('utf-8'), song['track']['title'])), song_list)
    return filter((lambda song: re.search(artist.decode('utf-8'), song['track']['artist'])), t)

logger = getLogger(__name__)
stream_handler = StreamHandler()
file_handler = FileHandler(filename="log.txt")
stream_handler.setLevel(DEBUG)
file_handler.setLevel(DEBUG)
logger.setLevel(DEBUG)

file_handler.setFormatter(Formatter('[%(asctime)s] %(message)s'))
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


api = Mobileclient()
api.login(os.environ['GMUSIC_USER'], os.environ['GMUSIC_PW'], Mobileclient.FROM_MAC_ADDRESS)

playlist = api.create_playlist("ぼくのかんがえたさいきょうのぷれいりすと")
logger.debug('playlist was created: %s' % playlist)

df = pd.read_csv('anison.csv', quotechar='"', escapechar="\\")
# embed()
music_list = [df.values[i] for i in range(1000)]



for music in music_list:
    logger.debug('Searching %s / %s from %s ...' % (music[6], music[7], music[2]))

    if is_invalid_artist(music[7]):
        continue
    search_result = api.search('%s %s' % (music[6], music[7]))
    logger.debug('%d songs found' % len(search_result['song_hits']))

    song_list = filter_song(search_result['song_hits'], music[6], music[7])
    logger.debug('Reduced to %d songs' % len(song_list))

    if len(song_list) > 0:
        # embed()
        logger.debug('Add to the playlist: %s / %s' % (song_list[0]['track']['title'], song_list[0]['track']['artist']))
        api.add_songs_to_playlist(playlist, song_list[0]['track']['storeId'])

    # sleep for a while
    time.sleep(random.uniform(2.0, 4.0))


# print(json.dumps(search_result['song_hits']))
