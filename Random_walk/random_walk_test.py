# import subprocess
# import tempfile
# import textwrap
# import traceback
# import turtle
# import sys
# import random
# import math
# import statistics

# '''Program supposed to plot random walks on turtle graphics'''

# import subprocess
# import tempfile
# import textwrap
# import traceback

# def save_to_image(dest='random_walk.png'):
#     '''Saves the turtle canvas to dest. Do not modify this function.'''
#     with tempfile.NamedTemporaryFile(prefix='random_walk',
#                                      suffix='.eps') as tmp:
#         turtle.getcanvas().postscript(file=tmp.name)
#         command = ['gs',
#                    '-dSAFER',
#                    '-o',
#                    dest,
#                    '-r200',
#                    '-dEPSCrop',
#                    '-sDEVICE=png16m',
#                    tmp.name]
#         try:
#             subprocess.run(command,
#                            stdout=subprocess.PIPE,
#                            stderr=subprocess.STDOUT,
#                            check=True)
#         except Exception as exp:
#             message = f'''\
#             There was an error running ghostscript.

#             If you are seeing this error in Codio, please report it to your instructor.
#             If you are seeing this error elsewhere, consider installing ghostscript or
#             replacing the call to `save_to_image()' with `turtle.done()' in your local
#             copy. Be sure not to change run_doodles.py in Codio!

#             The system was attempting to run the following command:
#             {' '.join(command)}

#             Error details:
#             '''
#             print(textwrap.dedent(message), file=sys.stderr)
#             [_, minor, _] = sys.version.split()[0].split('.')
#             minor = int(minor)
#             # python version >= 3.10
#             if minor >= 10:
#                 # pylint: disable=E1120
#                 traceback.print_exception(exp)
#             # python version < 3.10
#             else:
#                 traceback.print_exception(None, exp, None)




# def north():
#     return (0,1)

# def east():
#     return (1,0)

# def south():
#     return (0,-1)

# def west():
#     return (-1,0)


# def pa_steps():
#     return random.choice(((0,1),(0,-1),(1,0),(-1,0)))

# def mi_ma_steps():
#     return random.choice(((0,1),(0,-1),(0,-1),(1,0),(-1,0)))

# def reg_steps():
#     return random.choice(((1,0),(-1,0)))


# # def walk(length):
    
# #     pa_steps()

# #     pass


# def find_median(my_list):
#     # mean = 0
#     new_list = []
#     for i in range(len(my_list)):
#         mean = 0

#         for j in range(len(my_list[i])):

#             mean += abs(my_list[i][j]**2)
            
#             # print(mean)
#             # mean = math.sqrt(mean)
#             # print(mean)
#         mean = math.sqrt(mean)
#         new_list.append(mean)
#     # return round(mean/len(my_list),1)
#     # print(new_list)
#     return round(statistics.mean(new_list),1)


# def find_max(my_list):
#     new_list = []
#     for i in range(len(my_list)):
#         max = 0
#         for j in range(len(my_list[i])):
#             max += abs(my_list[i][j]**2)
#         max = round(math.sqrt(max),1)
#         new_list.append(max)
#     new_list.sort()
#     return new_list[-1]

# def find_min(my_list):
#     new_list = []
#     for i in range(len(my_list)):
#         max = 0
#         for j in range(len(my_list[i])):
#             max += abs(my_list[i][j]**2)
#         max = round(math.sqrt(max),1)
#         new_list.append(max)
#     new_list.sort()
#     return new_list[0]


# def find_cv(my_list):
#     new_list = []
#     for i in range(len(my_list)):
#         mean = 0

#         for j in range(len(my_list[i])):

#             mean += abs(my_list[i][j]**2)

#         mean = math.sqrt(mean)
#         new_list.append(mean)

#     return round((statistics.stdev(new_list))/(statistics.mean(new_list)),1)

# def print_info(my_list):
#     print("Pa random walk of", my_list[0], "steps")
#     print('Median =',find_median(my_list), 'CV =', find_cv(my_list))
#     print('Max =', find_max(my_list), 'Min =', find_min(my_list))

#     # print("Pa random walk of", walk_lengths_list[1], "steps")
#     # print('Median =',find_median(pa_list2), 'CV =', find_cv(pa_list2))
#     # print('Max =', find_max(pa_list2), 'Min =', find_min(pa_list2))
#     return

# def simulate(walk_lengths_list, number_of_trials, person):

#     if person == 'pa':
#         pa_list = []
#         test = []
#         pa_list2 = []
#         for i in range(len(walk_lengths_list)):

#             for j in range(number_of_trials):
#                 x_coords = 0
#                 y_coords = 0
#                 for k in range(walk_lengths_list[i]):

#                     pa_coords = pa_steps()
#                     x_coords += pa_coords[0]
#                     y_coords += pa_coords[1]

#                 pa_list.append((x_coords,y_coords))
#         test.append(pa_list)
#         print(len(test))
#         print(test[0])
#         # print(test[1])
#                 # print("index #" , i, "trial #", j+1,  '(',x_coords, y_coords,')')

#         # if(len(walk_lengths_list) > 1):
#         #     for i in range(len(walk_lengths_list)):

#         #         # print_info(walk_lengths_list[i])
#             # print("Pa random walk of", walk_lengths_list[0], "steps")
#             # print('Median =',find_median(pa_list), 'CV =', find_cv(pa_list))
#             # print('Max =', find_max(pa_list), 'Min =', find_min(pa_list))

#             # print("Pa random walk of", walk_lengths_list[1], "steps")
#             # print('Median =',find_median(pa_list2), 'CV =', find_cv(pa_list2))
#             # print('Max =', find_max(pa_list2), 'Min =', find_min(pa_list2))

#         # else:
#         #     print("Pa random walk of", walk_lengths_list[0], "steps")
#         #     print('Median =',find_median(pa_list), 'CV =', find_cv(pa_list))
#         #     print('Max =', find_max(pa_list), 'Min =', find_min(pa_list))


#     elif person == 'mi-ma':
#         ma_list = []
#         ma_list2 = []
#         for i in range(len(walk_lengths_list)):

#             for j in range(number_of_trials):
#                 j_coords = 0
#                 k_coords = 0
#                 for k in range(walk_lengths_list[i]):

#                     ma_coords = mi_ma_steps()
#                     j_coords += ma_coords[0]
#                     k_coords += ma_coords[1]
#                 if(i == 0):
#                     ma_list.append((j_coords,k_coords))
#                 else:
#                     ma_list2.append((j_coords,k_coords))

#                 # print("index #" , i, "trial #", j+1,  '(',x_coords, y_coords,')')

#         if(len(walk_lengths_list) > 1):
#             print("Mi-Ma random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(ma_list), 'CV =', find_cv(ma_list))
#             print('Max =', find_max(ma_list), 'Min =', find_min(ma_list))

#             print("Mi-Ma random walk of", walk_lengths_list[1], "steps")
#             print('Median =',find_median(ma_list2), 'CV =', find_cv(ma_list2))
#             print('Max =', find_max(ma_list2), 'Min =', find_min(ma_list2))

#         else:
#             print("Mi-Ma random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(ma_list), 'CV =', find_cv(ma_list))
#             print('Max =', find_max(ma_list), 'Min =', find_min(ma_list))


#     elif person == 'reg':
#         reg_list = []
#         reg_list2 = []
#         for i in range(len(walk_lengths_list)):

#             for j in range(number_of_trials):
#                 l_coords = 0
#                 m_coords = 0
#                 for k in range(walk_lengths_list[i]):

#                     reg_coords = reg_steps()
#                     l_coords += reg_coords[0]
#                     m_coords += reg_coords[1]
#                 if(i == 0):
#                     reg_list.append((l_coords,m_coords))
#                 else:
#                     reg_list2.append((l_coords,m_coords))


#         if(len(walk_lengths_list) > 1):
#             print("Reg random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(reg_list), 'CV =', find_cv(reg_list))
#             print('Max =', find_max(reg_list), 'Min =', find_min(reg_list))

#             print("Reg random walk of", walk_lengths_list[1], "steps")
#             print('Median =',find_median(reg_list2), 'CV =', find_cv(reg_list2))
#             print('Max =', find_max(reg_list2), 'Min =', find_min(reg_list2))

#         else:
#             print("Reg random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(reg_list), 'CV =', find_cv(reg_list))
#             print('Max =', find_max(reg_list), 'Min =', find_min(reg_list))


#     elif person == 'all':
#         pa_list = []
#         pa_list2 = []
#         for i in range(len(walk_lengths_list)):

#             for j in range(number_of_trials):
#                 x_coords = 0
#                 y_coords = 0
#                 for k in range(walk_lengths_list[i]):

#                     pa_coords = pa_steps()
#                     x_coords += pa_coords[0]
#                     y_coords += pa_coords[1]
#                 if(i == 0):
#                     pa_list.append((x_coords,y_coords))
#                 else:
#                     pa_list2.append((x_coords,y_coords))


#         if(len(walk_lengths_list) > 1):
#             print("Pa random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(pa_list), 'CV =', find_cv(pa_list))
#             print('Max =', find_max(pa_list), 'Min =', find_min(pa_list))

#             print("Pa random walk of", walk_lengths_list[1], "steps")
#             print('Median =',find_median(pa_list2), 'CV =', find_cv(pa_list2))
#             print('Max =', find_max(pa_list2), 'Min =', find_min(pa_list2))

#         else:
#             print("Pa random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(pa_list), 'CV =', find_cv(pa_list))
#             print('Max =', find_max(pa_list), 'Min =', find_min(pa_list))


#         ma_list = []
#         ma_list2 = []
#         for i in range(len(walk_lengths_list)):

#             for j in range(number_of_trials):
#                 j_coords = 0
#                 k_coords = 0
#                 for k in range(walk_lengths_list[i]):

#                     ma_coords = mi_ma_steps()
#                     j_coords += ma_coords[0]
#                     k_coords += ma_coords[1]
#                 if(i == 0):
#                     ma_list.append((j_coords,k_coords))
#                 else:
#                     ma_list2.append((j_coords,k_coords))


#         if(len(walk_lengths_list) > 1):
#             print("Mi-Ma random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(ma_list), 'CV =', find_cv(ma_list))
#             print('Max =', find_max(ma_list), 'Min =', find_min(ma_list))

#             print("Mi-Ma random walk of", walk_lengths_list[1], "steps")
#             print('Median =',find_median(ma_list2), 'CV =', find_cv(ma_list2))
#             print('Max =', find_max(ma_list2), 'Min =', find_min(ma_list2))

#         else:
#             print("Mi-Ma random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(ma_list), 'CV =', find_cv(ma_list))
#             print('Max =', find_max(ma_list), 'Min =', find_min(ma_list))

#         reg_list = []
#         reg_list2 = []

#         for i in range(len(walk_lengths_list)):

#             for j in range(number_of_trials):
#                 l_coords = 0
#                 m_coords = 0
#                 for k in range(walk_lengths_list[i]):

#                     reg_coords = reg_steps()
#                     l_coords += reg_coords[0]
#                     m_coords += reg_coords[1]
#                 if(i == 0):
#                     reg_list.append((l_coords,m_coords))
#                 else:
#                     reg_list2.append((l_coords,m_coords))

#                 # print("index #" , i, "trial #", j+1,  '(',x_coords, y_coords,')')

#         if(len(walk_lengths_list) > 1):
#             print("Reg random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(reg_list), 'CV =', find_cv(reg_list))
#             print('Max =', find_max(reg_list), 'Min =', find_min(reg_list))

#             print("Reg random walk of", walk_lengths_list[1], "steps")
#             print('Median =',find_median(reg_list2), 'CV =', find_cv(reg_list2))
#             print('Max =', find_max(reg_list2), 'Min =', find_min(reg_list2))

#         else:
#             print("Reg random walk of", walk_lengths_list[0], "steps")
#             print('Median =',find_median(reg_list), 'CV =', find_cv(reg_list))
#             print('Max =', find_max(reg_list), 'Min =', find_min(reg_list))

#     else:
#         print("error")

#     pass


# def plot():
#     # define turtle, screen size
#     t = turtle
#     t.screensize(300,400)
#     t.shapesize(.5)
#     t.shape('circle')
#     t.color('black')
#     t.speed(5)
#     pa_list = []

#     for j in range(50):
#         x_coords = 0
#         y_coords = 0
#         for k in range(100):

#             pa_coords = pa_steps()
#             x_coords += pa_coords[0]
#             y_coords += pa_coords[1]
#         pa_list.append((x_coords,y_coords))

#     for i in range(len(pa_list)):
#         x = pa_list[i][0]
#         y = pa_list[i][1]
#         t.penup()
#         t.goto(x*5, y*5)
#         t.pendown()
#         t.stamp()
#     # print(pa_list)

#     # t.penup()
#     # t.goto(0,0)
#     # t.pendown()
#     t.shape('square')
#     t.color('green')
#     t.speed(5)
#     ma_list = []

#     for j in range(50):
#         x_coords = 0
#         y_coords = 0
#         for k in range(100):

#             ma_coords = mi_ma_steps()
#             x_coords += ma_coords[0]
#             y_coords += ma_coords[1]
#         ma_list.append((x_coords,y_coords))

#     for i in range(len(pa_list)):
#         x = ma_list[i][0]
#         y = ma_list[i][1]
#         t.penup()
#         t.goto(x*5, y*5)
#         t.pendown()
#         t.stamp()


#     # t.penup()
#     # t.goto(0,0)
#     # t.pendown()
#     t.shape('triangle')
#     t.color('red')
#     t.speed(5)
#     reg_list = []

#     for j in range(50):
#         x_coords = 0
#         y_coords = 0
#         for k in range(100):

#             reg_coords = reg_steps()
#             x_coords += reg_coords[0]
#             y_coords += reg_coords[1]
#         reg_list.append((x_coords,y_coords))

#     for i in range(len(pa_list)):
#         x = reg_list[i][0]
#         y = reg_list[i][1]
#         t.penup()
#         t.goto(x*5, y*5)
#         t.pendown()
#         t.stamp()

#     pass


# def main():
#     list_walk_lengths = []
#     if ',' in sys.argv[1]:
#         list_walk_lengths = sys.argv[1].split(',')
#         list_walk_lengths[0] = int(list_walk_lengths[0])
#         list_walk_lengths[1] = int(list_walk_lengths[1])
#     else:
#         list_walk_lengths.append(int(sys.argv[1]))

#     trials = int(sys.argv[2])
#     person = sys.argv[3].lower()

#     simulate(list_walk_lengths, trials, person)

#     # plot()
#     # save_to_image()
#     pass
# if __name__ == "__main__":
#     main()







import math
from random import choice
import statistics
import sys
import turtle
def main():
    #this function beings all of the work and calls for the user's input
    turtle_dict =  {}
    '''main function'''
    list_walk_lengths = []
    if ',' in sys.argv[1]:
        list_walk_lengths = sys.argv[1].split(',')
        list_walk_lengths[0] = int(list_walk_lengths[0])
        list_walk_lengths[1] = int(list_walk_lengths[1])
    else:
        list_walk_lengths.append(int(sys.argv[1]))

    trials = int(sys.argv[2])
    person = sys.argv[3].lower()
    simulate(list_walk_lengths, trials, person, turtle_dict)
def get_direction(model):
    #this function gives the directions possible for all three models and randomly chooses one
    direction_dict = {'Pa':[(0,1),(1,0),(0,-1),(-1,0)],
              'Mi-ma':[(0,1),(1,0),(0,-1),(0,-1),(-1,0)],
              'Reg':[(1,0),(-1,0)]}
    return choice(direction_dict[model])
def simulate(split_sys, trials, model, turtle_dict):
    #this is the main work done. it takes the coordinates from each model and appends them to a list of coordinates
    #then they print out the ending results
    coordinates = []
    distance = []
    if model == 'pa':
        for step_choice in split_sys:
            coordinates = []
            distance = []
            for walk in range(trials):
                position = [0,0]
                for step in range(step_choice):
                    x = randomwalk(step_choice, get_direction('Pa'),position)
                coordinates.append(x)
                dist = walk_distance(x)
                distance.append(dist)
                get_direction('Pa')
            print(f'{model} random walk of {step_choice} steps')
            values(distance)
            turtle_dict['Pa'] = coordinates
    elif model == 'mi-ma':
        for step_choice in split_sys:
            coordinates = []
            distance = []
            for walk in range(trials):
                position = [0,0]
                for step in range(step_choice):
                    x = randomwalk(step_choice, get_direction('Mi-ma'),position)
                coordinates.append(x)
                dist = walk_distance(x)
                distance.append(dist)
                get_direction('Mi-ma')
            print(f'{model} random walk of {step_choice} steps')
            values(distance)
            turtle_dict['Mi-ma'] = coordinates
    elif model == 'reg':
        for step_choice in split_sys:
            coordinates = []
            distance = []
            for walk in range(trials):
                position = [0,0]
                for step in range(step_choice):
                    x = randomwalk(step_choice, get_direction('Reg'),position)
                coordinates.append(x)
                dist = walk_distance(x)
                distance.append(dist)
                get_direction('Reg')
            print(f'{model} random walk of {step_choice} steps')
            values(distance)
            turtle_dict['Reg'] = coordinates
    elif model == 'all':
        pa_position = [0,0]
        mima_position = [0,0]
        reg_position = [0,0]
        for step_choice in split_sys:
            coordinates = []
            distance = []
            for walk in range(trials):
                position = [0,0]
                for step in range(step_choice):
                    x = randomwalk(step_choice, get_direction('Pa'),position)
                coordinates.append(x)
                dist = walk_distance(x)
                distance.append(dist)
                get_direction('Pa')
            print(f'Pa random walk of {step_choice} steps')
            values(distance)
            turtle_dict['Pa'] = coordinates
        coordinates = []
        distance = []
        for step_choice in split_sys:
            coordinates = []
            distance = []
            for walk in range(trials):
                position = [0,0]
                for step in range(step_choice):
                    x = randomwalk(step_choice, get_direction('Mi-ma'),position)
                coordinates.append(x)
                dist = walk_distance(x)
                distance.append(dist)
                get_direction('Mi-ma')
            print(f'Mi-ma random walk of {step_choice} steps')
            values(distance)
            turtle_dict['Mi-ma'] = coordinates
        coordinates = []
        distance = []
        for step_choice in split_sys:
            coordinates = []
            distance = []
            for walk in range(trials):
                position = [0,0]
                for step in range(step_choice):
                    x = randomwalk(step_choice, get_direction('Reg'),position)
                coordinates.append(x)
                dist = walk_distance(x)
                distance.append(dist)
                get_direction('Reg')
            print(f'Reg random walk of {step_choice} steps')
            values(distance)
            turtle_dict['Reg'] = coordinates
    else:
        print(f"Incorrect input")
        quit()
def values(distance):
    #this is the mathematic function. it takes all of the coordinates from the list and creates the values
    Mean = statistics.mean(distance)
    CV = statistics.stdev(distance)/Mean
    Max = max(distance)
    Min = min(distance)
    print(f"Mean = {Mean:.1f} CV = {CV:.1f}")
    print(f"Max = {Max:.1f} Min = {Min:.1f}")
def randomwalk(walk_length,c_direction,position):
    #this takes each position taken from any model, and adds it to the previous coordinate which results
    #in the final position for the model
    position[0]+= c_direction[0]
    position[1]+= c_direction[1]
    return position

def walk_distance(position):
    #this is the function that calculates the distance from the final location to the origin point
    x = math.sqrt((position[0]**2) + (position[1]**2))
    return x
def plot():
    #this plots all of the coordinates for each model and places them in a turtle window.
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    model = "Pa"
    t.color("black")
    t.shape("circle")
    for trial in range(50):
        position = [0,0]
        for step in range(100):
            position = randomwalk(100,get_direction('Pa'),position)
        position[0],position[1] = position[0]*5,position[1]*5
        t.goto(position)
        t.stamp()
    model = "Mi-ma"
    t.color("green")
    t.shape("square")
    for trial in range(50):
        position = [0,0]
        for step in range(100):
            position = randomwalk(100,get_direction('Mi-ma'),position)
        position[0],position[1] = position[0]*5,position[1]*5
        t.goto(position)
        t.stamp()
    model = ("Reg")
    t.color("red")
    t.shape("arrow")
    for trial in range(50):
        position = [0,0]
        for step in range(100):
            position = randomwalk(100,get_direction('Reg'),position)
        position[0],position[1] = position[0]*5,position[1]*5
        t.goto(position)
        t.stamp()
    
main()

def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to dest. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        subprocess.run(['gs',
                        '-dSAFER',
                        '-o',
                        dest,
                        '-r200',
                        '-dEPSCrop',
                        '-sDEVICE=png16m',
                        tmp.name],
                       stdout=subprocess.DEVNULL)