SELECT
    c.CustomerName,
    SUM(s.Quantity) AS UnitsSold,
    ROUND(SUM(s.NetRevenue),2) AS Revenue
FROM sales_orders s
JOIN customers c
    ON s.CustomerID = c.CustomerID
GROUP BY c.CustomerName
ORDER BY UnitsSold DESC
LIMIT 10;