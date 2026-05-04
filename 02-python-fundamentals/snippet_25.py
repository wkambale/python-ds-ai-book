# Simulate a mobile money account balance
balance = 50000
withdrawal_amount = 12000
transaction_fee = 500
transaction_count = 0

# Keep making withdrawals as long as the balance can cover it
while balance >= (withdrawal_amount + transaction_fee):
    balance = balance - (withdrawal_amount + transaction_fee)
    transaction_count += 1
    print(f"Withdrawal {transaction_count} successful. New balance: {balance}")

print(f"\nLoop finished after {transaction_count} transactions.")
print("Insufficient funds for another withdrawal.")