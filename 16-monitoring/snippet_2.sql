-- Get model evaluation metrics
SELECT
    *
FROM
    ML.EVALUATE(MODEL `mobicash_analytics.churn_model_v1`,
    (
        SELECT * FROM `mobicash_analytics.training_data`
        WHERE MOD(ABS(FARM_FINGERPRINT(CAST(customer_id AS STRING))), 10) >= 8
    ))