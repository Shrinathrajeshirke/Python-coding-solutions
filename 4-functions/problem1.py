# Write a function that:

# Takes length and width as parameters
# Returns area AND perimeter
# Of a rectangle
# Print both results

def rectangle(length, breadth):
    area_of_rect = length*breadth
    perimeter_of_rect = 2*(length+breadth)

    return area_of_rect, perimeter_of_rect

area, perimeter = rectangle(10,5)

print(f"Area of rectangle: {area}")
print(f"Perimeter of rectangle: {perimeter}")