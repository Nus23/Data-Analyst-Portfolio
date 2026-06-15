# Sales Forecasting Dashboard

## Project Overview

This project analyzes Walmart historical sales data and builds a machine learning forecasting model to predict future weekly sales. The objective is to identify sales trends, evaluate store performance, and generate business insights that support inventory planning and operational decision-making.

---

## Dataset

Walmart Store Sales Forecasting Dataset

Files used:

* train.csv
* test.csv
* stores.csv
* features.csv

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-Learn
* Random Forest Regressor
* VS Code
* GitHub

---

## Project Workflow

### 1. Data Preparation

* Loaded Walmart sales data
* Converted date fields to datetime format
* Created time-based features:

  * Year
  * Month
  * Week

### 2. Exploratory Data Analysis

Generated visualizations to identify:

* Weekly sales trends
* Seasonal sales peaks
* High-performing stores

### 3. Machine Learning Model

Model Used:

* Random Forest Regressor

Features:

* Store
* Department
* Year
* Month
* Week

Target:

* Weekly_Sales

### 4. Model Evaluation

Metric:

* Mean Absolute Error (MAE)

Result:

MAE = 1436.34

This indicates that the model's average prediction error is approximately £1,436 per weekly sales prediction.

---

## Visualizations

### Walmart Weekly Sales Trend

Shows weekly sales fluctuations and seasonal peaks.

![Sales Trend](images/sales_trend.png)

---

### Actual vs Predicted Weekly Sales

Compares model predictions with actual sales values.

![Actual vs Predicted](images/actual_vs_predicted_sales.png)

---

### Top 10 Stores by Total Sales

Highlights the highest-performing Walmart stores.

![Top Stores](images/top_10_stores_sales.png)

---

## Key Insights

* Strong seasonal sales spikes occur during holiday periods.
* Certain stores consistently outperform others.
* The Random Forest model captures overall sales patterns effectively.
* Forecasting can support staffing, inventory, and operational planning.
* Machine learning can improve business decision-making through predictive analytics.

---

## Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Feature Engineering
* Machine Learning
* Forecasting
* Business Analytics
* Python Programming
* GitHub Documentation

---

## Author

Nusrat Jahan Onia

MSc Data Science & Artificial Intelligence

GitHub:
https://github.com/Nus23
