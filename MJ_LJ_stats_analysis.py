#cell 1
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#cell 2
nba_df = pd.read_csv("NBA_Data/NBA Player Stats(1950 - 2022).csv")
nba_df = nba_df[["Season", "Player", "G", "FG%", "3P%", "2P%", "MP", "PTS", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV"]]
#cell 3
specific_player_df = nba_df.loc[(nba_df["Player"] == "LeBron James") | (nba_df["Player"] == "Michael Jordan")]
specific_player_df.head()
#cell 4
#Lifetime Average Stats of each player (as of 2022 LeBron James)
mean_games = specific_player_df["G"].groupby(specific_player_df["Player"]).mean()
mean_fgp = specific_player_df["FG%"].groupby(specific_player_df["Player"]).mean()
mean_3pc = specific_player_df["3P%"].groupby(specific_player_df["Player"]).mean()
mean_2pc = specific_player_df["2P%"].groupby(specific_player_df["Player"]).mean()
mean_mins = specific_player_df["MP"].groupby(specific_player_df["Player"]).mean()
mean_pts = specific_player_df["PTS"].groupby(specific_player_df["Player"]).mean()
mean_reb = specific_player_df["TRB"].groupby(specific_player_df["Player"]).mean()
mean_ast = specific_player_df["AST"].groupby(specific_player_df["Player"]).mean()
mean_stl = specific_player_df["STL"].groupby(specific_player_df["Player"]).mean()
mean_blk = specific_player_df["BLK"].groupby(specific_player_df["Player"]).mean()
mean_tov = specific_player_df["TOV"].groupby(specific_player_df["Player"]).mean()
mean_summary_df = pd.DataFrame({"Avg. Games Played": mean_games, "Avg. Mins Played": mean_mins, "Avg. Points Scored": mean_pts,
                                "Avg. Field Goal %": mean_fgp, "Avg. 3 Point %": mean_3pc, "Avg. 2 Point %": mean_2pc,
                           "Avg. Rebounds": mean_reb, "Avg. Assists": mean_ast, "Avg. Steals": mean_stl, "Avg. Blocks": mean_blk, 
                           "Avg. Turnovers": mean_tov})
mean_summary_df
#cell 5
each_game_stats = pd.read_csv("NBA_Data/MJ_LJ_Games.csv")
each_game_stats.head()
#cell 6  
each_game_stats.rename(columns={"PLAYER_NAME": "Player", "FG_PCT": "FG%", "FG3_PCT": "3P%"}, inplace=True)
each_game_stats
#cell 7
each_game_stats = each_game_stats[["Season", "Player", "MATCHUP", "WL", "PTS", "FG%", "OREB", "DREB", "AST", "STL", "BLK", "TOV"]]
each_game_stats.head()
#cell 8
#Check for na values
each_game_stats.count()
#cell 9 
each_game_stats.dropna(inplace=True)
#cell 10
each_game_stats.count()
#cell 11 
mj_each_game = each_game_stats.loc[each_game_stats["Player"] == "Michael Jordan"]
mj_each_game
#cell 12
champ_mj_avg = mj_each_game[(mj_each_game["Season"] == 1991)]["PTS"].mean()
champ_mj_avg
#cell 13
lj_each_game = each_game_stats.loc[each_game_stats["Player"] == "LeBron James"]
lj_each_game
#cell 14
champ_lj_avg = lj_each_game[(lj_each_game["Season"] == 2012)]["PTS"].mean()
champ_lj_avg
#cell 15
#Average Points each player scored when they won championship (around the same age)
champ_avg = pd.DataFrame({"Avg. Points MJ Scored": champ_mj_avg, "Avg. Points LJ Scored": champ_lj_avg}, index = [0])
champ_avg
#cell 16
mj_pts = mj_each_game.loc[mj_each_game["Season"] == 1991]
mj_pts
#cell 17
summary_values_chart = mean_summary_df[["Avg. Games Played", "Avg. Mins Played", "Avg. Points Scored", "Avg. Rebounds", "Avg. Assists", "Avg. Steals", "Avg. Blocks", "Avg. Turnovers"]]
summary_values_chart.plot(kind="bar")
plt.legend(loc="upper center", bbox_to_anchor=(0.45,0.8))
plt.show()
#cell 18
summary_per_chart = mean_summary_df[["Avg. Field Goal %", "Avg. 3 Point %", "Avg. 2 Point %"]]
summary_per_chart.plot(kind="bar")
plt.ylim(0, 0.75)
plt.legend(loc="upper center", bbox_to_anchor=(0.5,1))
plt.show()