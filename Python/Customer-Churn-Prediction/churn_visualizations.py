import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Count churn values
churn_counts = df["Churn"].value_counts()

# Create chart
plt.figure(figsize=(6,4))
churn_counts.plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.tight_layout()

# Save chart
plt.savefig("images/churn_distribution.png")

# Show chart
plt.show()