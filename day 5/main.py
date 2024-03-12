import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
letters_num = int(input("How many letters would you like in )your password?\n"))
symbols_num = int(input("How many symbols would you like?\n"))
numbers_num = int(input("How many numbers would you like?\n"))

generated_pass = []

generated_pass.extend(random.choices(symbols,k=symbols_num))

generated_pass.extend(random.choices(letters,k=letters_num))

generated_pass.extend(random.choices(numbers,k=numbers_num))

random.shuffle(generated_pass)

new_generated_pass = ""

for char in generated_pass:
  new_generated_pass += str(char)


print(
  new_generated_pass
)