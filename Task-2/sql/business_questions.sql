
-- 1. What is the total revenue?
SELECT ROUND(SUM(Total_Sales), 2) AS total_revenue
FROM sales;

-- 2. Which category generates the highest revenue?
SELECT Category,
       ROUND(SUM(Total_Sales), 2) AS revenue
FROM sales
GROUP BY Category
ORDER BY revenue DESC;

-- 3. Which city generates the highest revenue?
SELECT City,
       ROUND(SUM(Total_Sales), 2) AS revenue
FROM sales
GROUP BY City
ORDER BY revenue DESC;

-- 4. What are the top 5 best-selling products by quantity?
SELECT Product,
       SUM(Quantity) AS total_quantity
FROM sales
GROUP BY Product
ORDER BY total_quantity DESC
LIMIT 5;

-- 5. What is the monthly revenue?
SELECT strftime('%Y-%m', Order_Date) AS sales_month,
       ROUND(SUM(Total_Sales), 2) AS monthly_revenue
FROM sales
GROUP BY sales_month
ORDER BY sales_month;

-- 6. Which customers generate the highest revenue?
SELECT Customer_ID,
       Customer_Name,
       ROUND(SUM(Total_Sales), 2) AS customer_revenue
FROM sales
GROUP BY Customer_ID, Customer_Name
ORDER BY customer_revenue DESC
LIMIT 10;

-- 7. What is the average order value?
SELECT ROUND(AVG(order_revenue), 2) AS average_order_value
FROM (
    SELECT Order_ID, SUM(Total_Sales) AS order_revenue
    FROM sales
    GROUP BY Order_ID
);
