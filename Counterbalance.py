import turtle
from myShape import *
from random import randint
bob = turtle.Turtle()
turtle.bgcolor("black")
turtle.colormode(255)
turtle.tracer(0)
turtle.shape("turtle")


bob.color("pink")
for times in range(100):
    n = randint(1, 100)
    print(randint(1, 100))
    bob.forward(10)
    bob.left(90)
    polygon(bob, 10, 360)
    bob.right(250)

move(300, 300, bob)

bob.color("white")
for times in range(100):
    n = randint(1, 100)
    print(randint(1, 100))
    bob.forward(10)
    bob.left(90)
    polygon(bob, 10, 360)
    bob.right(250)


    
move(200, -150, bob)

bob.color("cyan")
for times in range(100):
    n = randint(1, 100)
    print(randint(1, 100))
    bob.forward(10)
    bob.left(90)
    polygon(bob, 10, 360)
    bob.right(250)

move(300, 150, bob)

bob.color("purple")
for times in range(100):
    n = randint(1, 100)
    print(randint(1, 100))
    bob.forward(10)
    bob.left(90)
    polygon(bob, 10, 360)
    bob.right(250)

bob.width("5")
for times in range(36):
    move(0, 0, bob)
    bob.color("pink")
    polygon(bob, 1000, 4)
    bob.right(90)
    bob.forward(10)
    bob.left(20)
    move(0, 0, bob)
    bob.right(90)
    bob.color("purple")
    polygon(bob, 200, 8)
    bob.right(90)
    bob.forward(10)
    bob.left(20)
    
for times in range(36):
    move(0, 0, bob)
    bob.color("light blue")
    polygon(bob, 1000, 3)
    bob.right(90)
    bob.forward(10)
    bob.left(20)
    move(0, 0, bob)
    bob.right(90)
    bob.color("white")
    polygon(bob, 200, 6)
    bob.right(90)
    bob.forward(10)
    bob.left(20)

for times in range(30):
    move(0, 0, bob)
    bob.color(0,150,200)
    polygon(bob, 1000, 8)
    bob.left(35)

for times in range(40):
    move(0, 0, bob)
    bob.color("cyan")
    polygon(bob, 3000, 3)
    bob.left(20)
    bob.forward(100)

move(-100, 100, bob)

for times in range(36):
    move(0, 0, bob)
    bob.color("pink")
    polygon(bob, 1000, 4)
    bob.right(90)
    bob.forward(10)
    bob.left(20)
    move(0, 0, bob)
    bob.right(90)
    bob.color("purple")
    polygon(bob, 200, 8)
    bob.right(90)
    bob.forward(10)
    bob.left(20)
    
for times in range(36):
    move(0, 0, bob)
    bob.color("light blue")
    polygon(bob, 1000, 3)
    bob.right(90)
    bob.forward(10)
    bob.left(20)
    move(0, 0, bob)
    bob.right(90)
    bob.color("white")
    polygon(bob, 200, 6)
    bob.right(90)
    bob.forward(10)
    bob.left(20)

for times in range(30):
    move(0, 0, bob)
    bob.color(0,150,200)
    polygon(bob, 1000, 8)
    bob.left(35)

for times in range(40):
    move(0, 0, bob)
    bob.color("cyan")
    polygon(bob, 3000, 3)
    bob.left(20)
    bob.forward(100)
