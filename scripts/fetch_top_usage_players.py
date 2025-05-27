import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import os


def fetch_top_usage_players(season='2023-23', limit = 50):
    # Load the Per Possession Stats table
    tables = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2023_advanced.html")
    df = tables[0]

    # Remove duplicate header rows and empty rows
    df = df[df['Rk'] != 'Rk']
    df = df.dropna(subset=['Player', 'USG%'])

    # Keep only Player and USG% columns
    df = df[['Player', 'USG%']]

    # Convert USG% to float and sort
    df['USG%'] = pd.to_numeric(df['USG%'], errors='coerce')
    df = df.dropna(subset=['USG%'])
    df = df.sort_values('USG%', ascending=False).head(50)

    # Loop over top players
    for player_name in df['Player']:
        # Find player ID using nba_api
        search = players.find_players_by_full_name(player_name)
        if not search:
            continue
        player_id = search[0]['id']

        # Pull game log for the specified season
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)
        gamelog_df = gamelog.get_data_frames()[0]

        # Save as CSV in data subfolder
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        os.makedirs(data_dir, exist_ok=True)
        filename = os.path.join(data_dir, f"{player_name.replace(' ', '_')}_gamelog_{season}.csv")
        gamelog_df.to_csv(filename, index=False)

if __name__ == "__main__":
    fetch_top_usage_players()
    print("Top usage players' game logs have been saved successfully.")
# This script fetches the top 50 players by usage rate for the 2022-23 season