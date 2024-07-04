from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import PlayerGameLogs
from nba_api.stats.endpoints import shotchartdetail
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
player_game_logs = PlayerGameLogs(
    season_nullable='2023-24',  
    player_id_nullable=201935, 
    season_type_nullable='Regular Season'
)
df = player_game_logs.get_data_frames()[0]
df['MATCHUP'] = df['MATCHUP'].astype(str)
df['OPP'] = ""
for i in range(len(df)):
    matchup = df.iloc[i, 9]
    df.iloc[i, -1] = matchup[-3:]
df['H/A'] = ""
for i in range(len(df)):
    matchup = df.iloc[i, 9]
    if 'vs.' in matchup:
        df.iloc[i, -1] = 'Home'
    else:
        df.iloc[i, -1] = 'Away'
harden_game_log = df[['MATCHUP', 'WL', 'MIN', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'PTS',  'AST', 'REB', 'STL', 'BLK', 'TOV', 'OPP', 'H/A','FG3M','FG3A','FGA','FGM','FTA','FTM']] 

# Win Loss Stats Comparison
wins = 46
losses = 26
average_stats = harden_game_log.groupby('WL')[['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG3M','FG3A','FGA','FGM','FTA','FTM']].sum().reset_index()
average_stats['2PA'] = average_stats['FGA'] - average_stats['FG3A']
average_stats['2PM'] = average_stats['FGM'] - average_stats['FG3M']
average_stats['2PT_PCT'] = round(average_stats['2PM']/average_stats['2PA'], 3)
average_stats['FG_PCT'] = round(average_stats['FGM']/average_stats['FGA'], 3)
average_stats['FG3_PCT'] = round(average_stats['FG3M']/average_stats['FG3A'], 3)
average_stats['FT_PCT'] = round(average_stats['FTM']/average_stats['FTA'], 3)
average_stats[['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG3M','FG3A','FGA','FGM','FTA','FTM','2PA','2PM','FG_PCT','FT_PCT','FG3_PCT']] = average_stats[['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG3M','FG3A','FGA','FGM','FTA','FTM','2PA','2PM','FG_PCT','FT_PCT','FG3_PCT']].astype(float)
columns = ['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG3M','FG3A','FGA','FGM','FTA','FTM','2PA','2PM']
average_stats.loc[0, columns] /= losses
average_stats.loc[1, columns] /= wins
average_stats[columns] = average_stats[columns].round(1)
# Home vs Away Stats Comparison
loc_stats = harden_game_log.groupby('H/A')[['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG_PCT', 'FG3_PCT', 'FT_PCT','FG3M','FG3A','FGA','FGM','FTA','FTM']].sum().reset_index()
loc_stats['2PA'] = loc_stats['FGA'] - loc_stats['FG3A']
loc_stats['2PM'] = loc_stats['FGM'] - loc_stats['FG3M']
loc_stats['2PT_PCT'] = round(loc_stats['2PM']/loc_stats['2PA'], 3)
loc_stats['FG_PCT'] = round(loc_stats['FGM']/loc_stats['FGA'], 3)
loc_stats['FG3_PCT'] = round(loc_stats['FG3M']/loc_stats['FG3A'], 3)
loc_stats['FT_PCT'] = round(loc_stats['FTM']/loc_stats['FTA'], 3)
columns = ['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG3M','FG3A','FGA','FGM','FTA','FTM','2PA','2PM']
for i in columns:
    loc_stats[i] = round(loc_stats[i]/36,1)
# Stats by Opponent Comparison
matchup_stats = harden_game_log.groupby('OPP')[['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG_PCT', 'FG3_PCT', 'FT_PCT','FG3M','FG3A','FGA','FGM','FTA','FTM']].sum().reset_index()
matchup_stats['2PA'] = matchup_stats['FGA'] - matchup_stats['FG3A']
matchup_stats['2PM'] = matchup_stats['FGM'] - matchup_stats['FG3M']
matchup_stats['2PT_PCT'] = round(matchup_stats['2PM']/matchup_stats['2PA'], 3)
matchup_stats['FG_PCT'] = round(matchup_stats['FGM']/matchup_stats['FGA'], 3)
matchup_stats['FG3_PCT'] = round(matchup_stats['FG3M']/matchup_stats['FG3A'], 3)
matchup_stats['FT_PCT'] = round(matchup_stats['FTM']/matchup_stats['FTA'], 3)
matchup_stats[['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG3M','FG3A','FGA','FGM','FTA','FTM','2PA','2PM','FG_PCT','FT_PCT','FG3_PCT']] = matchup_stats[['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG3M','FG3A','FGA','FGM','FTA','FTM','2PA','2PM','FG_PCT','FT_PCT','FG3_PCT']].astype(float)
columns = ['MIN','PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG3M','FG3A','FGA','FGM','FTA','FTM','2PA','2PM']
matchup_stats.loc[0, columns] /= 2
matchup_stats.loc[1, columns] /= 2
matchup_stats.loc[2, columns] /= 2
matchup_stats.loc[3, columns] /= 2
matchup_stats.loc[4, columns] /= 1
matchup_stats.loc[5, columns] /= 2
matchup_stats.loc[6, columns] /= 3
matchup_stats.loc[7, columns] /= 4
matchup_stats.loc[8, columns] /= 2
matchup_stats.loc[9, columns] /= 4
matchup_stats.loc[10, columns] /= 2
matchup_stats.loc[11, columns] /= 2
matchup_stats.loc[12, columns] /= 3
matchup_stats.loc[13, columns] /= 4
matchup_stats.loc[14, columns] /= 2
matchup_stats.loc[15, columns] /= 2
matchup_stats.loc[16, columns] /= 4
matchup_stats.loc[17, columns] /= 3
matchup_stats.loc[18, columns] /= 2
matchup_stats.loc[19, columns] /= 3
matchup_stats.loc[20, columns] /= 1
matchup_stats.loc[21, columns] /= 2
matchup_stats.loc[22, columns] /= 2
matchup_stats.loc[23, columns] /= 3
matchup_stats.loc[24, columns] /= 4
matchup_stats.loc[25, columns] /= 2
matchup_stats.loc[26, columns] /= 2
matchup_stats.loc[27, columns] /= 3
matchup_stats.loc[28, columns] /= 2
matchup_stats[columns] = matchup_stats[columns].round(1)
# Reg Vs Playoff Career Stats
# Regular Season Career Stats
career = playercareerstats.PlayerCareerStats(player_id=201935)
df2 = career.get_data_frames()[0]
df2.rename(columns={'TEAM_ABBREVIATION': 'TEAM'}, inplace=True)
df2.rename(columns={'FG_PCT': 'FG PCT'}, inplace=True)
df2.rename(columns={'FG3_PCT': '3PT PCT'}, inplace=True)
df2.rename(columns={'FT_PCT': 'FT PCT'}, inplace=True)
df2.rename(columns={'PLAYER_AGE': 'AGE'}, inplace=True)
df2 = df2[df2['TEAM'] != 'TOT']
gp = df2['GP'].sum()
mins = round(df2['MIN'].sum()/gp, 1)
fg_pct = round(df2['FGM'].sum()/df2['FGA'].sum(), 3)
ft_pct = round(df2['FTM'].sum()/df2['FTA'].sum(), 3)
threept_pct = round(df2['FG3M'].sum()/df2['FG3A'].sum(), 3)
points = round(df2['PTS'].sum()/gp, 1)
assists = round(df2['AST'].sum()/gp, 1)
rebounds = round(df2['REB'].sum()/gp, 1)
turnovers = round(df2['TOV'].sum()/gp, 1)
steals = round(df2['STL'].sum()/gp, 1)
blocks = round(df2['BLK'].sum()/gp, 1)
threes_shot = round(df2['FG3A'].sum()/gp,1)
fgs_shot = round(df2['FGA'].sum()/gp, 1)
twos_shot = round(fgs_shot-threes_shot,1)
fgm = round(df2['FGM'].sum()/gp, 1)
threesm = round(df2['FG3M'].sum()/gp, 1)
twosm = round(fgm-threesm,1)
two_pct = round((df2['FGM'].sum()-df2['FG3M'].sum())/(df2['FGA'].sum()-df2['FG3A'].sum()),3)
ftm = round(df2['FTM'].sum()/gp,1)
fta = round(df2['FTA'].sum()/gp,1)
# Playoffs Career Stats
df4= career.get_data_frames()[2]
df4.rename(columns={'TEAM_ABBREVIATION': 'TEAM'}, inplace=True)
df4.rename(columns={'FG_PCT': 'FG PCT'}, inplace=True)
df4.rename(columns={'FG3_PCT': '3PT PCT'}, inplace=True)
df4.rename(columns={'FT_PCT': 'FT PCT'}, inplace=True)
df4.rename(columns={'PLAYER_AGE': 'AGE'}, inplace=True)
gp = df4['GP'].sum()
mins2 = round(df4['MIN'].sum()/gp, 1)
fg_pct2 = round(df4['FGM'].sum()/df4['FGA'].sum(), 3)
ft_pct2 = round(df4['FTM'].sum()/df4['FTA'].sum(), 3)
threept_pct2 = round(df4['FG3M'].sum()/df4['FG3A'].sum(), 3)
points2 = round(df4['PTS'].sum()/gp, 1)
assists2 = round(df4['AST'].sum()/gp, 1)
rebounds2 = round(df4['REB'].sum()/gp, 1)
turnovers2 = round(df4['TOV'].sum()/gp, 1)
steals2 = round(df4['STL'].sum()/gp, 1)
blocks2 = round(df4['BLK'].sum()/gp, 1)
threes_shot2 = round(df4['FG3A'].sum()/gp,1)
fgs_shot2 = round(df4['FGA'].sum()/gp, 1)
twos_shot2 = round(fgs_shot2-threes_shot2,1)
fgm2 = round(df4['FGM'].sum()/gp, 1)
threesm2 = round(df4['FG3M'].sum()/gp, 1)
twosm2 = round(fgm2-threesm2, 1)
two_pct2 = round((df4['FGM'].sum()-df4['FG3M'].sum())/(df4['FGA'].sum()-df4['FG3A'].sum()),3)
ftm2 = round(df4['FTM'].sum()/gp,1)
fta2 = round(df4['FTA'].sum()/gp,1)
stats_dict = [{'Season': 'Regular',
    'Mins':mins,
    'PPG': points,
    'APG': assists,
    'RPG': rebounds,
    'STL': steals,
    'BLK': blocks,
    'TOV': turnovers, 
    'FG PCT': fg_pct,
    'FT PCT': ft_pct,
    '3PT PCT':threept_pct,
    '2PT PCT':two_pct,
    'FGA': fgs_shot,
    '3PA':threes_shot,
    'FGA': fgs_shot,
    'FTA':fta,
    '3PA':threes_shot,
    '2PA':twos_shot,
    'FGM':fgm,
    'FTM':ftm,
    '2PM':twosm,
    '3PM':threesm}, {'Season': 'Playoffs',
    'Mins': mins2,
    'PPG': points2,
    'APG': assists2,
    'RPG': rebounds2,
    'STL': steals2,
    'BLK': blocks2,
    'TOV': turnovers2,
    'FG PCT': fg_pct2,
    'FT PCT': ft_pct2,
    '3PT PCT':threept_pct2,
    '2PT PCT':two_pct2,
    'FGA': fgs_shot2,
    'FTA':fta2,
    '3PA':threes_shot2,
    '2PA':twos_shot2,
    'FGM':fgm2,
    'FTM':ftm2,
    '2PM':twosm2,
    '3PM':threesm2}]
reg_playoffs_df = pd.DataFrame(stats_dict)
rounded_points = round(df4['PTS']/df4['GP'], 1)
df4['PPG'] = rounded_points
rounded_rebounds = round(df4['REB']/df4['GP'], 1)
df4['RPG'] = rounded_rebounds
rounded_assists = round(df4['AST']/df4['GP'], 1)
df4['APG'] = rounded_assists

# By Year Playoff Stats
df5 = career.get_data_frames()[2]
df5.rename(columns={'TEAM_ABBREVIATION': 'TEAM'}, inplace=True)
df5.rename(columns={'PLAYER_AGE': 'AGE'}, inplace=True)
df5.rename(columns={'SEASON_ID': 'YEAR'}, inplace=True)
year_stats = df5.groupby('YEAR').sum().reset_index()
year_stats['MIN'] = year_stats['MIN'] / year_stats['GP']
year_stats['PPG'] = year_stats['PTS'] / year_stats['GP']
year_stats['APG'] = year_stats['AST'] / year_stats['GP']
year_stats['RPG'] = year_stats['REB'] / year_stats['GP']
year_stats['SPG'] = year_stats['STL'] / year_stats['GP']
year_stats['BPG'] = year_stats['BLK'] / year_stats['GP']
year_stats['TOV'] = year_stats['TOV'] / year_stats['GP']
year_stats['FGA'] = year_stats['FGA'] / year_stats['GP']
year_stats['FGM'] = year_stats['FGM'] / year_stats['GP']
year_stats['FG3A'] = year_stats['FG3A'] / year_stats['GP']
year_stats['FG3M'] = year_stats['FG3M'] / year_stats['GP']
year_stats['FTA'] = year_stats['FTA'] / year_stats['GP']
year_stats['FTM'] = year_stats['FTM'] / year_stats['GP']
year_stats['2PA'] = year_stats['FGA'] - year_stats['FG3A']
year_stats['2PM'] = year_stats['FGM'] - year_stats['FG3M']
year_stats['2PT_PCT'] = year_stats['2PM'] / year_stats['2PA']
year_stats[['MIN', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'TOV', 'FG3M', 'FG3A', 'FGA', 'FGM', 'FTA', 'FTM', '2PA', '2PM']] = year_stats[['MIN', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'TOV', 'FG3M', 'FG3A', 'FGA', 'FGM', 'FTA', 'FTM', '2PA', '2PM']].round(1)
year_stats[['FG_PCT', 'FG3_PCT', 'FT_PCT', '2PT_PCT']] = year_stats[['FG_PCT', 'FG3_PCT', 'FT_PCT', '2PT_PCT']].round(3)
year_stats2 = year_stats[['YEAR', 'MIN', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'TOV', 'FG3M', 'FG3A', 'FGA', 'FGM', 'FTA', 'FTM', '2PA', '2PM', 'FG_PCT', 'FG3_PCT', 'FT_PCT', '2PT_PCT']]
# Stats by Year Regular Season
df6 = career.get_data_frames()[0]
df6 = df6.drop([df6.index[10], df6.index[12],df6.index[14],df6.index[15]])
df6.rename(columns={'TEAM_ABBREVIATION': 'TEAM'}, inplace=True)
df6.rename(columns={'PLAYER_AGE': 'AGE'}, inplace=True)
df6.rename(columns={'SEASON_ID': 'YEAR'},inplace=True)
year_stats3 = df6.groupby('YEAR').sum().reset_index()
year_stats3['MIN'] = year_stats3['MIN'] / year_stats3['GP']
year_stats3['PPG'] = year_stats3['PTS'] / year_stats3['GP']
year_stats3['APG'] = year_stats3['AST'] / year_stats3['GP']
year_stats3['RPG'] = year_stats3['REB'] / year_stats3['GP']
year_stats3['SPG'] = year_stats3['STL'] / year_stats3['GP']
year_stats3['BPG'] = year_stats3['BLK'] / year_stats3['GP']
year_stats3['TOV'] = year_stats3['TOV'] / year_stats3['GP']
year_stats3['FGA'] = year_stats3['FGA'] / year_stats3['GP']
year_stats3['FGM'] = year_stats3['FGM'] / year_stats3['GP']
year_stats3['FG3A'] = year_stats3['FG3A'] / year_stats3['GP']
year_stats3['FG3M'] = year_stats3['FG3M'] / year_stats3['GP']
year_stats3['FTA'] = year_stats3['FTA'] / year_stats3['GP']
year_stats3['FTM'] = year_stats3['FTM'] / year_stats3['GP']
year_stats3['2PA'] = year_stats3['FGA'] - year_stats3['FG3A']
year_stats3['2PM'] = year_stats3['FGM'] - year_stats3['FG3M']
year_stats3['2PT_PCT'] = year_stats3['2PM'] / year_stats3['2PA']
year_stats3[['MIN', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'TOV', 'FG3M', 'FG3A', 'FGA', 'FGM', 'FTA', 'FTM', '2PA', '2PM']] = year_stats3[['MIN', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'TOV', 'FG3M', 'FG3A', 'FGA', 'FGM', 'FTA', 'FTM', '2PA', '2PM']].round(1)
year_stats3[['FG_PCT', 'FG3_PCT', 'FT_PCT', '2PT_PCT']] = year_stats3[['FG_PCT', 'FG3_PCT', 'FT_PCT', '2PT_PCT']].round(3)
year_stats4 = year_stats3[['YEAR', 'MIN', 'PPG', 'APG', 'RPG', 'SPG', 'BPG', 'TOV', 'FG3M', 'FG3A', 'FGA', 'FGM', 'FTA', 'FTM', '2PA', '2PM', 'FG_PCT', 'FG3_PCT', 'FT_PCT', '2PT_PCT']]

output_file = 'harden_stats.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    reg_playoffs_df.to_excel(writer, sheet_name='Reg VS Playoffs', index=False)
    matchup_stats.to_excel(writer,sheet_name='Stats by Opponent 2023-2024' ,index=False)
    loc_stats.to_excel(writer, sheet_name='Stats By Location 2023-2024', index=False)
    average_stats.to_excel(writer, sheet_name='Stats by WL 2023-2024', index=False)
    year_stats2.to_excel(writer, sheet_name='Stats By Year Playoffs', index=False)
    year_stats4.to_excel(writer, sheet_name='Stats By Year Regular Season', index=False)
# Shot Chart Diagrams
shot_chart_detail = shotchartdetail.ShotChartDetail(
        team_id = 0, 
        player_id = 201935, 
        context_measure_simple = 'FGA', 
        season_nullable = '2023-24',
        season_type_all_star = 'Regular Season')

shot_chart_df = shot_chart_detail.get_data_frames()[0]
# Function to draw the basketball court to plot shots
def draw_court(ax=None, color='black', lw=2):
    if ax is None:
        ax = plt.gca()
    # Create the basketball hoop
    hoop = plt.Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
    # Create backboard
    backboard = plt.Rectangle((-30, -7.5), 60, 1, linewidth=lw, color=color)
    # Create the paint
    outer_box = plt.Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    inner_box = plt.Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False)
    # Create free throw top arc
    top_free_throw = patches.Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=lw, color=color)
    # Create free throw bottom arc
    bottom_free_throw = patches.Arc((0, 142.5), 120, 120, theta1=180, theta2=360, linewidth=lw, color=color, linestyle='dashed')
    # Create restricted zone
    restricted = plt.Circle((0, 0), radius=40, linewidth=lw, color=color, fill=False)
    # Three point line
    corner_three_a = plt.Line2D([-220, -220], [-47.5, 92.5], linewidth=lw, color=color)
    corner_three_b = plt.Line2D([220, 220], [-47.5, 92.5], linewidth=lw, color=color)
    three_arc = patches.Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)
    # Center court
    center_outer = plt.Circle((0, 422.5), radius=60, linewidth=lw, color=color, fill=False)
    center_inner = plt.Circle((0, 422.5), radius=20, linewidth=lw, color=color, fill=False)
    # List of court elements to be plotted
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw, bottom_free_throw,
                      restricted, three_arc, center_outer, center_inner]
    # Add court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)
    # Add lines for the three point line
    ax.add_line(corner_three_a)
    ax.add_line(corner_three_b)    
    return ax
sns.scatterplot(
    data=shot_chart_df,
    x='LOC_X',
    y='LOC_Y',
    hue='EVENT_TYPE',
    palette={'Made Shot': 'green', 'Missed Shot': 'red'},
    alpha=0.6,
    edgecolor='w',
    linewidth=0.5
)
draw_court(plt.gca())
plt.xlim(-250, 250)
plt.ylim(-47.5, 422.5)
plt.xticks([])
plt.yticks([])
plt.xlabel('')
plt.ylabel('')
plt.title('Harden Shot Chart for 2023-2024')
plt.show()

shot_chart_details = shotchartdetail.ShotChartDetail(
        team_id = 0,
        player_id = 201935, 
        context_measure_simple = 'FGA', 
        season_nullable = '2017-18',
        season_type_all_star = 'Regular Season')

shot_chart_df2 = shot_chart_details.get_data_frames()[0]
sns.scatterplot(
    data=shot_chart_df2,
    x='LOC_X',
    y='LOC_Y',
    hue='EVENT_TYPE',
    palette={'Made Shot': 'green', 'Missed Shot': 'red'},
    alpha=0.6,
    edgecolor='w',
    linewidth=0.5
)
draw_court(plt.gca())
plt.xlim(-250, 250)
plt.ylim(-47.5, 422.5)
plt.xticks([])
plt.yticks([])
plt.xlabel('')
plt.ylabel('')
plt.title('Harden Shot Chart for 2017-2018(MVP)')
plt.show()