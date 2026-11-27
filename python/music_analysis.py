import pandas as pd

data = pd.read_csv("../data/Spotify Dataset.csv")

print("Dataset Information")
print(data.head())

print("\n")

print("Total Records :", len(data))

print("\nTop 10 Artists")

top_artists = data["Artist"].value_counts().head(10)

print(top_artists)

print("\nGenre Distribution")

top_genres = data["Genre"].value_counts().head(10)

print(top_genres)