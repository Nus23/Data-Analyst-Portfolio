import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_excel("data/Online Retail.xlsx")

# Clean data
df = df.dropna(subset=["CustomerID"])
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# Create sales amount
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# Convert date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Snapshot date
snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# RFM Table
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalAmount": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

# Scale data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

print(rfm.head())

print("\nCluster Counts:")
print(rfm["Cluster"].value_counts())
import matplotlib.pyplot as plt

plt.figure(figsize=(12,7))

plt.scatter(
    rfm["Frequency"],
    rfm["Monetary"],
    c=rfm["Cluster"],
    alpha=0.6
)

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Purchase Frequency")
plt.ylabel("Total Spending (£)")
plt.grid(True)

plt.savefig("images/customer_segments.png")
plt.show()
print("\nCluster Summary")
print(
    rfm.groupby("Cluster")
    .agg({
        "Recency":"mean",
        "Frequency":"mean",
        "Monetary":"mean"
    })
)
dir
