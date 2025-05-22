secret_number = 7

while True:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == secret_number:
        print(" Cheers! You've guessed right.")
        break
    else:
        print(" Wrong guess. Try again.")

            