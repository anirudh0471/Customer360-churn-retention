-- Query 1: Count all customers
SELECT COUNT(*)
FROM customers;

-- Query 2: Count customers who stayed and left
SELECT
    Churn,
    COUNT(*) AS CustomerCount
FROM customers
GROUP BY Churn;

--Query 3: Calculate overall churn rate
SELECT
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS ChurnRatePercent
FROM customers;

--Query 4: Find churn rates by contract type
SELECT
    Contract,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS ChurnRatePercent
FROM customers
GROUP BY Contract
ORDER BY ChurnRatePercent DESC;

--Query 5: Calculate churn by payment method
SELECT
    PaymentMethod,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS ChurnRatePercent
FROM customers
GROUP BY PaymentMethod
ORDER BY ChurnRatePercent DESC;