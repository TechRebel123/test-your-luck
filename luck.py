import time
import turtle
import random

q = input("DO YOU WANT TO TEST YOUR LUCK(YES/NO)? ").upper()
if q == "YES":
    print("LETS GO")
    time.sleep(4)

else:
    quit()

turtle.title("TRY YOUR LUCK!")

bob = turtle.Turtle()

turtle.bgcolor("cyan")

color = bob.color("red", "black")

bob.speed(0)

bob.ht()

bob.begin_fill()
bob.circle(150)
bob.penup()
bob.left(90)
bob.forward(10)
bob.right(90)
bob.end_fill()

color = bob.color("red", "red")

bob.begin_fill()
bob.circle(130)
bob.left(90)
bob.forward(10)
bob.right(90)
bob.end_fill()

color = bob.color("red", "yellow")

bob.begin_fill()
bob.circle(110)
bob.left(90)
bob.forward(10)
bob.right(90)
bob.end_fill()

color = bob.color("red", "blue")

bob.begin_fill()
bob.circle(90)
bob.left(90)
bob.forward(10)
bob.right(90)
bob.end_fill()

color = bob.color("red", "cyan")

bob.begin_fill()
bob.circle(60)
bob.left(90)
bob.forward(10)
bob.right(90)
bob.end_fill()

bob.pendown()

bob.penup()
bob.right(90)
bob.pensize(10)
bob.forward(300)

bob.color("white")

bob.goto(-22, 83)

bob.write("100",font=('arial',20,'bold'))

bob.goto(-12, 164)
bob.write("50",font=('arial',18,'bold'))

bob.goto(-10, 214)
bob.write("25",font=('arial',15,'bold'))

bob.goto(-8, 250)
bob.write("10",font=('arial',13,'bold'))

bob.goto(-4, 275)
bob.write("5",font=('arial',13,'bold'))

bob.st()

bob.goto(0, -200)
bob.left(180)
bob.shape("circle")
bob.color("#444")

time.sleep(10)
bob.speed(3)

#codes

a = "-22, 83"
b = "-12, 164"
c = "-10, 214"
d = "-8, 250"
e = "-4, 275"

all_pos = a, b, c, d, e

select = random.choice(all_pos)

if select == a:
    bob.goto(-22, 83)
    time.sleep(3)
    bob.ht()
    bob.goto(-400, -200)
    bob.write("YOU GOT 100 POINTS, YOU WON!", font=('Serif', 40,'bold'))

elif select == b:
    bob.goto(-12, 164)
    time.sleep(3)
    bob.ht()
    bob.goto(-300, -200)
    bob.write("YOU GOT 50 POINTS, GOOD BUT NOT THE BEST", font=('Serif', 25,'bold'))

elif select == c:
    bob.goto(-10, 214)
    time.sleep(3)
    bob.ht()
    bob.goto(-300, -200)
    bob.write("YOU GOT 25 POINTS, FINE", font=('Serif', 40,'bold'))
    
elif select == d:
    bob.goto(-8, 250)
    time.sleep(3)
    bob.ht()
    bob.goto(-300, -200)
    bob.write("YOU GOT 10 POINTS, NOOB", font=('Serif', 40,'bold'))

elif select == e:
    bob.goto(-4, 275)
    time.sleep(3)
    bob.ht()
    bob.goto(-300, -200)
    bob.write("YOU GOT 5 POINTS, YOU CAN BETTER DIE, HAHAHAH",font=('Serif', 12,'bold'))

turtle.done()