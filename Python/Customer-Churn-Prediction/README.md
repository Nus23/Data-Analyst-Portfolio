# Customer Churn Analysis and Prediction

## GitHub Repository

Repository Link:
https://github.com/Nus23/Data-Analyst-Portfolio/tree/main/Python/Customer-Churn-Prediction
Customer Churn Analysis and Prediction
Project Overview
This project analyses customer churn behaviour using the IBM Telco Customer Churn dataset. The objective is to identify the key factors influencing customer attrition and provide business recommendations to improve customer retention.
The project includes exploratory data analysis (EDA), data visualisation, business insights, and a machine learning model to predict customer churn.
 
Business Problem
Customer churn is a major challenge for subscription-based businesses. Losing existing customers increases acquisition costs and reduces long-term profitability.
This project aims to answer:
•	Why are customers leaving?
•	Which customer groups are most at risk?
•	What actions can reduce churn?
•	Can customer churn be predicted using machine learning?
 
Tools and Technologies
•	Python
•	Pandas
•	Matplotlib
•	Scikit-learn
•	VS Code
•	GitHub
 
Dataset
Dataset: IBM Telco Customer Churn Dataset
Records: 7,043 Customers
Features: 21 Variables Target Variable:
• Churn (Yes / No)
 
Project Structure
Customer-Churn-Prediction
•	data/
•	WA_Fn-UseC_-Telco-Customer-Churn.csv
•	Image/
•	churn_distribution.png
•	contract_churn.png
•	payment_method_churn.png
•	monthly_charges_churn.png
•	tenure_churn.png
•	customer_churn_analysis.py
•	churn_visualizations.py
•	contract_churn.py
•	payment_method_churn.py
•	monthly_charges_churn.py
•	tenure_churn.py
•	churn_prediction_model.py
•	README.md
 
Exploratory Data Analysis
1. Customer Churn Distribution
Findings:
•	Total Customers: 7,043
•	Customers Retained: 5,174
•	Customers Churned: 1,869 Insight:
Approximately 27% of customers left the company.
Business Recommendation:
Implement customer retention programmes targeting at-risk customers.
 
2. Contract Type Analysis Findings:
	Contract Type	Retained	Churned
Month-to-month	2220	1655
One year	1307	166
Two year	1647	48
Insight:
Month-to-month customers experience significantly higher churn compared with annual contracts.
Business Recommendation:
Encourage customers to move to longer-term contracts through loyalty incentives and discounted plans.
 
3. Payment Method Analysis
Insight:
Customers using Electronic Check payment methods showed substantially higher churn rates than customers using automatic payment methods.
Business Recommendation:
Promote automatic payments through incentives and discounts.
 
4. Monthly Charges Analysis
Insight:
Customers with higher monthly charges demonstrated a greater tendency to churn.
Business Recommendation:
Provide retention offers and loyalty rewards to high-value customers.
 
5. Customer Tenure Analysis
Insight:
Customers with short tenure are more likely to leave, while long-term customers show significantly lower churn rates.
Business Recommendation:
Focus retention efforts during the first year of the customer lifecycle.
 
Machine Learning Model
Model:
• Logistic Regression Steps:
1.	Data Cleaning
2.	Missing Value Handling
3.	Label Encoding
4.	Train-Test Split
5.	Model Training
6.	Model Evaluation Performance:
• Accuracy: 82.19%
 
Key Business Insights
1.	Month-to-month contracts have the highest churn risk.
2.	Electronic Check users are more likely to leave.
3.	Higher monthly charges increase churn probability.
4.	New customers are at the greatest risk of churn.
5.	Long-term customers are significantly more loyal.
 
Future Improvements
•	Random Forest Classifier
•	XGBoost Model
•	Feature Importance Analysis
•	Confusion Matrix Visualisation
•	Interactive Power BI Dashboard
•	Customer Churn Risk Scoring
 
Author
Nusrat Jahan Onia
MSc Data Science and Artificial Intelligence
University of Suffolk
GitHub Portfolio Project 2026

