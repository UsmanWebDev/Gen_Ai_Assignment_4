def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


# Define length and width variables
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function to calculate the area
area = calculate_area(length, width)

# Print the area
print("The area of the rectangle is:", area)
