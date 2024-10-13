from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# API ID and Hash
API_ID = int(os.getenv('22118129'))
API_HASH = os.getenv('43c66e3314921552d9330a4b05b18800')

# Delays (still hardcoded, but could be moved to .env if needed)
DELAYS = {
    'ACCOUNT': [5, 15],
    'PLAY': [5, 15],
    'ERROR_PLAY': [60, 180],
}

# Use proxies or not
PROXY = os.getenv('PROXY') == 'false'

# Play drop game
PLAY_GAMES = os.getenv('PLAY_GAMES') == 'True'

# Points with each play game; max 280
POINTS = list(map(int, os.getenv('POINTS').split(',')))

# Title blacklist tasks
BLACKLIST_TASKS = os.getenv('BLACKLIST_TASKS').split(',')

# Session folder
WORKDIR = os.getenv('WORKDIR')

ACCOUNT_PER_ONCE = int(os.getenv('ACCOUNT_PER_ONCE'))
