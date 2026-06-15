import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\Data-Portfolio\Customer-Churn-Prediction\data\WA_Fn-UseC_-Telco-Customer-Churn.csv")

payment_churn = pd.crosstab(df["PaymentMethod"], df["Churn"])

print(payment_churn)

payment_churn.plot(kind="bar", figsize=(10,6))

plt.title("Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(r"E:\Data-Portfolio\Customer-Churn-Prediction\Image\payment_method_churn.png")

plt.show()