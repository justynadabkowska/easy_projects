
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Order not randomised:

number_letter = 0
summary_letters = ""
for number_letter in range(1, (int(nr_letters) + 1)):
  random_letter = random.randint(0, (len(letters)-1))
  summary_letters += (letters[random_letter])

number_number = 0
summary_numbers = ""
for number_number in range(1, (int(nr_numbers) + 1)):
  random_number = random.randint(0, (len(numbers)-1))
  summary_numbers += (numbers[random_number])

number_symbols = 0
summary_symbols = ""
for number_symbols in range(1, (int(nr_symbols) + 1)):
  random_symbol = random.randint(0, (len(symbols)-1))
  summary_symbols += (symbols[random_symbol])

ordered_password = summary_symbols + summary_letters + summary_numbers
print(f"Ordered password is: {ordered_password}")

#Randomised order:

randomized_password = ''.join(random.sample(ordered_password, len(ordered_password)))
print(f"Randomized password is: {randomized_password}")