import math


def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * (radius ** 2)


# Define the radius variable
radius = float(input("Enter the radius of the circle: "))

# Call the function to calculate the area
area = calculate_circle_area(radius)

# Print the area
print("The area of the circle is:", area)
