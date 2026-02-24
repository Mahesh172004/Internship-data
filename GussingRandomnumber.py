import random

def guess_random_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Guess the random number between 1 and 100!")

    while True:
        guess=int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Yay! you guessed the number {number} in {attempts} attempts!")  
            break
guess_random_number()
      