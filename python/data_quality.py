import pandas as pd

data = pd.read_csv("../data/Spotify Dataset.csv")

print("Total Rows:", len(data))

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:")
print(data.duplicated().sum())