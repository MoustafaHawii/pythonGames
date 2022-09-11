#importiert das Modul random. Die zufällige Zahlen generiert
import random
#importiert das Modul math. Mit dem man mathematische Operationen durchführen kann.
import math

#Der Benutzer gibt die untere Grenze ein.
lower = int(input("Enter Lower bound:- "))
#Der Benutzer gibt die obere Grenze ein.
upper = int(input("Enter Upper bound:- "))
#Generiert eine zufällige Ganzzahl in dem Bereich und speichert diese in x.
x = random.randint(lower, upper)
#Gibt die Chancenanzahl zurück.
#round(2) rundet die Dezimalzahl auf 2 Stellen. 
#Die Anzahl Rateversuche werden so berechnet log2(untere Grenze - obere Grenze + 1)
print("You've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!")
#Variabel mit Anzahl Rateversuche
counter = 0
#Solange counter nicht grösser ist als die maximale Anzahl versuche ist gut.
while counter < math.log(upper - lower + 1, 2):
    #Ein Versucht wird dem counter hinzugefügt.
    counter += 1
    #Der Benutzer kann eine Zahl eingeben. Diese wird in die guess gespeichert.
    guess = int(input("Guess a number:- "))
    #Wenn guess gleich x ist wird hat man gewonnen.
    if x == guess:
        print("Congratulations you did it in ",
              counter, " try")
        break
    #Wenn der Versuch kleiner als x ist wird der Tipp gegeben höher zu raten.
    elif x > guess:
        print("You guessed too small!")
    #Wenn der Versuch grösser als x ist wird der Tipp gegeben tiefer zu raten.
    elif x < guess:
        print("You Guessed too high!")
#Wenn man nach dem vorgegebenen Maximum an Versuchen es immernoch nicht geschafft hat. Wird die Lösung angezeigt.
if counter >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)    