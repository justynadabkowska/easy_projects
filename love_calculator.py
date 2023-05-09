# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
lower_names = name1 + name2
true_letters = lower_names.count("t") + lower_names.count("r") + lower_names.count("u") + lower_names.count("e")
love_letters = lower_names.count("l") + lower_names.count("o") + lower_names.count("v") + lower_names.count("e")
score = 10*(true_letters) + love_letters
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
