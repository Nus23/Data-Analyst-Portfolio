# Sales Dashboard | Power BI Project

## Project Overview

This Power BI project analyses sales performance using a retail sales dataset. The dashboard provides clear insights into sales, profit, orders, customer segments, product categories, regional performance, and monthly trends.

The aim of this project is to demonstrate practical data analyst skills, including data cleaning, data modelling, DAX measure creation, KPI reporting, dashboard design, and business insight generation.

## Business Objective

The objective of this dashboard is to help a business understand:

* Overall sales and profit performance
* Monthly sales trends
* Best-performing products and categories
* Regional sales and profitability
* Customer segment performance
* Areas where sales are high but profit is low
* Operational patterns such as delivery time

## Dataset

The project uses a retail sales dataset containing order-level sales records.

Example fields include:

* Order ID
* Order Date
* Ship Date
* Customer Name
* Segment
* Region
* Category
* Sub-Category
* Product Name
* Sales
* Quantity
* Discount
* Profit

## Tools Used

* Power BI Desktop
* Power Query
* DAX
* Microsoft Excel / CSV
* GitHub

## Data Cleaning and Preparation

The dataset was cleaned and prepared in Power Query. Key steps included:

* Checking and correcting data types
* Formatting date columns
* Removing unnecessary columns
* Checking missing values
* Creating a delivery time column
* Preparing the data model for analysis
* Creating a separate Date Table for time-based analysis

## Data Model

A Date Table was created and connected to the main sales table using the Order Date field. This enabled monthly, yearly, and time-based sales analysis.

## Key DAX Measures

The following DAX measures were created:

```DAX
Total Sales = SUM(Orders[Sales])
```

```DAX
Total Profit = SUM(Orders[Profit])
```

```DAX
Total Orders = DISTINCTCOUNT(Orders[Order ID])
```

```DAX
Total Quantity = SUM(Orders[Quantity])
```

```DAX
Profit Margin = DIVIDE([Total Profit], [Total Sales], 0)
```

```DAX
Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
```

```DAX
Average Delivery Days = AVERAGE(Orders[Delivery Days])
```

## Dashboard Pages

### 1. Executive Sales Overview

This page provides a high-level summary of business performance using KPI cards and main trend visuals.

Key visuals:

* Total Sales
* Total Profit
* Total Orders
* Profit Margin
* Monthly Sales Trend
* Sales by Region
* Sales by Category
* Top Products by Sales

### 2. Product Performance

This page analyses product categories, sub-categories, and individual product performance.

Key visuals:

* Sales by Category
* Profit by Category
* Sales by Sub-Category
* Profit by Sub-Category
* Top 10 Products by Sales
* Bottom 10 Products by Profit

### 3. Regional Sales Analysis

This page compares sales and profit performance across regions and locations.

Key visuals:

* Sales by Region
* Profit by Region
* Orders by Region
* Profit Margin by Region
* Sales by State or City

### 4. Customer Segment Analysis

This page analyses sales and profitability by customer segment.

Key visuals:

* Sales by Segment
* Profit by Segment
* Orders by Segment
* Average Order Value by Segment
* Monthly Sales by Segment

## Key Insights

The dashboard can be used to answer business questions such as:

1. Which region generates the highest sales?
2. Which product categories are most profitable?
3. Which products have high sales but low profit?
4. Which customer segment contributes the most revenue?
5. How do sales change over time?
6. Are there any seasonal sales patterns?
7. How does delivery time vary across orders?

## Skills Demonstrated

This project demonstrates the following data analyst skills:

* Power BI dashboard development
* Power Query data cleaning
* DAX measure creation
* Data modelling
* KPI reporting
* Sales and profit analysis
* Business intelligence reporting
* Data visualisation
* Insight generation
* GitHub project documentation

## Project Files

```text
Sales-Dashboard/
│
├── README.md
├── data/
│   └── superstore_sales.csv
│
├── powerbi/
│   └── Sales_Dashboard.pbix
│
├── images/
│   ├── dashboard_overview.png
│   ├── sales_trend.png
│   └── profit_analysis.png
│
└── notes/
    └── insights.md
```

## Dashboard Preview

Screenshots of the dashboard will be added after the Power BI report is completed.

Example screenshots to include:

* Executive Sales Overview
* Product Performance
* Regional Sales Analysis
* Customer Segment Analysis

## Conclusion

This project demonstrates how Power BI can be used to transform raw sales data into meaningful business insights. The dashboard helps users monitor sales performance, identify profitable areas, understand customer behaviour, and support data-driven decision-making.
