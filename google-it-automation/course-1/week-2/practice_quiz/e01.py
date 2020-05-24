# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    km = miles * 1.6 # aprox 1.6 km in 1 mile
    return km

my_trip_miles = 55

# 2) Convert my_trip_miles to km by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blnck to print the result of the conversion
print("The distance in Kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the res#ult, and fill in the blank to print the result

print("The round-trip in kilometers is " + str(my_trip_km * 2))
