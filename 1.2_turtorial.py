'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
timmy=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
timmy.pensize(3) # width of pen line
timmy.speed(10)  # speed of drawing. Go fast to not waste time.
timmy.color("#00FF00")
timmy.setpos(50,185) #right ear
timmy.pendown()
timmy.goto(200,210)
timmy.goto(88,145)
timmy.penup()
timmy.setpos(-50,185)  #left ear
timmy.pendown()
timmy.goto(-200,210)
timmy.goto(-88,145)
timmy.penup()
timmy.setpos(200,-300)
timmy.pendown()
timmy.pencolor('#00FF00')
timmy.write('Sign Your Name Here',font=("Emma", 12, "normal"))
timmy.setpos(210,-300)
timmy.write(EmmaMoritz)
turtle.exitonclick() #Keeps pycharm window open
