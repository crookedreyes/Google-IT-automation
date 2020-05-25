def print_prime_factors(number):
    # Start with two, which is the first primer
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # check if the factor is a divisor of num
        if number % factor == 0:
            print(factor)
            number = number / factor
        else:
            # is it's not increment the factor by one
            factor = factor + 1
        return "Done"

print(print_prime_factors(100))
# this should print 2,2,5,5
#DO NOR DELETE THIS COMMENT
