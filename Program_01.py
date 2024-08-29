def calculate_age(birth_year, current_year):
    """Calculate the age based on birth year and current year."""
    return current_year - birth_year


# Ask for birth year and current year
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

# Call the function to calculate age
age = calculate_age(birth_year, current_year)

# Print age
print("Your age is:", age)
