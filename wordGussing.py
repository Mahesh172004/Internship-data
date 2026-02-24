import random

def guess_random_word():
    words = ["python", "java", "html", "css", "js", "react", "angular"]
    word = random.choice(words)
    attempts = 0

    print("Guess the random programming word!")
    print("Hint: programming language / web tech")

    while True:
        guess = input("Enter your guess: ").lower()
        attempts += 1

        if guess < word:
            print("Your guess comes BEFORE the word alphabetically. Try again.")
        elif guess > word:
            print("Your guess comes AFTER the word alphabetically. Try again.")
        else:
            print(f" Yay! You guessed the word '{word}' in {attempts} attempts.")
            break

guess_random_word()

#Assigment: Create a word guessing game where the user has to guess a random word from a predefined list. The game should provide feedback on whether the user's guess is correct, too high (comes after the word alphabetically), or too low (comes before the word alphabetically). The game should keep track of the number of attempts and display it when the user guesses the word correctly.