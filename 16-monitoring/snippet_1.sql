-- Create a logistic regression model for churn prediction
CREATE OR REPLACE MODEL `mobicash_analytics.churn_model_v1`
OPTIONS(
    model_type='LOGISTIC_REG',
    input_label_cols=['churned'],
    auto_class_weights=TRUE,
    max_iterations=20,
    learn_rate_strategy='LINE_SEARCH'
) AS
SELECT
    churned,
    age,
    account_balance,
    avg_transaction_amount,
    days_since_last_transaction,
    total_transactions_last_month,
    location
FROM
    `mobicash_analytics.training_data`
WHERE
    -- Use 80% for training
    MOD(ABS(FARM_FINGERPRINT(CAST(customer_id AS STRING))), 10) < 8