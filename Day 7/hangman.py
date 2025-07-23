word_list = ["advark", "baboon", "camel", "dingo", "elephant", "flamingo", "giraffe", "hippopotamus", "iguana", "jaguar"]

import random
chosen_word = random.choice(word_list)

guess =(input("Welcome to Hangman! Guess a letter: ").lower())

for letter in chosen_word:
    if letter == guess:
        print(f"Good guess! The letter '{guess}' is in the word.")
    else:
        print(f"Sorry, the letter '{guess}' is not in the word.")
        