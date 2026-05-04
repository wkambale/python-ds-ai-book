user_input = "twenty-five"

try:
    # Code that might raise an exception goes in the 'try' block
    number = int(user_input)
    print(f"You entered the number: {number}")
except ValueError:
    # Code to handle the specific error goes in the 'except' block
    print(f"Error: '{user_input}' is not a valid integer. Please enter a number.")