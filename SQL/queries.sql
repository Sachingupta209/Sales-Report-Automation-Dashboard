SELECT ROUND(SUM(sales),2) AS Total_Sales
FROM sales;
SELECT ROUND(SUM(profit),2) AS Total_Profit
FROM sales;
SELECT COUNT(*) AS Total_Orders
FROM sales;
SELECT
    category,
    ROUND(SUM(sales),2) AS Total_Sales
FROM sales
GROUP BY category
ORDER BY Total_Sales DESC;
SELECT
    region,
    ROUND(SUM(sales),2) AS Total_Sales
FROM sales
GROUP BY region
ORDER BY Total_Sales DESC;
SELECT
    region,
    ROUND(SUM(profit),2) AS Total_Profit
FROM sales
GROUP BY region
ORDER BY Total_Profit DESC;
SELECT
    customer_name,
    ROUND(SUM(sales),2) AS Total_Sales
FROM sales
GROUP BY customer_name
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT
    product_name,
    ROUND(SUM(sales),2) AS Total_Sales
FROM sales
GROUP BY product_name
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT
    payment_mode,
    COUNT(*) AS Total_Orders
FROM sales
GROUP BY payment_mode
ORDER BY Total_Orders DESC;
SELECT
ROUND(AVG(sales),2) AS Average_Order_Value
FROM sales;