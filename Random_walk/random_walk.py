import subprocess
import tempfile
import textwrap
import traceback
import turtle
import sys
import random
import math
import statistics

'''Program supposed to plot random walks on turtle graphics'''

def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to dest. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        command = ['gs',
                   '-dSAFER',
                   '-o',
                   dest,
                   '-r200',
                   '-dEPSCrop',
                   '-sDEVICE=png16m',
                   tmp.name]
        try:
            subprocess.run(command,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           check=True)
        except Exception as exp:
            message = f'''\
            There was an error running ghostscript.

            If you are seeing this error in Codio, please report it to your instructor.
            If you are seeing this error elsewhere, consider installing ghostscript or
            replacing the call to `save_to_image()' with `turtle.done()' in your local
            copy. Be sure not to change run_doodles.py in Codio!

            The system was attempting to run the following command:
            {' '.join(command)}

            Error details:
            '''
            print(textwrap.dedent(message), file=sys.stderr)
            [_, minor, _] = sys.version.split()[0].split('.')
            minor = int(minor)
            # python version >= 3.10
            if minor >= 10:
                # pylint: disable=E1120
                traceback.print_exception(exp)
            # python version < 3.10
            else:
                traceback.print_exception(None, exp, None)




def north():
    return (0,1)

def east():
    return (1,0)

def south():
    return (0,-1)

def west():
    return (-1,0)


def pa_steps():
    return random.choice(((0,1),(0,-1),(1,0),(-1,0)))

def mi_ma_steps():
    return random.choice((0,0),(0,-2),(1,0),(-1,0))

def reg_steps():
    return random.choice((0,0),(1,0),(-1,0))


def walk(person):
    # if person == 'pa':
    pa_steps()

    pass


def find_median(my_list):
    # mean = 0
    new_list = []
    for i in range(len(my_list)):
        mean = 0

        for j in range(len(my_list[i])):

            mean += abs(my_list[i][j]**2)
            
            # print(mean)
            # mean = math.sqrt(mean)
            # print(mean)
        mean = math.sqrt(mean)
        new_list.append(mean)
    # return round(mean/len(my_list),1)
    # print(new_list)
    return round(statistics.mean(new_list),1)

    # return new_list

def simulate(walk_lengths_list, number_of_trials, person):
    # helper_function(walk_lengths_list,plot())
    # print(number_of_trials)
    # Checking to see which person is selected
    # pa_list = []

    if person == 'pa':
        pa_list = []
        pa_list2 = []

        mean, cv, max, min = 0, 0, 0, 0
        for i in range(len(walk_lengths_list)):

            for j in range(number_of_trials):
                x_coords = 0
                y_coords = 0
                for k in range(walk_lengths_list[i]):

                    pa_coords = pa_steps()
                    x_coords += pa_coords[0]
                    y_coords += pa_coords[1]
                if(i == 0):
                    pa_list.append((x_coords,y_coords))
                else:
                    pa_list2.append((x_coords,y_coords))
                # pa_list.append(y_coords)
                # pa_list.clear()
                print("index #" , i, "trial #", j+1,  '(',x_coords, y_coords,')')

        print("Pa random walk of", walk_lengths_list[0], "steps")
        print('median',find_median(pa_list))
        # print(pa_list)
        # print(pa_list2)
        # for i in range(len(pa_list)):
        # print(pa_list[0][0])




        # for i in range(len(walk_lengths_list)):
        #     x_coords = 0
        #     y_coords = 0
        #     for k in range(walk_lengths_list[i]):

        #         for j in range(number_of_trials):
        #             pa_coords = pa_steps()
        #             x_coords += pa_coords[0]
        #             y_coords += pa_coords[1]
        #             # print(pa_coords)
        #             print(j+1,x_coords,y_coords)
        #     print("--------------")
                # print('trail #',i+1,'(',x_coords,y_coords,')')
                # Final destination of pa
                # print("trails ", j, "-" ,x_coords,y_coords)
        #     print(i)
        # x_coords = 0
        # y_coords = 0

        # for i in range(number_of_trials):
        #     x_coords = 0
        #     y_coords = 0
        #     for j in range(len(walk_lengths_list)):

        #         for k in range(walk_lengths_list[j]):
        #             pa_coords = pa_steps()
        #             x_coords += pa_coords[0]
        #             y_coords += pa_coords[1]
        #             # print(pa_coords)
        #             # print(x_coords,y_coords)
        #         print("trail" , j, "(",x_coords,y_coords,") for ", str(walk_lengths_list[j]) )


        # print(pa_steps())

    elif person == 'mi-ma':
        print("mi-ma")
    elif person == 'reg':
        print('reg')
    elif person == 'all':
        print('all')
    else:
        print("error")
    
    # print(walk_lengths_list)
    # print(number_of_trials)

    pass

# def helper_function(list, plotter()):
#     return list
def plot():
    # define turtle, screen size

    # Define color, shape for pa
    #plot pa
    # simulate([100], 50, 'pa')
    # turtle.stamp()


    # Define color, shape for mi-ma
    #plot mi-ma
    # simulate([100], 50, 'mi-ma')
    # turtle.stamp()

    # Define color, shape for reg
    #plot reg
    # simulate([100], 50, 'reg')
    # turtle.stamp()

    pass


def main():
    list_walk_lengths = []
    if ',' in sys.argv[1]:
        list_walk_lengths = sys.argv[1].split(',')
        list_walk_lengths[0] = int(list_walk_lengths[0])
        list_walk_lengths[1] = int(list_walk_lengths[1])
    else:
        list_walk_lengths.append(int(sys.argv[1]))
    # list_walk_lengths[0] = int(list_walk_lengths[0])
    # list_walk_lengths[1] = int(list_walk_lengths[1])
    trials = int(sys.argv[2])
    person = sys.argv[3].lower()

    simulate(list_walk_lengths, trials, person)
    # mean, cv, max, min = simulate(list_walk_lengths, trials, person)

    # print() mean, cv, max, min

    # plot()
    # save_to_image()
    pass
if __name__ == "__main__":
    main()
