#cell 1
import pandas as pd
from matplotlib import pyplot as plt
#cell 2
nba_df = pd.read_csv("NBA_Data/NBA Player Stats(1950 - 2022).csv")
nba_df = nba_df[["Season", "Player", "G", "MP", "PTS", "TRB", "AST", "STL", "BLK", "TOV"]]
mj_nba_df = nba_df.loc[nba_df["Player"] == "Michael Jordan"]
lj_nba_df = nba_df.loc[nba_df["Player"] == "LeBron James"]
specific_player_df = nba_df.loc[(nba_df["Player"] == "LeBron James") | (nba_df["Player"] == "Michael Jordan")]
avg_games_df = specific_player_df.groupby("Player")["G"].mean()
specific_player_df.count()
test = 2 + 2
