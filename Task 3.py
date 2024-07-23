#A password generator is a useful tool that generates strong and
#random passwords for users. This project aims to create a
#password generator application using Python, allowing users to
#specify the length and complexity of the password.

import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_punctuation=True):
    characters = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    try:
        length = int(input("Enter the desired length of the password: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
        return length, use_uppercase, use_digits, use_punctuation
    except ValueError:
        print("Invalid input. Please enter a number for the password length.")
        return get_user_input()

def main():
    print("Welcome to the Password Generator!")
    length, use_uppercase, use_digits, use_punctuation = get_user_input()
    
    try:
        password = generate_password(length, use_uppercase, use_digits, use_punctuation)
        print("\nGenerated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
