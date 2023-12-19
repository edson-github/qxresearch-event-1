import secrets

number_list = [secrets.randbelow(10000) + 1 for _ in range(10)]
print(number_list)