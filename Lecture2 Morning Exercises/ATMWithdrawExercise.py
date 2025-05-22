account_balance = 130000  

withdraw_amount = int(input("Enter amount to withdraw: "))

if withdraw_amount <= account_balance:
    account_balance -= withdraw_amount
    print(f"Withdrawal successful. Remaining balance: Shs.{account_balance:}")
else:
    print("Insufficient funds. Withdrawal denied.")
