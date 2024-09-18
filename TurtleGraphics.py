#TurtleGraphics.py
#Name: Max Perry
#Date: 9/18/2024
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS

hideturtle() #hides the default turtle in CodeHS

def square(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def fillCorner(myTurtle,corner):
    square(myTurtle,100)
    if corner==2:
        myTurtle.forward(100)
        myTurtle.right(90)
    elif corner==3:
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.right(180)
    elif corner==4:
        myTurtle.forward(100)
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.right(90)
    myTurtle.begin_fill()
    square(myTurtle,50)
    myTurtle.end_fill()
    

def drawPolygon(myTurtle,sides):
    for i in range(sides):
        myTurtle.forward(20)
        myTurtle.right(360/sides)

def squaresInSquares(myTurtle,num):
    size=30
    for i in range(num):
        myTurtle.up()
        myTurtle.goto(-(size/2),(size/2))
        myTurtle.down()
        square(myTurtle,size)
        size=size+20
    
def main():
    myTurtle = turtle.Turtle()
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
