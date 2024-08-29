def calculate_cube_surface_area(side):
    """Calculate the surface area of a cube given its side length."""
    return 6 * (side ** 2)


# Define the side variable
side = float(input("Enter the side length of the cube: "))

# Call the function to calculate the surface area
surface_area = calculate_cube_surface_area(side)

# Print the surface area
print("The surface area of the cube is:", surface_area)
