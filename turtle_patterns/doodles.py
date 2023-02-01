'''
Project Name: Turtle Patterns I
Author: Bailey Haskell
Due Date: 2023-01-31
Course: CS1400-zzz

Put your description here, lessons learned here, and any other information
someone using your program would need to know to make it run.
'''
# (3) add functions here that your main program calls
# to do stuff.
import turtle
def get_dimensions():
# Grabbing input for screen size
    width = int(input())
    height = int(input())

# Exception to catch if input is a positive integer
    if width < 1 or height < 1:
        raise ValueError

    return (width, height)

# Triangle function
def triangle(color, size, tilt):
    '''Draws a triangle'''
    turtle.fillcolor(color)
    turtle.begin_fill()      
    for i in range(3):
        turtle.lt(tilt)
        turtle.forward(size)

    turtle.end_fill()

def square(color,size,tilt):
    '''Draws a square'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.rt(tilt)
        turtle.forward(size)
    turtle.end_fill()

def circle(color, size, tilt):
    '''Draws a circle'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def rectangle(color, size, tilt):
    '''Draws a rectangle'''
    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.forward(size)
    turtle.lt(tilt)

    turtle.forward(size*1.8)
    turtle.lt(tilt)

    turtle.forward(size)
    turtle.lt(tilt)

    turtle.forward(size*1.8)
    turtle.end_fill()

def draw_house():
    '''Draws a house'''
    '''setting size for house and using porportions to find door size and doorknob size'''
    tri_size = 300
    sq_size = tri_size
    rec_size = sq_size * .3
    circle_size = rec_size * .1
# Draws roof
    triangle("red", tri_size, 120)
# Draws body of the house
    square("blue", sq_size, 90)
# picking up pen to not leave a line while moving to next point
    turtle.penup()
    turtle.goto((-(sq_size/2))-(rec_size/2),-(sq_size))
    turtle.pendown()
# Draws door
    rectangle("brown", rec_size, 90)
# picking up pen to not leave a line while moving to next point
    turtle.penup()
    turtle.goto((-(sq_size/2))-(rec_size/2) + rec_size*.2 ,-sq_size+((rec_size*1.8)/2))
    turtle.pendown()
# Draws doorknob
    circle("yellow", circle_size, 0)

def draw(width, height):
    '''
    Sets the size of the screen to width and height and draws a doodle.
    '''
    turtle.Screen().setup(width, height)
# Calls house function to draw a house
    draw_house()
    turtle.done()
