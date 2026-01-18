#This is a number guessing game
import random
secret_number = random.randint(1,10)#Number is between 1 and 10 inclusive
print("I'm thinking of a number between 1 and 10, you have 6 chances to guess it 😁.")

for guessesTaken in range(1,7):       #The user has 6 chances to guess the correct number
    guess = int(input("Take a guess:"))

    if guess < secret_number:
        print("Your guess is way too low , scoop a little high ")
    elif guess > secret_number:
        print("Your guess is way too high, scoop a little low ")
    else:
        break

if guess == secret_number:
    print(f"You guessed the correct number in {str(guessesTaken)} guess(es)!")
else:
    print(f"Nope, the correct number is {secret_number}")

