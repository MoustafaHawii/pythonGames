#Das sind modules die wir für das Game benötigen und deshalb importieren
#Ein Modul mit dem man Formen zeichnen kann.
from ast import main
import turtle
#Bietet möglichkeiten Zeit im Code darzustellen.
import time
#Generiert zufällig Zahlen.
import random

#Wir erstellen Standardwerte für das Spiel.
delay = 0.1
punkte = 0
high_score = 0

#Erstellen das GUI-Fenster.
main_panel = turtle.Screen()
main_panel.title("Snake")
main_panel.bgcolor("black")
#Breite und Höhe vom Fenster festlegen.
main_panel.setup(width=600, height=600)
#Die turtle Animation ausschalten
main_panel.tracer(0)

#Kopf der Schlange erstellen
kopf = turtle.Turtle()
#Der Kopf ist ein Rechteck
kopf.shape("square")
kopf.color("white")
kopf.penup()
kopf.goto(0, 0)
kopf.direction = "Stop"

#Die Äpfel im Game.
apfel = turtle.Turtle()
farben = random.choice(['red', 'green', 'yellow'])
apfel.shape("circle")
apfel.speed(0)
apfel.color(farben)
apfel.penup()
apfel.goto(0, 100)

#Den Score und Highscore erstellen.¨
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Score: 0 High Score: 0", align="center", font=("candara", 24, "bold"))

#Den Tasten eine funktion geben.
def group():
    if kopf.direction != "down":
        kopf.direction = "up"
 
 
def godown():
    if kopf.direction != "up":
        kopf.direction = "down"
 
 
def goleft():
    if kopf.direction != "right":
        kopf.direction = "left"
 
 
def goright():
    if kopf.direction != "left":
        kopf.direction = "right"

def move():
    if kopf.direction == "up":
        y = kopf.ycor()
        kopf.sety(y+20)
    if kopf.direction == "down":
        y = kopf.ycor()
        kopf.sety(y-20)
    if kopf.direction == "left":
        x = kopf.xcor()
        kopf.setx(x-20)
    if kopf.direction == "right":
        x = kopf.xcor()
        kopf.setx(x+20)

#Soll die auf folgende Tasten reagieren.
main_panel.listen()
main_panel.onkeypress(group, "w")
main_panel.onkeypress(godown, "s")
main_panel.onkeypress(goleft, "a")
main_panel.onkeypress(goright, "d")

#Ein Array von neuen Körperteilen
segments = []

#Programmlogik 
while True:
    main_panel.update()
    #Wir hollen uns die Kordionate des Kopfs und prüfen ob dieser in eine Wand fuhr.
    if kopf.xcor() > 290 or kopf.xcor() < -290 or kopf.ycor() > 290 or kopf.ycor() < -290:
        #Unterbricht die Ausführung für 1 Sekunde.
        time.sleep(1)
        kopf.goto(0,0)
        kopf.direction = "Stop"
        farben = random.choice(['grey', 'red', 'white'])
        kopf.shape("square")
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        punkte = 0
        delay = 0.1
        score.clear()
        score.write("Score : {} High Score : {} ".format(punkte, high_score), align="center", font=("candara", 24, "bold"))

    #Wo essen plaziert wird nach dem man eins gegessen hat.
    if kopf.distance(apfel) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        apfel.goto(x, y)
    
        #ein neues Körperteil hinzufügen
        neues_segment = turtle.Turtle()
        neues_segment.speed(0)
        neues_segment.shape("square")
        neues_segment.color("orange")  # tail colour
        neues_segment.penup()
        segments.append(neues_segment)
        delay -= 0.001
        punkte += 10
        if punkte > high_score:
            high_score = punkte
        main_panel.clear()
        main_panel.write("Score: {} High Score: {} ".format(punkte, high_score), align="center", font=("candara", 24, "bold"))

        #Kontrolle ob Kopf mit Körper kolidiert
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = kopf.xcor()
        y = kopf.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(kopf) < 20:
            time.sleep(1)
            kopf.goto(0,0)
            kopf.direction("stop")
            farben = random.choice(['grey', 'red', 'white'])
            kopf.shape("square")
            for segment in segments:
                segment.goto(1000,1000)
            segment.clear()

            punkte = 0
            delay = 0.1
            score.clear()
            score.write("Score : {} High Score : {} ".format(punkte, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

main_panel.mainloop()