import pandas as pd
import re
from nba_api.stats.library.data import players
from nba_api.stats.static import players
import time

# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()
print('Number of players fetched: {}'.format(len(nba_players)))
nba_players[:5]

list = pd.DataFrame(nba_players, columns = ['id', 'full_name', 'first_name', 'last_name', 'is_active'])

# set only active
print("Existing Dataframe is :\n", (list.loc[list.is_active]))

time.sleep(15)
