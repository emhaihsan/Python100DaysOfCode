# Password Generator Project
# Prompt user for desired password length
# Include number of letters, symbols and numbers
# Generate a password based on user input

# Import the random module
import random

# Define lists of characters for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Prompt user for desired password length
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate a password based on user input
orderedPass = []
for _ in range(nr_letters):
    # Add random letters to the ordered password list
    orderedPass.append(random.choice(letters))
for _ in range(nr_symbols):
    # Add random symbols to the ordered password list
    orderedPass.append(random.choice(symbols))
for _ in range(nr_numbers):
    # Add random numbers to the ordered password list
    orderedPass.append(random.choice(numbers))

randomPass = ""
for _ in range(len(orderedPass)):
    # Generate a random character from the ordered password list
    char = random.choice(orderedPass)
    # Remove the character from the ordered password list
    orderedPass.remove(char)
    # Add the character to the random password string
    randomPass += char

# Print the generated password
print(randomPass)

