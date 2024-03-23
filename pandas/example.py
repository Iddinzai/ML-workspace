import pandas as pd
import numpy as np
players = pd.read_csv("players_22.csv")
players.head()
features = ["overall", "potential", "wage_eur", "value_eur", "age"]
players=players.dropna(subset=features)
data=players[features].copy()
#scale the data
#initialize random centroids
#label each data point
#update centroids
#repeat steps 3 and 4 until centroids stop changing
data = ((data - data.min()) / (data.max() - data.min())) * 10 + 1
data.describe()
data.head()
print(data)
