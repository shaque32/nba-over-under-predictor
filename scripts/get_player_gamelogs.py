from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
def getGameLogs():
    player_name = input("Enter the player's full name: ")
    season = input("Enter the season (e.g., '2022-23'): ")

    player = players.find_players_by_full_name(player_name)[0]
    gamelog = playergamelog.PlayerGameLog(player_id=player['id'], season=season)

    DataFrame = gamelog.get_data_frames()[0]
    columns_to_keep = ['GAME_DATE', 'MATCHUP', 'PTS', 'REB', 'AST']
    df_filtered = DataFrame[columns_to_keep]

    df_filtered = df_filtered.sort_values('GAME_DATE', ascending=False).reset_index(drop=True)

    filename = f'data/{player_name.replace(" ", "_").lower()}_gamelogs_{season}.csv'
    df_filtered.to_csv(filename, index=False)

if __name__ == "__main__":
    getGameLogs()
    print("Game logs have been saved successfully.")
