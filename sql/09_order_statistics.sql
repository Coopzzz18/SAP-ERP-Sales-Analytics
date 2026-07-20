SELECT
    ROUND(AVG(NetRevenue),2) AS AverageOrderValue,
    ROUND(MAX(NetRevenue),2) AS LargestOrder,
    ROUND(MIN(NetRevenue),2) AS SmallestOrder
FROM sales_orders;