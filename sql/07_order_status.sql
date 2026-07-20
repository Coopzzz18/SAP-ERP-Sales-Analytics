SELECT
    OrderStatus,
    COUNT(*) AS Orders,
    ROUND(SUM(NetRevenue),2) AS Revenue
FROM sales_orders
GROUP BY OrderStatus
ORDER BY Revenue DESC;