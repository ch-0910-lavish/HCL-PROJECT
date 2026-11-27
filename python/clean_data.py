import pandas as pd

data = pd.read_csv("../data/Spotify Dataset.csv")

data.drop_duplicates(inplace=True)

data.fillna("Unknown", inplace=True)

print("Cleaned Dataset")

print(data.head())

print("\nTotal Records After Cleaning:", len(data))