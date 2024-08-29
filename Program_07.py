def calculate_percentage(number, percentage):
    """Calculate the percentage of a given number."""
    return (number * percentage) / 100


# Get the number and percentage from the user
number = float(input("Enter the number: "))
percentage = float(input("Enter the percentage (%): "))

# Call the function to calculate the percentage
result = calculate_percentage(number, percentage)

# Print the result
print(f"{percentage}% of {number} is {result}")
