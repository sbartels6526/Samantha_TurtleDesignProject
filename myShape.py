def polygon(t, distance, side):
    angle = 360/side
    for times in range(side):
        t.forward(distance)
        t.left(angle)

def move(x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
