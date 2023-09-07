def factorial(num):
    if num < 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# tests
print(factorial(8))  # 40320
print(factorial(18))  # 6402373705728000
print(factorial(45))  # 119622220865480194561963161495657715064383733760000000000
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(-20))  # None
