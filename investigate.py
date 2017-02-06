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


api = Mobileclient()
api.login(os.environ['GMUSIC_USER'], os.environ['GMUSIC_PW'], Mobileclient.FROM_MAC_ADDRESS)


if len(sys.argv) != 3:
    print("Invalid Arguments")
    exit(1)
print('Searching %s / %s ...' % (sys.argv[1], sys.argv[2]))
search_result = api.search('%s %s' % (sys.argv[1], sys.argv[2]))
song_list = search_result['song_hits']
embed()
