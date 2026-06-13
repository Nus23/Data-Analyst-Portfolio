import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic-Dataset.csv")

gender_counts = df["Sex"].value_counts()

gender_counts.plot(kind="bar")

plt.title("Passengers by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.xticks(rotation=0)

plt.savefig("passengers_by_gender.png", bbox_inches="tight")
plt.show()