SELECT
    c.CustomerName,
    c.Country,
    ROUND(SUM(s.NetRevenue),2) AS TotalRevenue,
    COUNT(s.SalesOrderID) AS Orders
FROM sales_orders s
JOIN customers c
ON s.CustomerID = c.CustomerID
GROUP BY
    c.CustomerName,
    c.Country
ORDER BY TotalRevenue DESC
LIMIT 10;