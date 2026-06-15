import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load data
train = pd.read_csv(r"E:\Data-Portfolio\Sales-Forecasting-Dashboard\data\train.csv")

# Convert date
train["Date"] = pd.to_datetime(train["Date"])

# Create date features
train["Year"] = train["Date"].dt.year
train["Month"] = train["Date"].dt.month
train["Week"] = train["Date"].dt.isocalendar().week.astype(int)

# Features
X = train[["Store", "Dept", "Year", "Month", "Week"]]

# Target
y = train["Weekly_Sales"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", round(mae, 2))
import matplotlib.pyplot as plt

comparison = pd.DataFrame({
    "Actual": y_test.values[:100],
    "Predicted": predictions[:100]
})

plt.figure(figsize=(12,6))
plt.plot(comparison["Actual"].values, label="Actual Sales")
plt.plot(comparison["Predicted"].values, label="Predicted Sales")

plt.title("Actual vs Predicted Weekly Sales")
plt.xlabel("Sample")
plt.ylabel("Weekly Sales")
plt.legend()

plt.tight_layout()
plt.savefig(r"E:\Data-Portfolio\Sales-Forecasting-Dashboard\images\actual_vs_predicted_sales.png")
plt.show()