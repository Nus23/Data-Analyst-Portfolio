import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\Data-Portfolio\Customer-Churn-Prediction\data\WA_Fn-UseC_-Telco-Customer-Churn.csv")

plt.figure(figsize=(8,5))

plt.hist(
    [df[df["Churn"]=="No"]["tenure"],
     df[df["Churn"]=="Yes"]["tenure"]],
    bins=20,
    label=["Stayed","Churned"]
)

plt.title("Customer Tenure vs Churn")
plt.xlabel("Tenure (Months)")
plt.ylabel("Customers")

plt.legend()

plt.tight_layout()

plt.savefig(r"E:\Data-Portfolio\Customer-Churn-Prediction\images\tenure_churn.png")

plt.show()