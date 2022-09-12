#Das sind modules die wir für das Game benötigen und deshalb importieren
#Ein Modul mit dem man Formen zeichnen kann.
import turtle
#Bietet möglichkeiten Zeit im Code darzustellen.
import time
#Generiert zufällig Zahlen.
import random

#Wir erstellen Standardwerte für das Spiel.
delay = 0.1
score = 0
high_score = 0

#Erstellen das GUI-Fenster.
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
#Breite und Höhe vom Fenster festlegen.
wn.setup(width=600, height=600)
#Die turtle Animation ausschalten
wn.tracer(0)

#Kopf der Schlange erstellen
head = turtle.Turtle()
#Der Kopf ist ein Rechteck
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

#Die Äpfel im Game.
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'white'])
shapes = random.choice(['circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

#Den Score und Highscore erstellen.¨
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))

#Den Tasten eine funktion geben.
def group():
    if head.direction != "down":
        head.direction = "up"
 
 
def godown():
    if head.direction != "up":
        head.direction = "down"
 
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
 
def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#Soll die auf folgende Tasten reagieren.
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

#Ein Array von neuen Körperteilen
segments = []

#Programmlogik 
while True:
    wn.update()
    #Wir hollen uns die Kordionate des Kopfs und prüfen ob dieser in eine Wand fuhr.
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        #Unterbricht die Ausführung für 1 Sekunde.
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    #Wo essen plaziert wird nach dem man eins gegessen hat.
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
    
        #ein neues Körperteil hinzufügen
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

        #Kontrolle ob Kopf mit Körper kolidiert
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
 
wn.mainloop()