-- Export high-risk customers to a table for the retention team
CREATE OR REPLACE TABLE `mobicash_analytics.high_risk_customers` AS
SELECT
    customer_id,
    churn_probability,
    CASE
        WHEN churn_probability > 0.7 THEN 'High'
        WHEN churn_probability > 0.4 THEN 'Medium'
        ELSE 'Low'
    END AS risk_level,
    CURRENT_TIMESTAMP() AS prediction_timestamp
FROM (
    SELECT
        customer_id,
        predicted_churned_probs[OFFSET(1)].prob AS churn_probability
    FROM
        ML.PREDICT(MODEL `mobicash_analytics.churn_model_v1`,
        (SELECT * FROM `mobicash_analytics.active_customers`))
)
WHERE churn_probability > 0.4