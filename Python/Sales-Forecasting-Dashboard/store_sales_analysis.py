import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv(r"E:\Data-Portfolio\Sales-Forecasting-Dashboard\data\train.csv")

store_sales = (
    train.groupby("Store")["Weekly_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(store_sales)

plt.figure(figsize=(10,6))
store_sales.plot(kind="bar")

plt.title("Top 10 Stores by Total Sales")
plt.xlabel("Store")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(r"E:\Data-Portfolio\Sales-Forecasting-Dashboard\images\top_10_stores_sales.png")
plt.show()