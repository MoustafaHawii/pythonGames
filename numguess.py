import random
import math

lower = int(input("Enter Lower bound:- "))
 
upper = int(input("Enter Upper bound:- "))
 
x = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 
counter = 0
 
while counter < math.log(upper - lower + 1, 2):
    counter += 1
 
    guess = int(input("Guess a number:- "))
 
    if x == guess:
        print("Congratulations you did it in ",
              counter, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
if counter >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)    