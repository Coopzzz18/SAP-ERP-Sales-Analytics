SELECT
    strftime('%Y-%m', OrderDate) AS Month,
    ROUND(SUM(NetRevenue), 2) AS Revenue,
    COUNT(DISTINCT SalesOrderID) AS Orders
FROM sales_orders
GROUP BY strftime('%Y-%m', OrderDate)
ORDER BY Month;