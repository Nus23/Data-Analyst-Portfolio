import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nContent Types:")
print(df["type"].value_counts())

print("\nTop 10 Countries:")
print(df["country"].value_counts().head(10))

print("\nRatings:")
print(df["rating"].value_counts())

print("\nMost Recent Release Year:")
print(df["release_year"].max())