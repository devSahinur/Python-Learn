"""
1. Start
2. Input guessNumber
3. Generate RandomNumber
4. If guessNumber == randomNumber
    i) yes , print won
    ii) No, print lost
5. End
"""
from random import randint

for x in range(1,6):
    guessNumber = int(input("Enter your guess between 1 to 5: "))
    randomNumber = randint(1,5)   
    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have Lost. Random number was: ", randomNumber)


