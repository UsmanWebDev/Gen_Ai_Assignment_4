import math


def calculate_cylinder_volume(radius: float, height: float) -> float:
    """Calculate the volume of a cylinder."""
    return math.pi * (radius ** 2) * height


# Get the radius and height from the user
radius: float = float(input("Enter the radius of the cylinder: "))
height: float = float(input("Enter the height of the cylinder: "))

# Call the function to calculate the volume
volume: float = calculate_cylinder_volume(radius, height)

# Print the volume
print("The volume of the cylinder is:", round(volume, 2))
