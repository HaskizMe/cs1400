'''
Project Name: Turtle Patterns II
Author: Bailey Haskell
Due Date: 2023-03-2
Course: CS1400-zzz
Put your description here, lessons learned here, and any other information
someone using your program would need to know to make it run.
'''
import turtle
import random
def triangle(color, size, tilt):
    '''Draws a triangle'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    i = 0
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

def draw_house(scale, x_coord, y_coord, roof, body):
    '''setting size for house and using porportions to find door size and doorknob size'''
    tri_size = scale
    sq_size = tri_size
    rec_size = sq_size * .3
    circle_size = rec_size * .1
    # Draws roof
    move(x_coord,y_coord)
    triangle(roof, tri_size, 120)
    # Draws body of the house
    square(body, sq_size, 90)
    # picking up pen to not leave a line while moving to next point
    turtle.penup()
    turtle.goto((-(sq_size/2))-(rec_size/2)+(x_coord),(-(sq_size))+(y_coord))
    turtle.pendown()
    # Draws door
    rectangle("brown", rec_size, 90)
    # picking up pen to not leave a line while moving to next point
    turtle.penup()
    turtle.goto(((-(sq_size/2))-(rec_size/2) + rec_size*.2)+x_coord ,(-sq_size+((rec_size*1.8)/2))+y_coord)
    turtle.pendown()
    # Draws doorknob
    circle("yellow", circle_size, 0)

def draw_star():
    '''Draws one star'''
    size = 10
    angle = 120
    # color to fill
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    # form star
    i = 0
    while i < 5:
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
        i = i+1
    # fill color
    turtle.end_fill()

def draw_stars():
    '''Draws multiple stars'''
    i = 0
    while i < 15:
        move(random.randint(-490,490),random.randint(100,390))
        draw_star()
        i = i+1

def draw_cloud():
    '''Draws one cloud'''
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
    '''Draws multiple clouds'''
    i = 0
    while i < 6:
        move(random.randint(-490,490),random.randint(100,390))
        draw_cloud()
        i = i+1

def move(x_coord, y_coord):
    '''Used to move the pen'''
    turtle.penup()
    turtle.goto(x_coord, y_coord)
    turtle.pendown()

def draw_bird():
    '''Draws one bird'''
    turtle.color("black","black")
    turtle.setheading(0)
    turtle.pensize(5)
    turtle.rt(-120)
    turtle.circle(10,120)
    turtle.rt(120)
    turtle.circle(10,120)
    turtle.pensize(0)

def draw_birds():
    '''Draws multiple birds'''
    i = 0
    while i < 5:
        move(random.randint(-490,490),random.randint(100,390))
        draw_bird()
        i = i+1

def draw_houses():
    '''Draws multiple houses'''
    draw_house(150, 0, -100, "green", "black")
    turtle.setheading(0)
    draw_house(175,-300, -125, "orange", "dark blue")
    turtle.setheading(0)
    draw_house(50, 200, -90, "grey", "purple")
    turtle.setheading(0)

def get_screen_height():
    '''Returning the screen height'''
    return 800

def get_screen_width():
    '''Returning the screen width'''
    return 1000

def draw_scene(scene):
    '''Draws an entire scene of day or night'''
    # splitting the middle
    color_sky = "white"
    color_ground = "white"
    # Changes background color based on scene type
    if scene == "night":
        color_sky = "dark blue"
        color_ground = "dark green"
        turtle.Screen().bgcolor(color_sky)
        draw_stars()
        draw_birds()
    else:
        color_sky = "light blue"
        color_ground = "light green"
        turtle.Screen().bgcolor(color_sky)
        draw_clouds()
        draw_birds()
    # Draws the background and splits the screen into sky and ground
    turtle.setheading(0)
    bottom_half = get_screen_height()/6
    top_half = -get_screen_width()/2
    move(top_half, -bottom_half)
    turtle.fillcolor(color_ground)
    turtle.begin_fill()
    turtle.forward(get_screen_width())
    turtle.rt(90)
    turtle.forward((get_screen_height()/2) - bottom_half)
    turtle.rt(90)
    turtle.forward(get_screen_width())
    turtle.rt(90)
    turtle.forward((get_screen_height()/2) - bottom_half)
    turtle.end_fill()
    turtle.setheading(0)
    draw_houses()

def draw(my_list):
    '''Sets the size of the screen to width and height and draws a doodle.'''
    turtle.Screen().setup(get_screen_width(), get_screen_height())
    if my_list[0] == "night":
        draw_scene("night")
    elif my_list[0] == "day":
        draw_scene("day")
    else:
        print("Please enter either 'day' or 'night'")
    # turtle.done()