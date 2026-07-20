SELECT
    m.Category,
    ROUND(SUM(s.NetRevenue),2) AS Revenue,
    SUM(s.Quantity) AS UnitsSold,
    COUNT(*) AS Orders
FROM sales_orders s
JOIN materials m
    ON s.MaterialID = m.MaterialID
GROUP BY m.Category
ORDER BY Revenue DESC;
