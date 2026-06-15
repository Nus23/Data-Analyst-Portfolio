# Sales Performance Dashboard | Power BI Project

## Project Overview

This Power BI project analyses retail sales performance using a Superstore sales dataset. The dashboard provides a clear overview of sales, orders, customers, average order value, delivery time, regional performance, product categories, and monthly sales trends.

This project was created as part of my Data Analyst portfolio to demonstrate practical Power BI skills, including data import, data cleaning, data modelling, DAX measure creation, dashboard design, and business insight generation.

## Business Objective

The objective of this dashboard is to help a business understand sales performance and answer key questions such as:

* What is the total sales performance?
* How many orders and customers are included in the dataset?
* Which region generates the highest sales?
* Which product categories contribute most to sales?
* What are the top-selling products?
* How does sales performance change over time?
* What is the average order value?
* What is the average delivery time?

## Dataset

The dataset used for this project is a Superstore sales dataset.

The dataset includes order-level sales records with fields such as:

* Order ID
* Order Date
* Ship Date
* Ship Mode
* Customer ID
* Customer Name
* Segment
* Country
* City
* State
* Region
* Product ID
* Category
* Sub-Category
* Product Name
* Sales
* Quantity
* Discount

Note: The version of the dataset used in this project did not include a Profit column, so the dashboard focuses on sales performance rather than profitability analysis.

## Tools Used

* Power BI Desktop
* Power Query
* DAX
* CSV dataset
* GitHub

## Data Cleaning and Preparation

The dataset was cleaned and prepared in Power Query before building the dashboard.

Key cleaning steps included:

* Imported the CSV file into Power BI
* Renamed the main query/table to Orders
* Checked and corrected data types
* Set Order Date and Ship Date as Date fields
* Set Sales as a decimal number
* Removed unnecessary columns such as Row ID and Postal Code
* Created a new Delivery Days column using Ship Date and Order Date
* Loaded the cleaned data into Power BI

## Data Model

A separate Date Table was created using DAX to support time-based analysis.

The Date Table includes:

* Date
* Year
* Month Number
* Month Name
* Year Month

A relationship was created between:

Date Table[Date] and Orders[Order Date]

This allows the dashboard to analyse sales by month and year.

## DAX Measures

The following DAX measures were created for the dashboard:

```DAX
Total Sales = SUM('Orders'[Sales])
```

```DAX
Total Orders = DISTINCTCOUNT('Orders'[Order ID])
```

```DAX
Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
```

```DAX
Average Delivery Days = AVERAGE('Orders'[Delivery Days])
```

```DAX
Total Customers = DISTINCTCOUNT('Orders'[Customer ID])
```

## Dashboard Features

The dashboard includes the following KPI cards:

* Total Sales
* Total Orders
* Total Customers
* Average Delivery Days
* Average Order Value

The dashboard also includes the following visuals:

* Monthly Sales Trend
* Sales by Region
* Sales by Category
* Top 10 Products by Sales

Interactive slicers were added for:

* Year
* Region
* Category

## Key Insights

The dashboard shows the following insights:

1. Total sales are approximately $2.26M across the dataset.
2. The dataset includes around 5K orders and 793 customers.
3. The West region generated the highest sales compared with other regions.
4. Technology, Furniture, and Office Supplies are the main product categories.
5. The dashboard highlights the top 10 products by sales.
6. Monthly sales trends help identify changes in sales performance over time.
7. Slicers allow users to filter the dashboard by Year, Region, and Category.

## Project Folder Structure

```text
Sales-Dashboard
│
├── README.md
├── data
│   └── superstore_sales.csv
│
├── powerbi
│   └── Sales_Dashboard.pbix
│
├── images
│   └── dashboard_overview.png
│
└── notes
    └── insights.md
```

## Dashboard Preview

![Sales Dashboard Overview](images/dashboard_overview.png)
<img width="972" height="542" alt="image" src="https://github.com/user-attachments/assets/0a67f2af-c3b9-45c1-8fb2-088c2dd0003e" />

## Skills Demonstrated

This project demonstrates the following skills:

* Power BI dashboard development
* Data cleaning using Power Query
* Data modelling
* Creating a Date Table
* Building relationships between tables
* Writing DAX measures
* Creating KPI cards
* Creating interactive charts
* Using slicers for dashboard filtering
* Sales analysis
* Business intelligence reporting
* GitHub project documentation

## Conclusion

This Power BI Sales Performance Dashboard transforms raw sales data into meaningful business insights. The dashboard allows users to monitor sales trends, compare regional performance, identify top product categories, and understand key sales metrics through a clean and interactive report.
