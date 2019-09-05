'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
timmy=turtle.Turtle()
timmy.penup()
timmy.shape('turtle')
timmy.pensize(3) # width of pen line
timmy.speed(2)  # speed of drawing. Go fast to not waste time.
timmy.color("#00FF00")
timmy.setpos(0,0)
timmy.pendown()
timmy.circle(100)
timmy.penup()
timmy.setpos(-50,185)
timmy.pendown()
timmy.goto(-50,15)
timmy.penup()
timmy.goto(-10,200)
timmy.pendown()
timmy.goto(-10,0)
timmy.penup()
timmy.goto(30,185)
timmy.pendown()
timmy.goto(30,15)
timmy.penup()
timmy.goto(200,-300)
timmy.pencolor('#00FF00')
timmy.write('Emma E. Moritz',font=("Emma", 12, "normal"))
turtle.exitonclick() #Keeps pycharm window open
