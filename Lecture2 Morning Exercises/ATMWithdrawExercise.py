# Use if-else statements to check the account balance before allowing withdrawal.
account_balance = 120000  # Initial balance
withdraw_amount = float(input("Enter the amount you want to withdraw: "))

if withdraw_amount <= account_balance:
    account_balance -= withdraw_amount
    print("Withdrawal successful! New balance:"+ {account_balance})
else:
    print("Insufficient balance. Transaction denied.")
