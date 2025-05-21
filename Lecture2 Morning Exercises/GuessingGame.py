#Generate a random number btn 1 and 10. Keep asking the user
import random
#Generate a random number
secret_number = random.randint(1,10)
while True:
    guess = int(input("Guess a number between 1 and 10"))
    if guess == secret_number:
        print ("Cheers  you've guessed right")
        break
        
    else:
        print("Wrong Guess")
            