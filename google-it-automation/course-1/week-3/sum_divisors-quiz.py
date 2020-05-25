def sum_divisors(n):
    sum = 0
    #return the sum of all devisors of n, not including n
    while n >= 0:
        n = n - 2
        print(n)
    return sum

print(sum_divisors(0))
# 0
print(sum_divisors(2)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


