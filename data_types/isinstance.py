# Integer = False

account_balance = '12'

print(isinstance(account_balance, int))

# Integer = True

account_balance = 12

print(isinstance(account_balance, int))

# Integer / Float = True

account_balance = 12

print(isinstance(account_balance, (int, float)))