SELECT
    p.PlantName,
    p.Country,
    ROUND(SUM(s.NetRevenue),2) AS Revenue,
    SUM(s.Quantity) AS UnitsSold,
    COUNT(*) AS Orders
FROM sales_orders s
JOIN plants p
    ON s.PlantID = p.PlantID
GROUP BY
    p.PlantName,
    p.Country
ORDER BY Revenue DESC;