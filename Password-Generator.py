import random, string

# Function to color output text green in the terminal
def green(txt):
    return f"\033[92m{txt}\033[0m"

# Ask user for the desired password length and a custom string to include (optional)
pass_len = int(input("Enter the password length: "))
input_str = input("Enter the string you want to include in the password (or press Enter to skip): ")

# Check if the input string is longer than the total password length
if len(input_str) > pass_len:
    raise ValueError("The custom string is longer than the total password length!")

# Set of all characters: letters (uppercase/lowercase), digits, and symbols
charValues = string.ascii_letters + string.digits + string.punctuation

# Calculate remaining length to be filled with random characters
remain_len = pass_len - len(input_str)

# Generate the random part of the password
random_pass = "".join([random.choice(charValues) for i in range(remain_len)])

# Combine the input string with the random part and shuffle to make the password unpredictable
combined = list(input_str + random_pass)
random.shuffle(combined)

# Join the shuffled characters into the final password string
password = ''.join(combined)

# Show the result
print("Your password has been generated successfully!")
print("Your random password is:", green(password))
