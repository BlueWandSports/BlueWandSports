import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import players
import time


luka_id = next((x for x in players.get_players() if x.get("full_name") == "Luka Doncic"), None).get("id")

gamelog_luka = pd.concat(playergamelog.PlayerGameLog(player_id=luka_id, season=SeasonAll.all).get_data_frames())
gamelog_luka["GAME_DATE"] = pd.to_datetime(gamelog_luka["GAME_DATE"], format="%b %d, %Y")
gamelog_luka = gamelog_luka.query("GAME_DATE.dt.year in [2023]")
print(gamelog_luka)

time.sleep(15)
