import figures
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
figures.draw_square(20,-100,100)
figures.draw_square(20,-60,100)

figures.draw_rectangle(20,40,-20,100)

figures.draw_rectangle(20,40,20,100)

figures.draw_trangle(30,60,100)
figures.draw_trangle(30,100,100)

window.mainloop()