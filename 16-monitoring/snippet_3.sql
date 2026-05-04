-- Predict churn for new customers
SELECT
    customer_id,
    predicted_churned,
    predicted_churned_probs[OFFSET(1)].prob AS churn_probability
FROM
    ML.PREDICT(MODEL `mobicash_analytics.churn_model_v1`,
    (
        SELECT
            customer_id,
            age,
            account_balance,
            avg_transaction_amount,
            days_since_last_transaction,
            total_transactions_last_month,
            location
        FROM
            `mobicash_analytics.active_customers`
    ))
WHERE
    predicted_churned_probs[OFFSET(1)].prob > 0.5
ORDER BY
    churn_probability DESC