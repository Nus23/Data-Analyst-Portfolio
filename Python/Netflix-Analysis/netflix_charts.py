import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

content_counts = df["type"].value_counts()

content_counts.plot(kind="bar")

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.savefig("netflix_content_types.png", bbox_inches="tight")

plt.show()