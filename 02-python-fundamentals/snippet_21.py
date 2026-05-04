# A script to check eligibility for a micro-loan
credit_score = 650
has_stable_income = True
outstanding_debt_ratio = 0.45  # 45%

if credit_score >= 700 and has_stable_income and outstanding_debt_ratio < 0.4:
    print("Congratulations! You are approved for our premium loan product.")
elif credit_score >= 600 and has_stable_income and outstanding_debt_ratio < 0.5:
    print("You are approved for our standard loan product.")
elif credit_score >= 550 and has_stable_income:
    print("You may be eligible for a starter loan with a co-signer.")
else:
    print("We are sorry, but we cannot approve a loan at this time.")
    print("Please work on improving your credit score and reducing existing debt.")