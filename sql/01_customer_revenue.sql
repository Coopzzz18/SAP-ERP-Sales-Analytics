SELECT
    CustomerID,
    ROUND(SUM(NetRevenue),2) AS TotalRevenue,
    COUNT(SalesOrderID) AS Orders
FROM sales_orders
GROUP BY CustomerID
ORDER BY TotalRevenue DESC
LIMIT 10;