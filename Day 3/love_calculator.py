print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lowercase_names = combined_names.lower()

t = lowercase_names.count('t')
r = lowercase_names.count('r')
u = lowercase_names.count('u')
e = lowercase_names.count('e')

true_score = t + r + u + e 

l = lowercase_names.count('l')
o = lowercase_names.count('o')
v = lowercase_names.count('v')
e = lowercase_names.count('e')

love_score = l + o + v + e

total_love_score = int(str(true_score) + str(love_score))
if (total_love_score < 10) or (total_love_score > 90):
    print(f"Your love score is {total_love_score}, you go together like coke and mentos.")
elif (total_love_score >= 40) and (total_love_score <= 50):
    print(f"Your love score is {total_love_score}, you are alright together.")
else:
    print(f"Your love score is {total_love_score}.")