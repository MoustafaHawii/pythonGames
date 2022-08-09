name = input("Enter your name: ")
print(f"Greetings{name}! Welcome to your adventure!")
start = input("Would you rather play game or die?")
if start == "play":
    print ("Great! Lets play the game!")
    setting = input("Want to go to the jungle or the desert? ")
else:
    print("Okay you are dead, good work...")
    quit()

if setting == "jungle":
    print("Welcome to the mighty Amazon rainforest! Your tour guide told you to wait...")
    response = input("But he has been gone a long time... Follow him or wair here?")
    if response == "follow":
        print("You head off in the direction the guide left.")
    elif response == "wait":
        print("You give it another 10 minutes... still nothing!")
        response = input("Keep waiting or follow him? ")
        if response == "follow":
            print("You head off in the direction the guide left.")
        elif response == "wait":
            print("He finally comes back! He said the Jungle is lame and the tour is over! Ending 1/6 Found!")
            quit()
    else:
        print("invalid response! you lose!")
        quit()
    follow = input("You saw him head towards the river, there is a canoe nearby. Follow by walking or canoe? ")
    if follow == "walk":
        print("As soon as you walk into the woods a huge snake crushes you to death! Ending 2/6 Found!")
        quit()
    elif follow == "canoe":
        print("As soon as you get in the canoe, a huge wave washes you overboard and leeches drain your blood! \n Ending 3/6 Found!")
        quit()
    else:
        print("invalid response! you lose!")
        quit()
elif setting == "desert":
    print("Welcome to the mighty Sahara Desert! Your tour guide told you to wait...")
    response = input("but he has been gone a while now... follow him or wait here?")
    if response == "follow":
        print("You head off in the direction the guide left.")
    elif response == "wait":
        print("You give it another 10minutes... still nothing!")
        response = input("Keep waiting or follow him? ")
        if response == "follow":
            print("You head off in the direction the guide left.")
        elif response == "wait":
            print("He finally comes back! He said the Desert is too hot and the tour is over! Ending 4/6 Found!")
            quit()
    else:
        print("Not a valid response, you lose!")
        quit()
    follow = input("You saw him head towards the Pyramids, there is a camel nearby. Follow by walking or camel? ")
    if follow == "walk":
        print("As soon as you start walking a scorpion stings you and the poison kills you! Ending 5/6 Found!")
        quit()
    elif follow == "camel":
        print("The camel you are riding leads you straight to treasure and now you are billionaire!\n Ending 6/6 Found!")
        quit()
    else:
        print("Not a vaid response, you lose!")
        quit()
        
