from gmusicapi import Mobileclient
import os
import json
import pandas as pd
from IPython import embed
from logging import getLogger, StreamHandler, FileHandler, DEBUG, Formatter
import random
import time
import re
import sys

def filter_song(song_list, title, artist):
    t = filter((lambda song: re.search(title.decode('utf-8'), song['track']['title'])), song_list)
    return filter((lambda song: re.search(artist.decode('utf-8'), song['track']['artist'])), t)

api = Mobileclient()
api.login(os.environ['GMUSIC_USER'], os.environ['GMUSIC_PW'], Mobileclient.FROM_MAC_ADDRESS, locale=u'ja_JP')


if len(sys.argv) != 3:
    print("Invalid Arguments")
    exit(1)
print('Searching %s / %s ...' % (sys.argv[1], sys.argv[2]))
search_result = api.search('%s %s' % (sys.argv[1], sys.argv[2]))
song_list = search_result['song_hits']

filterd_list = filter_song(song_list, sys.argv[1], sys.argv[2])

if len(song_list) > 0:
    print('%d songs found' % len(song_list))
if len(filterd_list) > 0:
    print('Exact match: %s / %s' % (filterd_list[0]['track']['title'], filterd_list[0]['track']['artist']))

embed()
