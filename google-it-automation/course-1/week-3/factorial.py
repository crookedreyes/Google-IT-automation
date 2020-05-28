def factorial(n):
    result = 1
    for i in range(n):
        result = result * (n-i)
        #print(result)
    return result

print(factorial(4))

