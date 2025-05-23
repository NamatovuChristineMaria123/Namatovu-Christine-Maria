def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result = result*i
    return result

print(factorial(5))  
