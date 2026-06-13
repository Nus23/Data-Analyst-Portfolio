import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSurvival Rate:")
print(df["Survived"].value_counts())

print("\nAverage Age:")
print(round(df["Age"].mean(), 2))

print("\nPassengers by Gender:")
print(df["Sex"].value_counts())