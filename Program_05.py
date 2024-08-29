def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def temperature_conversion():
    """Temperature Conversion Program."""
    print("Temperature Conversion Program")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
    else:
        print("Invalid choice. Please enter 1 or 2.")


# Run the temperature conversion program
temperature_conversion()
