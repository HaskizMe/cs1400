import random
import statistics
import turtle
# import numpy

def move(x,y,the_color,the_shape,scale):
    # turtle.pensize(500)
    turtle.speed(0)
    turtle.shape(the_shape)
    turtle.color(the_color)
    turtle.penup()
    turtle.goto(x*scale,y*scale)
    turtle.pendown()
    turtle.stamp()
    pass


def main():


    random.seed(100)
    pa_list = [(0,1),(0,-1),(1,0),(-1,0)]
    mi_ma_list = [(0,0),(0,-2),(1,0),(-1,0)]
    reg_list = [(0,0),(1,0),(-1,0)]
    trials = 50
    steps = 100
    steps1 = 1000
    lst = []

    if trials == trials:
        for trial in range(trials):
            # beginning of trial for pa
            x = 0
            y = 0
            a= []
            for step in range(steps):
                # each step
                a = random.randint(0,3)
                x += pa_list[a][0]
                y += pa_list[a][1]
                # end of trial
                turtle.pensize(500)

            move(x,y,"black","circle",5)

if __name__ == "__main__":
    main()