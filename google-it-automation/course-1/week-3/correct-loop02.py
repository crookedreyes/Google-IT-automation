# Correct infinite loop
def print_range(start, end):
    # loop through the numbers start to end
    n = start
    while n <= end:
        print(n)
        # variable control missing
        n = n + 1

print_range(1,5) # Should print 1 2 3 4 5 (each number in is's own line)
