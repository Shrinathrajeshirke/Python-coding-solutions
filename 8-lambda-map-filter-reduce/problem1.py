# Using lambda and map():

# Take a list of temperatures in Celsius
# Convert all to Fahrenheit
# Formula: F = (C × 9/5) + 32

def celsius_to_fehrenheit(temp_list):
    print("Output: ")
    print(f"{'Celsius:': <12} {temp_list}")
    return list(map(lambda x: round((x*(9/5))+32,1), temp_list))

print(f"{'fahrenheit:':<12} {celsius_to_fehrenheit([0, 20, 37, 100])}")