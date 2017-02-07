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
api.login(os.environ['GMUSIC_USER'], os.environ['GMUSIC_PW'], Mobileclient.FROM_MAC_ADDRESS, locale=u'ja_JP')


# qfqnryeo3rdbdvv3jpscdfhmya
# Aqfqnryeo3rdbdvv3jpscdfhmya
search_result = api.get_artist_info(sys.argv[1])
embed()
