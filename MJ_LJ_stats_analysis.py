#cell 
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#cell 
nba_df = pd.read_csv("NBA_Data/NBA Player Stats(1950 - 2022).csv")
nba_df = nba_df[["Season", "Player", "G", "FG%", "3P%", "2P%", "MP", "PTS", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV"]]
#cell 
specific_player_df = nba_df.loc[(nba_df["Player"] == "LeBron James") | (nba_df["Player"] == "Michael Jordan")]
specific_player_df.head()
#cell
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
#cell 
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
#cell 
each_game_stats = pd.read_csv("NBA_Data/MJ_LJ_Games.csv")
each_game_stats.head()
#cell  
each_game_stats.rename(columns={"PLAYER_NAME": "Player", "FG_PCT": "FG%", "FG3_PCT": "3P%"}, inplace=True)
each_game_stats
#cell
each_game_stats = each_game_stats[["Season", "Player", "MATCHUP", "WL", "PTS", "FG%", "OREB", "DREB", "AST", "STL", "BLK", "TOV"]]
each_game_stats.head()
#cell 
#Check for na values
each_game_stats.count()
#cell 
each_game_stats.dropna(inplace=True)
#cell 
each_game_stats.count()
#cell
mean_pts = each_game_stats["PTS"].groupby(each_game_stats["Player"]).mean()
median_pts = each_game_stats["PTS"].groupby(each_game_stats["Player"]).median()
var_pts = each_game_stats["PTS"].groupby(each_game_stats["Player"]).var()
std_dev_pts = each_game_stats["PTS"].groupby(each_game_stats["Player"]).std()
std_err_pts = each_game_stats["PTS"].groupby(each_game_stats["Player"]).sem()

summary_lifetime_pts_df = pd.DataFrame({"Mean Points Scored": mean_pts, "Median Points Scored": median_pts, "Variance of Points Scored": var_pts,
                               "Std. Dev of Points Scored": std_dev_pts, "Std. Error of Points Scored": std_err_pts})
summary_lifetime_pts_df
#cell 
mean_fgp = each_game_stats["FG%"].groupby(each_game_stats["Player"]).mean()
median_fgp = each_game_stats["FG%"].groupby(each_game_stats["Player"]).median()
var_fgp = each_game_stats["FG%"].groupby(each_game_stats["Player"]).var()
std_dev_fgp = each_game_stats["FG%"].groupby(each_game_stats["Player"]).std()
std_err_fgp = each_game_stats["FG%"].groupby(each_game_stats["Player"]).sem()

summary_lifetime_fgp_df = pd.DataFrame({"Mean Field Goal %": mean_fgp, "Median Field Goal %": median_fgp, "Variance of Field Goal %": var_fgp,
                               "Std. Dev of Field Goal %": std_dev_fgp, "Std. Error of Field Goal %": std_err_fgp})
summary_lifetime_fgp_df
#cell 
mj_stats = each_game_stats.loc[each_game_stats["Season"] == 1991]
mj_stats
#cell 
#PTS stats when MJ won championship 1991 (age 27)
mean_pts_mj = mj_stats["PTS"].groupby(mj_stats["Player"]).mean()
median_pts_mj = mj_stats["PTS"].groupby(mj_stats["Player"]).median()
var_pts_mj = mj_stats["PTS"].groupby(mj_stats["Player"]).var()
std_dev_pts_mj = mj_stats["PTS"].groupby(mj_stats["Player"]).std()
std_err_pts_mj = mj_stats["PTS"].groupby(mj_stats["Player"]).sem()

summary_1991_pts_df = pd.DataFrame({"Mean Points Scored": mean_pts_mj, "Median Points Scored": median_pts_mj, "Variance of Points Scored": var_pts_mj,
                               "Std. Dev of Points Scored": std_dev_pts_mj, "Std. Error of Points Scored": std_err_pts_mj})
summary_1991_pts_df
#cell 
lj_stats = each_game_stats.loc[each_game_stats["Season"] == 2012]
lj_stats
#cell 
#PTS stats when LJ won championship 2012 (age 28)
mean_pts_lj = lj_stats["PTS"].groupby(lj_stats["Player"]).mean()
median_pts_lj = lj_stats["PTS"].groupby(lj_stats["Player"]).median()
var_pts_lj = lj_stats["PTS"].groupby(lj_stats["Player"]).var()
std_dev_pts_lj = lj_stats["PTS"].groupby(lj_stats["Player"]).std()
std_err_pts_lj = lj_stats["PTS"].groupby(lj_stats["Player"]).sem()

summary_2012_pts_df = pd.DataFrame({"Mean Points Scored": mean_pts_lj, "Median Points Scored": median_pts_lj, "Variance of Points Scored": var_pts_lj,
                               "Std. Dev of Points Scored": std_dev_pts_lj, "Std. Error of Points Scored": std_err_pts_lj})
summary_2012_pts_df
#cell 
summary_values_chart = mean_summary_df[["Avg. Games Played", "Avg. Mins Played", "Avg. Points Scored", "Avg. Rebounds", "Avg. Assists", "Avg. Steals", "Avg. Blocks", "Avg. Turnovers"]]
summary_values_chart.plot(kind="bar")
plt.legend(loc="upper center", bbox_to_anchor=(0.45,0.8))
plt.show()
#cell 
summary_per_chart = mean_summary_df[["Avg. Field Goal %", "Avg. 3 Point %", "Avg. 2 Point %"]]
summary_per_chart.plot(kind="bar")
plt.ylim(0, 0.75)
plt.legend(loc="upper center", bbox_to_anchor=(0.5,1))
plt.show()