def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

number = input("Enter a number\n")
print(number_group(int(number)))