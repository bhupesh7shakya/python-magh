from random import randint as a

def guess_the_number():
    random_number = a(1, 10)
    attempts = 0
    print("\nWelcome to the number guessing game.")
    print("The number to be guessed is between 1 to 10.")
    print("Can you guess it correct in lesser attempts ?")

    while True:
        user_guess = input("Enter a number: ")
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        user_guess = int(user_guess)
        attempts += 1

        if user_guess < random_number:
            print("Too low, Better luck next time.")
        elif user_guess > random_number:
            print("Too high, Better luck next time.")
        elif user_guess == random_number:
            print(f"Congratulations, Your guess is correct. You guessed it correct in {attempts} attempts.")
            guess_the_number()

if __name__ == "__main__":
    guess_the_number()