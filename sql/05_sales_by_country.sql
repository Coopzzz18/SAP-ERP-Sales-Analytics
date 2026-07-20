SELECT
    c.Country,
    ROUND(SUM(s.NetRevenue),2) AS Revenue,
    SUM(s.Quantity) AS UnitsSold,
    COUNT(DISTINCT s.SalesOrderID) AS Orders
FROM sales_orders s
JOIN customers c
    ON s.CustomerID = c.CustomerID
WHERE s.OrderStatus <> 'Cancelled'
GROUP BY c.Country
ORDER BY Revenue DESC
LIMIT 15;