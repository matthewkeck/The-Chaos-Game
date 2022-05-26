## Matthew R Keck
## 5/26/2022
## the ChaosGame

import turtle
import random
import time
import math

## Creates a window to display the turtle graphics.
window = turtle.bgcolor("black")
window = turtle.getscreen()
## Creats a pen to draw graphics.
pen = turtle.Turtle()

## sets a value to the properties of the pen-like color, size, shape, and speed.
pen.pen(pencolor="green", fillcolor="green", pensize=5, speed=2)
pen.shape("turtle")

## This Function prints the word hello on the window by giving the graphic specific instructions.
def hello():
    
    x = -300
    y = 100
    pen.penup()
    pen.goto((x,y))

    pen.right(90)
    pen.pendown()
    pen.forward(200)
    pen.penup()
    pen.backward(100)
    pen.left(90)
    pen.pendown()
    pen.forward(100)
    pen.left(90)
    pen.penup()
    pen.forward(100)
    pen.pendown()
    pen.backward(200)
    pen.penup()

    pen.right(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(200)
    pen.pendown()
    pen.backward(200)
    pen.right(90)
    pen.forward(50)
    pen.penup()
    pen.backward(50)
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.backward(50)
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    pen.pendown()
    pen.forward(50)
    pen.penup()

    pen.forward(50)
    pen.pendown()
    pen.right(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(50)
    pen.penup()
    pen.backward(50)
    pen.left(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(50)

    pen.forward(50)
    pen.pendown()
    pen.right(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(50)
    pen.penup()
    pen.forward(125)

    pen.pendown()
    pen.circle(100)

## This function allows the user to play the game with a pentagon.
def pentagon(pen,numberOfIterations):
    ## Setting our x and y coordinates.
    x = 0
    y = 0

    ## Setting the x and y coordinates for each point on the pentagon.
    xMid = 0
    yMid = 200

    xTopRight = 300
    yTopRight = 0

    xTopLeft = -300
    yTopLeft = 0

    xBottomRight = 200
    yBottomRight = -300

    xBottomLeft = -200
    yBottomLeft = -300

    ## For loop will run-up to the user-selected number of iterations. Every time through
    ## the loop there will be a new dot.
    for a in range(numberOfIterations):
        ## The probability variable determines the point on the pentagon we will move to to leave
        ## a dot.
        prob = random.randint(1,5)

        ## If-else chain determines which point we head to.
        if prob == 1:
            ## sets the pen to a new color.
            pen.pen(pencolor="red", fillcolor="red", pensize=1, speed=9)
            ## Determines how close we move to the point on the pentagon by adding our current position
            ## to the point position and dividing by three.
            x = (x + xTopRight)/3
            y = (y + yTopRight)/3
            ## Moves penup we don't draw a line as we move to our new x and y coordinates.
            pen.penup()
            pen.goto((x,y))
            ## Places the pen down and leaves a dot.
            pen.pendown()
            pen.dot(3)

        ## else if statment because we only want one of our if statements to run every time we go through
        ## the loop.
        elif prob == 2:
            pen.pen(pencolor="yellow", fillcolor="yellow", pensize=1, speed=9)
            x = (x + xTopLeft)/3
            y = (y + yTopLeft)/3
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

        elif prob == 3:
            pen.pen(pencolor="blue", fillcolor="blue", pensize=1, speed=9)
            x = (x + xBottomRight)/3
            y = (y + yBottomRight)/3
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

        elif prob == 4:
            pen.pen(pencolor="green", fillcolor="green", pensize=1, speed=9)
            x = (x + xMid)/3
            y = (y + yMid)/3
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

        else:
            pen.pen(pencolor="purple", fillcolor="purple", pensize=1, speed=9)
            x = (x + xBottomLeft)/3
            y = (y + yBottomLeft)/3
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

## Similar to the pentagon function only now we are playing the game on a square with four points.
def square(pen,numberOfIterations):
    x = 0
    y = 0

    xTopRight = 300
    yTopRight = 300

    xTopLeft = -300
    yTopLeft = 300

    xBottomRight = 300
    yBottomRight = -300

    xBottomLeft = -300
    yBottomLeft = -300

    for a in range(numberOfIterations):
        ## I got weard results on a square but this probability seemed to create a fractal.
        prob = random.randint(1,8)
        
        if prob == 1 or prob == 2:
            pen.pen(pencolor="green", fillcolor="green", pensize=1, speed=9)
            x = (x + xTopRight)/3
            y = (y + yTopRight)/3
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

        elif prob == 3 or prob == 4:
            pen.pen(pencolor="red", fillcolor="red", pensize=1, speed=9)
            x = (x + xTopLeft)/3
            y = (y + yTopLeft)/3
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

        elif prob == 5 or prob == 6:
            pen.pen(pencolor="yellow", fillcolor="yellow", pensize=1, speed=9)
            x = (x + xBottomRight)/3
            y = (y + yBottomRight)/3
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

        else:
            pen.pen(pencolor="blue", fillcolor="blue", pensize=1, speed=9)
            x = (x + xBottomLeft)/3
            y = (y + yBottomLeft)/3
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

    
## Similar to the last two functions only now we are playing the game on a triangle with three points.

def triangle(pen,numberOfIterations):
    x = 0
    y = 0

    xMid = 0
    yMid = 300

    xRight = 300
    yRight = -300

    xLeft = -300
    yLeft = -300

    for a in range(numberOfIterations):
        prob = random.randint(1,6)
        
        if prob == 1 or prob == 2:
            pen.pen(pencolor="red", fillcolor="red", pensize=1, speed=20)
            x = (x + xMid)/2
            y = (y + yMid)/2
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

        elif prob == 3 or prob == 4:
            pen.pen(pencolor="blue", fillcolor="blue", pensize=1, speed=20)
            x = (x + xRight)/2
            y = (y + yRight)/2
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

        else:
            pen.pen(pencolor="green", fillcolor="green", pensize=1, speed=20)
            x = (x + xLeft)/2
            y = (y + yLeft)/2
            pen.penup()
            pen.goto((x,y))
            pen.pendown()
            pen.dot(3)

## This function is similar but fairly different then last functions we will be trying the game on a
## spiral.
def spiral(tt,numberOfIterations):
    theta = 0
    r = 0
    x = 0
    y = 0
    i = 0

    currentX = 0
    currentY = 0

    theta2 = 0
    r2 = 0
    x2 = 0
    y2 = 0

    currentX2 = 0
    currentY2 = 0

    pen.pen(pencolor="yellow", fillcolor="yellow", pensize=3, speed=9)

    while i < numberOfIterations:

        ## Theta determines a random number that represents the angle we will be traveling. uniform to generates
        ## a random floating numbers.
        theta = random.uniform(.1,12.5)

        ## r is the radius of our spiral. We calculate r by scaling the golden ratio to the power
        ## of our random varble theta and multply all that by 5.
        r = (((1+math.sqrt(5))/2)**theta)*5

        ## We find our x and y corrdinats parametrically by useing sin and cos of theta multiplyed by
        ## our radius.
        y = math.sin(theta) * r
        x = math.cos(theta) * r

        currentX = (x - currentX) * .3
        currentY = (y - currentY) * .3

        pen.penup()
        pen.goto((currentX,currentY))
        pen.pendown()
        pen.dot(2)



        i = i + 1

## The function allows the user to call all other functions.
def main():
    ## variables to allow the user to choose the function and the number of iterations 
    ## the function will run.
    userSelection = 0
    numberOfIterations = 0

    ## calls the hello function to print the word hello on the turtle graphic window.
    hello()

    ## try and catch statement to stop any user input errors.
    try:

        ## while statement so the user can iterate through the menu multiple times.
        while userSelection != 5:

            ## prints the menu to the user and saves the user input.
            userSelection = int(input("select a shape. \n" +
                  "1. triangle \n" +
                  "2. square \n" +
                  "3. pentagon \n" +
                  "4. spiral \n" +
                  "5. exit minu \n"))

            ## if-else chain to match the user input with the function from the menu.
            if userSelection == 1:
                
                numberOfIterations = int(input("enter the number of iterations you would like to generate. I recommend at least 500.\n"))
                pen.clear()
                triangle(pen, numberOfIterations)
                
            elif userSelection == 2:
                
                numberOfIterations = int(input("enter the number of iterations you would like to generate. I recommend at least 500.\n"))
                pen.clear()
                square(pen, numberOfIterations)
                
            elif userSelection == 3:
                
                numberOfIterations = int(input("enter the number of iterations you would like to generate. I recommend at least 500.\n"))
                pen.clear()
                pentagon(pen, numberOfIterations)

            elif userSelection == 4:
                
                numberOfIterations = int(input("enter the number of iterations you would like to generate. I recommend at least 500.\n"))
                pen.clear()
                spiral(pen, numberOfIterations)

            elif userSelection == 5:
                break;

            else:
                print("invalid input")

    except:
        print("An exception occurred")
    



main()





