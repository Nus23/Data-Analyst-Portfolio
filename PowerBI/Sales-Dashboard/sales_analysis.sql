-- View all sales
SELECT * FROM customer_sales;

-- Total sales by category
SELECT
    Category,
    SUM(Quantity * Price) AS TotalSales
FROM customer_sales
GROUP BY Category;

-- Top selling products
SELECT
    Product,
    SUM(Quantity) AS TotalQuantity
FROM customer_sales
GROUP BY Product
ORDER BY TotalQuantity DESC;

-- Average product price
SELECT
    AVG(Price) AS AveragePrice
FROM customer_sales;

-- Highest revenue product
SELECT
    Product,
    SUM(Quantity * Price) AS Revenue
FROM customer_sales
GROUP BY Product
ORDER BY Revenue DESC;