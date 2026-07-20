SELECT
    m.MaterialID,
    m.MaterialName,
    m.Category,
    SUM(s.Quantity) AS UnitsSold,
    ROUND(SUM(s.NetRevenue), 2) AS TotalRevenue,
    COUNT(DISTINCT s.SalesOrderID) AS Orders
FROM sales_orders s
JOIN materials m
    ON s.MaterialID = m.MaterialID
WHERE s.OrderStatus <> 'Cancelled'
GROUP BY
    m.MaterialID,
    m.MaterialName,
    m.Category
ORDER BY TotalRevenue DESC
LIMIT 10;