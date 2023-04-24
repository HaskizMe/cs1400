'''Program supposed to plot random walks on turtle graphics'''
import turtle
import sys
import random
import math
import statistics
import subprocess
import tempfile
import textwrap
import traceback

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
                traceback.print_exception(exp)
            # python version < 3.10
            else:
                traceback.print_exception(None, exp, None)


def pa_steps():
    '''Pa steps'''
    return random.choice(((0,1),(0,-1),(1,0),(-1,0)))

def mi_ma_steps():
    '''mi-ma steps'''
    return random.choice(((0,1),(0,-1),(0,-1),(1,0),(-1,0)))

def reg_steps():
    '''reg steps'''
    return random.choice(((1,0),(-1,0)))

def find_distances(my_list):
    '''finding and storing all distances'''
    new_list = []
    for i in range(len(my_list)):
        distance = 0
        distance = (my_list[i][0]**2) + abs(my_list[i][1]**2)
        distance = math.sqrt(distance)
        new_list.append(distance)
    return new_list

def find_median(my_list):
    '''Find median function'''
    find_median_list = find_distances(my_list)
    return round(statistics.mean(find_median_list),1)


def find_max(my_list):
    '''Find max function'''
    find_max_list = find_distances(my_list)
    find_max_list.sort()
    return round(find_max_list[-1],1)

def find_min(my_list):
    '''Find min function'''
    find_min_list = find_distances(my_list)
    find_min_list.sort()
    return round(find_min_list[0],1)


def find_cv(my_list):
    '''Find cv function'''
    find_cv_list = find_distances(my_list)
    return round((statistics.stdev(find_cv_list))/(statistics.mean(find_cv_list)),1)

def simulate(walk_lengths_list, number_of_trials, person):
    '''Simulating walking distances'''
    if person == 'pa':
        pa_list = []
        pa_list2 = []
        for i in range(len(walk_lengths_list)):

            for j in range(number_of_trials):
                x_coords = 0
                y_coords = 0
                for k in range(walk_lengths_list[i]):
                    pa_coords = pa_steps()
                    x_coords += pa_coords[0]
                    y_coords += pa_coords[1]
                if i == 0:
                    j = 0
                    k = 0
                    pa_list.append((j+x_coords,k+y_coords))
                else:
                    pa_list2.append((x_coords,y_coords))


        if len(walk_lengths_list) > 1:
            print("Pa random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(pa_list), 'CV =', find_cv(pa_list))
            print('Max =', find_max(pa_list), 'Min =', find_min(pa_list))

            print("Pa random walk of", walk_lengths_list[1], "steps")
            print('Mean =',find_median(pa_list2), 'CV =', find_cv(pa_list2))
            print('Max =', find_max(pa_list2), 'Min =', find_min(pa_list2))

        else:
            # print(pa_list)
            print("Pa random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(pa_list), 'CV =', find_cv(pa_list))
            print('Max =', find_max(pa_list), 'Min =', find_min(pa_list))


    elif person == 'mi-ma':
        ma_list = []
        ma_list2 = []
        for i in range(len(walk_lengths_list)):

            for j in range(number_of_trials):
                j_coords = 0
                k_coords = 0
                for k in range(walk_lengths_list[i]):
                    j = 0
                    k = 0
                    ma_coords = mi_ma_steps()
                    j_coords += ma_coords[0]
                    k_coords += ma_coords[1]
                if i == 0:
                    ma_list.append((j_coords,k_coords))
                else:
                    ma_list2.append((j_coords,k_coords))

                # print("index #" , i, "trial #", j+1,  '(',x_coords, y_coords,')')

        if len(walk_lengths_list) > 1:
            print("Mi-Ma random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(ma_list), 'CV =', find_cv(ma_list))
            print('Max =', find_max(ma_list), 'Min =', find_min(ma_list))

            print("Mi-Ma random walk of", walk_lengths_list[1], "steps")
            print('Mean =',find_median(ma_list2), 'CV =', find_cv(ma_list2))
            print('Max =', find_max(ma_list2), 'Min =', find_min(ma_list2))

        else:
            print("Mi-Ma random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(ma_list), 'CV =', find_cv(ma_list))
            print('Max =', find_max(ma_list), 'Min =', find_min(ma_list))


    elif person == 'reg':
        reg_list = []
        reg_list2 = []
        for i in range(len(walk_lengths_list)):

            for j in range(number_of_trials):
                l_coords = 0
                m_coords = 0
                for k in range(walk_lengths_list[i]):

                    reg_coords = reg_steps()
                    l_coords += reg_coords[0]
                    m_coords += reg_coords[1]
                if i == 0:
                    reg_list.append((l_coords,m_coords))
                else:
                    reg_list2.append((l_coords,m_coords))


        if len(walk_lengths_list) > 1:
            print("Reg random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(reg_list), 'CV =', find_cv(reg_list))
            print('Max =', find_max(reg_list), 'Min =', find_min(reg_list))

            print("Reg random walk of", walk_lengths_list[1], "steps")
            print('Mean =',find_median(reg_list2), 'CV =', find_cv(reg_list2))
            print('Max =', find_max(reg_list2), 'Min =', find_min(reg_list2))

        else:
            print("Reg random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(reg_list), 'CV =', find_cv(reg_list))
            print('Max =', find_max(reg_list), 'Min =', find_min(reg_list))


    elif person == 'all':
        pa_list = []
        pa_list2 = []
        for i in range(len(walk_lengths_list)):

            for j in range(number_of_trials):
                x_coords = 0
                y_coords = 0
                for k in range(walk_lengths_list[i]):

                    pa_coords = pa_steps()
                    x_coords += pa_coords[0]
                    y_coords += pa_coords[1]
                if i == 0:
                    pa_list.append((x_coords,y_coords))
                else:
                    pa_list2.append((x_coords,y_coords))


        if len(walk_lengths_list) > 1:
            print("Pa random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(pa_list), 'CV =', find_cv(pa_list))
            print('Max =', find_max(pa_list), 'Min =', find_min(pa_list))

            print("Pa random walk of", walk_lengths_list[1], "steps")
            print('Mean =',find_median(pa_list2), 'CV =', find_cv(pa_list2))
            print('Max =', find_max(pa_list2), 'Min =', find_min(pa_list2))

        else:
            print("Pa random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(pa_list), 'CV =', find_cv(pa_list))
            print('Max =', find_max(pa_list), 'Min =', find_min(pa_list))


        ma_list = []
        ma_list2 = []
        for i in range(len(walk_lengths_list)):

            for j in range(number_of_trials):
                j_coords = 0
                k_coords = 0
                for k in range(walk_lengths_list[i]):

                    ma_coords = mi_ma_steps()
                    j_coords += ma_coords[0]
                    k_coords += ma_coords[1]
                if i == 0:
                    ma_list.append((j_coords,k_coords))
                else:
                    ma_list2.append((j_coords,k_coords))


        if len(walk_lengths_list) > 1:
            print("Mi-Ma random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(ma_list), 'CV =', find_cv(ma_list))
            print('Max =', find_max(ma_list), 'Min =', find_min(ma_list))

            print("Mi-Ma random walk of", walk_lengths_list[1], "steps")
            print('Mean =',find_median(ma_list2), 'CV =', find_cv(ma_list2))
            print('Max =', find_max(ma_list2), 'Min =', find_min(ma_list2))

        else:
            print("Mi-Ma random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(ma_list), 'CV =', find_cv(ma_list))
            print('Max =', find_max(ma_list), 'Min =', find_min(ma_list))

        reg_list = []
        reg_list2 = []
        for i in range(len(walk_lengths_list)):

            for j in range(number_of_trials):
                l_coords = 0
                m_coords = 0
                for k in range(walk_lengths_list[i]):

                    reg_coords = reg_steps()
                    l_coords += reg_coords[0]
                    m_coords += reg_coords[1]
                if i == 0:
                    reg_list.append((l_coords,m_coords))
                else:
                    reg_list2.append((l_coords,m_coords))

                # print("index #" , i, "trial #", j+1,  '(',x_coords, y_coords,')')

        if len(walk_lengths_list) > 1:
            print("Reg random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(reg_list), 'CV =', find_cv(reg_list))
            print('Max =', find_max(reg_list), 'Min =', find_min(reg_list))

            print("Reg random walk of", walk_lengths_list[1], "steps")
            print('Mean =',find_median(reg_list2), 'CV =', find_cv(reg_list2))
            print('Max =', find_max(reg_list2), 'Min =', find_min(reg_list2))

        else:
            print("Reg random walk of", walk_lengths_list[0], "steps")
            print('Mean =',find_median(reg_list), 'CV =', find_cv(reg_list))
            print('Max =', find_max(reg_list), 'Min =', find_min(reg_list))

    else:
        print("Hi there")


def plot():
    '''Plotting points on screen'''
    t_f = turtle
    t_f.screensize(300,400)
    t_f.shapesize(.8)
    t_f.shape('circle')
    t_f.color('black')
    t_f.speed(5)
    pa_list = []

    for j in range(50):
        x_coords = 0
        y_coords = 0
        for k in range(100):
            j = 0
            k = 0
            pa_coords = pa_steps()
            x_coords += pa_coords[0]
            y_coords += pa_coords[1]
        pa_list.append((j+x_coords,k+y_coords))

    for i in range(len(pa_list)):
        x_coords = pa_list[i][0]
        y_coords = pa_list[i][1]
        t_f.penup()
        t_f.goto(x_coords*5, y_coords*5)
        t_f.pendown()
        t_f.stamp()

    t_f.shape('square')
    t_f.color('green')
    t_f.speed(5)
    ma_list = []

    for j in range(50):
        x_coords = 0
        y_coords = 0
        for k in range(100):

            ma_coords = mi_ma_steps()
            x_coords += ma_coords[0]
            y_coords += ma_coords[1]
        ma_list.append((x_coords,y_coords))

    for i in range(len(pa_list)):
        x_coords = ma_list[i][0]
        y_coords = ma_list[i][1]
        t_f.penup()
        t_f.goto(x_coords*5, y_coords*5)
        t_f.pendown()
        t_f.stamp()

    t_f.shape('triangle')
    t_f.color('red')
    t_f.speed(5)
    reg_list = []

    for j in range(50):
        x_coords = 0
        y_coords = 0
        for k in range(100):

            reg_coords = reg_steps()
            x_coords += reg_coords[0]
            y_coords += reg_coords[1]
        reg_list.append((x_coords,y_coords))

    for i in range(len(pa_list)):
        x_coords = reg_list[i][0]
        y_coords = reg_list[i][1]
        t_f.penup()
        t_f.goto(x_coords*5, y_coords*5)
        t_f.pendown()
        t_f.stamp()


def main():
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

    simulate(list_walk_lengths, trials, person)
    plot()
    save_to_image()
if __name__ == "__main__":
    main()
