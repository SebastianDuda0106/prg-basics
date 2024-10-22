import turtle
pen = turtle.Turtle()
pen.speed(5)
def draw_square(side_length,corda,cordb):

    # Create the turtle

    # Side length

    # Draw a square
    pen.penup()
    pen.goto(corda,cordb)
    pen.pendown()
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)

    # Hide the turtle and finish

def draw_trangle(side_length,corda,cordb):

    # Create the turtle

    # Side length

    # Draw a square
    pen.penup()
    pen.goto(corda,cordb)
    pen.pendown()
    for i in range(3):
        pen.forward(side_length)
        pen.right(120)

    # Hide the turtle and finish

def draw_rectangle(lenght_a, lenght_b,corda,cordb):
    # Create the turtle

    # Side length

    pen.penup()
    pen.goto(corda,cordb)
    pen.pendown()
    # Draw a square
    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)

    # Hide the turtle and finish
    