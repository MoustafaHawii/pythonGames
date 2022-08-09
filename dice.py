import random

against = True 

while against: 
    print(random.randint(1, 6))
    nextRoll = input("Roll again?(y/n)")
    if nextRoll.lower() == "y":
        continue
    else: 
        print ("bye")
        break
