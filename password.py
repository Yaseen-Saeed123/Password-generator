"""
This project is practice on the string module, loops, conditionals, lists, try ... except
"""
import string
import random

# Create lists of characters
upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
digits = list(string.digits)
puncutuation = list(string.punctuation)

# Get number of characters
while True:
    try:
        print("-"*30)
        char_no = int(input("How many characters for your password? "))
        if char_no < 6 or char_no > 16:
            print("-"*30)
            print("Please enter a number between 6 and 16")
            pass
        else:
            break
    except:
        print("-"*30)
        print("You have to enter numbers only")

# Shuffle all lists
random.shuffle(upper)
random.shuffle(lower)
random.shuffle(digits)
random.shuffle(puncutuation)

# Calculate 30% and 20%
letter = round(char_no * (30/100))
non_letter = round(char_no * (20/100))

# Create password
password = []

for i in range(letter):
    password.append(upper[i])
    password.append(lower[i])

for i in range(non_letter):
    password.append(digits[i])
    password.append(puncutuation[i])   

# Shuffle password again
random.shuffle(password)

# Transform password into a string and print it
password = "".join(password)
print("="*30)
print("Your password is:", format(password))
print("="*30)