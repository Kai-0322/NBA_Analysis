#cell 1
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#cell 2
nba_df = pd.read_csv("NBA_Data/NBA Player Stats(1950 - 2022).csv")
nba_df = nba_df[["Season", "Player", "G", "MP", "PTS", "TRB", "AST", "STL", "BLK", "TOV"]]
#cell 3
specific_player_df = nba_df.loc[(nba_df["Player"] == "LeBron James") | (nba_df["Player"] == "Michael Jordan")]
specific_player_df.head()
#cell 4
#Lifetime Total Stats of each player (as of 2022 LeBron James)
total_games = specific_player_df["G"].groupby(specific_player_df["Player"]).sum()
total_mins = specific_player_df["MP"].groupby(specific_player_df["Player"]).sum()
total_pts = specific_player_df["PTS"].groupby(specific_player_df["Player"]).sum()
total_reb = specific_player_df["TRB"].groupby(specific_player_df["Player"]).sum()
total_ast = specific_player_df["AST"].groupby(specific_player_df["Player"]).sum()
total_stl = specific_player_df["STL"].groupby(specific_player_df["Player"]).sum()
total_blk = specific_player_df["BLK"].groupby(specific_player_df["Player"]).sum()
total_tov = specific_player_df["TOV"].groupby(specific_player_df["Player"]).sum()
total_summary_df = pd.DataFrame({"Total Games Played": total_games, "Total Mins Played": total_mins, "Total Points Scored": total_pts,
                           "Total Rebounds": total_reb, "Total Assists": total_ast, "Total Steals": total_stl, "Total Blocks": total_blk, 
                           "Total Turnovers": total_tov})
total_summary_df
#cell 5
#Lifetime Average Stats of each player (as of 2022 LeBron James)
mean_games = specific_player_df["G"].groupby(specific_player_df["Player"]).mean()
mean_mins = specific_player_df["MP"].groupby(specific_player_df["Player"]).mean()
mean_pts = specific_player_df["PTS"].groupby(specific_player_df["Player"]).mean()
mean_reb = specific_player_df["TRB"].groupby(specific_player_df["Player"]).mean()
mean_ast = specific_player_df["AST"].groupby(specific_player_df["Player"]).mean()
mean_stl = specific_player_df["STL"].groupby(specific_player_df["Player"]).mean()
mean_blk = specific_player_df["BLK"].groupby(specific_player_df["Player"]).mean()
mean_tov = specific_player_df["TOV"].groupby(specific_player_df["Player"]).mean()
mean_summary_df = pd.DataFrame({"Avg. Games Played": mean_games, "Avg. Mins Played": mean_mins, "Avg. Points Scored": mean_pts,
                           "Avg. Rebounds": mean_reb, "Avg. Assists": mean_ast, "Avg. Steals": mean_stl, "Avg. Blocks": mean_blk, 
                           "Avg. Turnovers": mean_tov})
mean_summary_df
#cell 6
each_game_stats = pd.read_csv("NBA_Data/NBA Player Box Score Stats(1950 - 2022).csv")
each_game_stats.head()
#cell 7
mj_each_game = each_game_stats.loc[each_game_stats["PLAYER_NAME"] == "Michael Jordan"]
mj_each_game
#cell 8
champ_mj_avg = mj_each_game[(mj_each_game["Season"] == 1991)]["PTS"].mean()
champ_mj_avg
#cell 9 
lj_each_game = each_game_stats.loc[each_game_stats["PLAYER_NAME"] == "LeBron James"]
lj_each_game
#cell 10
champ_lj_avg = lj_each_game[(lj_each_game["Season"] == 2012)]["PTS"].mean()
champ_lj_avg
#cell 11 
#Average Points each player scored when they won championship (around the same age)
champ_avg = pd.DataFrame({"Avg. Points MJ Scored": champ_mj_avg, "Avg. Points LJ Scored": champ_lj_avg}, index = [0])
champ_avg
#cell 12
mj_pts = mj_each_game.loc[mj_each_game["Season"] == 1991]
mj_pts
#cell 13
x_axis = np.arange(len(mj_pts["MATCHUP"]))
tick_locations = [value+0.4 for value in x_axis]
plt.figure(figsize=(20,4))
plt.plot(x_axis, mj_pts["PTS"], color='r')
plt.xticks(tick_locations, mj_pts["MATCHUP"], rotation="vertical")
plt.show()
#cell 14
mj_nba_df = nba_df.loc[nba_df["Player"] == "Michael Jordan"]
#cell 15
lj_nba_df = nba_df.loc[nba_df["Player"] == "LeBron James"]