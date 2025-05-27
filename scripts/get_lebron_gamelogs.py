from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import pandas as pd

lebron = players.find_players_by_full_name("LeBron James")[0]
gamelog = playergamelog.PlayerGameLog(player_id=lebron['id'], season='2022-23')

DataFrame = gamelog.get_data_frames()[0]
# Select relevant columns
columns_to_keep = ['GAME_DATE', 'MATCHUP', 'PTS', 'REB', 'AST']
df_filtered = DataFrame[columns_to_keep]

df_filtered = df_filtered.sort_values('GAME_DATE', ascending=False).reset_index(drop=True)

df_filtered.to_csv('data/lebron_gamelogs_2022-23.csv', index=False)