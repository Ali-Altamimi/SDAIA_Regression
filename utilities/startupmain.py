from VGChartz import get_games_data


df = get_games_data()
df.to_csv('F:\Books\T10\sdaia t5\MTA Project\SDAIA_Regression\data\vgchartz_games.csv')