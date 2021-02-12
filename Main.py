import random # Importing the random module.

a = random.randint(1, 2) # Guessing randomly between 1 and 2 using 'random' module.
if a == 1: # Telling the Program what to do if the guess is 1.
    print("You got Heads!") # Printing Heads as the Result.
else: # Putting an else condition so that the Program knows what to do if guess is 2.
    print("You got Tails!") # Printing Tails as the Result.