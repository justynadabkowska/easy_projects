import random
random_number = random.randint(0,2)
word_list = ["aardvark", "baboon", "camel"]

chosen_word = word_list[random_number]
print(chosen_word)
guess = (input("Write a letter: ")).lower()
print(guess)
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
