def calculate_bmi(weight: float, height: float) -> float:
    """Calculate the Body Mass Index (BMI)."""
    return weight / (height ** 2)


def categorize_bmi(bmi: float) -> str:
    """Categorize the BMI value."""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal weight"
    elif bmi < 30:
        return "overweight"


# Get the height and weight from the user
height: float = float(input("Enter your height in meters: "))
weight: float = float(input("Enter your weight in kilograms: "))

# Call the function to calculate the BMI
bmi: float = calculate_bmi(weight, height)

# Print the BMI and its category
print("Your BMI is:", round(bmi, 2))
print("You are", categorize_bmi(bmi))
