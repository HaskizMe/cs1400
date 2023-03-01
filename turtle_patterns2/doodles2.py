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
import random
screen_width = 1000
screen_height = 800
# Triangle function
def triangle(color, size, tilt):
    '''Draws a triangle'''
    turtle.fillcolor(color)
    turtle.begin_fill() 
    i = 0     
    # for i in range(3):
    while i < 3:
        turtle.lt(tilt)
        turtle.forward(size)
        i+=1

    turtle.end_fill()

def square(color,size,tilt):
    '''Draws a square'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    j = 0
    while j < 4:
        turtle.rt(tilt)
        turtle.forward(size)
        j+=1
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
    tri_size = 100
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

def draw_star():
    size = 10
    angle = 120
    # color to fill
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    # form star
    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    # fill color
    turtle.end_fill()

def draw_stars():

    for i in range(15):
        move(random.randint(-490,490),random.randint(100,390))
        draw_star()

def draw_cloud():
    turtle.color("white","white")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.rt(90)
    turtle.forward(10)
    turtle.circle(30)
    turtle.rt(90)
    turtle.circle(30)
    turtle.right(90)
    turtle.circle(30)
    turtle.right(90)
    turtle.end_fill()

def draw_clouds():
    for i in range(6):
        move(random.randint(-490,490),random.randint(100,390))
        draw_cloud()


def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_scene(scene):
    # splitting the middle
    color_sky = "white"
    color_ground = "white"

    if(scene == "night"):
        color_sky = "dark blue"
        color_ground = "dark green"
        turtle.Screen().bgcolor(color_sky)
        draw_stars()
    else:
        color_sky = "light blue"
        color_ground = "light green"
        turtle.Screen().bgcolor(color_sky)
        draw_clouds()
    bottom_half = screen_height/6
    top_half = -screen_width/2
    move(top_half, -bottom_half)
    turtle.fillcolor(color_ground)
    turtle.begin_fill()
    turtle.forward(screen_width)
    turtle.rt(90)
    turtle.forward((screen_height/2) - bottom_half)
    turtle.rt(90)
    turtle.forward(screen_width)
    turtle.rt(90)
    turtle.forward((screen_height/2) - bottom_half)
    turtle.end_fill()
    move(0,0)
    turtle.setheading(0)
    draw_house()

def draw(list):
    '''
    Sets the size of the screen to width and height and draws a doodle.
    '''
    turtle.Screen().setup(screen_width, screen_height)
    if(list[0] == "night"):
        draw_scene("night")
    
    elif(list[0] == "day"):
        draw_scene("day")
    
    # Calls house function to draw a house
    # move(0,0)
    # draw_house()
    # draw_stars()
    turtle.done()