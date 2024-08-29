def convert_seconds(total_seconds):
    """Convert seconds into minutes and seconds."""
    return total_seconds // 60, total_seconds % 60


# Get the number of seconds from the user
total_seconds = int(input("Enter the total number of seconds: "))

# Call the function and get the result
minutes, seconds = convert_seconds(total_seconds)

# Print the result
print(f"{total_seconds} seconds is equal to {
      minutes} minutes and {seconds} seconds")
