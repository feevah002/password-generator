# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
generated_password = ''
# generate random letters 
for number in range(0, nr_letters):
    randomLetterIndex = random.randint(0,25)
    generated_password += letters[randomLetterIndex]
# generate random symbols
for number in range(0, nr_symbols):
    randomSymbolIndex = random.randint(0,8)
    generated_password += symbols[randomSymbolIndex]
# generate random numbers
for number in range(0, nr_numbers):
    randomNumIndex = random.randint(0,9)
    generated_password += numbers[randomNumIndex]
print(f'sequential: {generated_password}')

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
shuffled_password = ''
used_index = []
while len(shuffled_password) != len(generated_password):
    x = random.randint(0, len(generated_password) - 1)
    if (x in used_index):
         continue
    else:
        used_index.append(x)
        shuffled_password += generated_password[x] 

print(f'randomised: {shuffled_password}')
