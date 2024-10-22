import figures
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
pen = turtle.Turtle()
pen.speed(5)
figures.draw_square(20,0,0)
pen.hideturtle()
window.mainloop()