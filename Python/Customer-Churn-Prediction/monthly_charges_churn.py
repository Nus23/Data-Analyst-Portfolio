import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\Data-Portfolio\Customer-Churn-Prediction\data\WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Convert if needed
df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"])

# Plot
plt.figure(figsize=(8,5))

plt.hist(
    [df[df["Churn"]=="No"]["MonthlyCharges"],
     df[df["Churn"]=="Yes"]["MonthlyCharges"]],
    bins=20,
    label=["Stayed","Churned"]
)

plt.title("Monthly Charges vs Churn")
plt.xlabel("Monthly Charges")
plt.ylabel("Customers")

plt.legend()

plt.tight_layout()

plt.savefig(r"E:\Data-Portfolio\Customer-Churn-Prediction\images\monthly_charges_churn.png")

plt.show()