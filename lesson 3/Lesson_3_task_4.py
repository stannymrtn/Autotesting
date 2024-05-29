from turtle import *
myScreen = Turtle()
myScreen.screen.setup(640,480)

def drawHead(myScreen):
    myScreen.up() # Голова
    myScreen.goto(0,-50)
    myScreen.pensize(5)
    myScreen.down()
    myScreen.circle(50)
    

def drawRightEye(myScreen):
    myScreen.up() # Правый глаз
    myScreen.goto(20,10)
    myScreen.pensize(1)
    myScreen.down()
    myScreen.circle(5)

def drawLeftEye(myScreen):
    myScreen.up() # Левый глаз
    myScreen.goto(-20,10)
    myScreen.pensize(1)
    myScreen.down()
    myScreen.circle(5)

def drawNose(myScreen): # Нос
    myScreen.up()
    myScreen.goto(-3,-5)
    myScreen.pensize(1)
    myScreen.down()
    myScreen.circle(4)

def drawMouth(myScreen):
    myScreen.width(2)
    myScreen.up()
    myScreen.goto(-20, -10)
    myScreen.down()
    myScreen.setheading(-60)
    myScreen.circle(20,120)

def drawleftMustache(myScreen):
    myScreen.up()
    myScreen.goto(-30, 0)
    myScreen.down()
    myScreen.setheading(180)
    myScreen.forward(60)
    myScreen.up()
    myScreen.goto(-30, -5)
    myScreen.down()
    myScreen.setheading(180)
    myScreen.forward(60)
    myScreen.up()
    myScreen.goto(-30, -10)
    myScreen.down()
    myScreen.setheading(180)
    myScreen.forward(60)
    myScreen.up()
    myScreen.goto(-30, -15)
    myScreen.down()
    myScreen.setheading(180)
    myScreen.forward(60)

def drawRightMustache(myScreen):
    myScreen.up()
    myScreen.goto(20, 0)
    myScreen.down()
    myScreen.setheading(-360)
    myScreen.forward(75)
    myScreen.up()
    myScreen.goto(20, -5)
    myScreen.down()
    myScreen.setheading(-360)
    myScreen.forward(75)
    myScreen.up()
    myScreen.goto(20, -10)
    myScreen.down()
    myScreen.setheading(-360)
    myScreen.forward(75)
    myScreen.up()
    myScreen.goto(20, -15)
    myScreen.down()
    myScreen.setheading(-360)
    myScreen.forward(75)

def drawlefthear(myScreen):
    myScreen.up()
    myScreen.goto(-30, 30)
    myScreen.down()
    myScreen.setheading(120)
    myScreen.forward(40)
    myScreen.up()
    myScreen.goto(-50, 5)
    myScreen.down()
    myScreen.setheading(90)
    myScreen.forward(60)

def drawrighthear(myScreen):
    myScreen.up()
    myScreen.goto(50,15)
    myScreen.down()
    myScreen.setheading(90)
    myScreen.forward(60)
    myScreen.up()
    myScreen.goto(30, 30)
    myScreen.down()
    myScreen.setheading(65)
    myScreen.forward(50)

    

head = drawHead(myScreen)
rightEye = drawRightEye(myScreen)
leftEye = drawLeftEye(myScreen)
nose = drawNose(myScreen)
mouth = drawMouth(myScreen)
leftmustache = drawleftMustache(myScreen)
rightmustache = drawRightMustache(myScreen)
lefthear = drawlefthear(myScreen)
righthear = drawrighthear(myScreen)

myScreen.screen.exitonclick()
myScreen.screen.mainloop()