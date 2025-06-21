import random, string
import pyperclip

# Function to color output text green in the terminal
def green(txt):
    return f"\033[92m{txt}\033[0m"

# Function to copy the generated password to the clipboard and notify the user.
def copy_to_clipboard(pwd):
    if pwd:
        try:
            pyperclip.copy(pwd)
            print("\033[94mPassword copied to clipboard!\033[0m")  # blue message
        except pyperclip.PyperclipException:
            print("\033[91mClipboard copy failed (unsupported OS or missing xclip/xsel).\033[0m")   # red message
    else:
        print("\033[91mNo password to copy!\033[0m")    # red message


# ------------ main logic ------------ #
def main():
    # Ask user for length and optional custom string
    pass_len = int(input("Enter the password length: "))
    input_str = input("Enter the string you want to include in the password (or press Enter to skip): ")

    if len(input_str) > pass_len:
        raise ValueError("The custom string is longer than the total password length!")

    # Set of all characters: letters (uppercase/lowercase), digits, and symbols
    charValues = string.ascii_letters + string.digits + string.punctuation

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

    # Offer to copy
    copy = input("\nCopy password to clipboard? (y/n): ").strip().lower()
    if copy == "y":
        copy_to_clipboard(password)


if __name__ == "__main__":
    main()