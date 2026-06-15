import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"E:\Data-Portfolio\Customer-Churn-Prediction\data\WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Group data
contract_churn = pd.crosstab(df["Contract"], df["Churn"])

print(contract_churn)

# Plot
contract_churn.plot(kind="bar", figsize=(8,5))

plt.title("Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(r"E:\Data-Portfolio\Customer-Churn-Prediction\Image\contract_churn.png")

plt.show()