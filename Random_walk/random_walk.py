import subprocess
import tempfile
import textwrap
import traceback
import turtle
import sys

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

def simulate(walk_lengths_list, number_of_trials, person):
    # helper_function(walk_lengths_list,plot())
    turtle.penup()
    turtle.forward(100)
    plot()
# turtle.moveto(0,1)
    pass

# def helper_function(list, plotter()):
#     return list
def plot():
    turtle.screensize(300, 400)
    turtle.circle(5)
    save_to_image()
    pass


def main():
    list_walk_lengths = sys.argv[1].split(',')
    list_walk_lengths[0] = int(list_walk_lengths[0])
    list_walk_lengths[1] = int(list_walk_lengths[1])
    trials = sys.argv[2]
    person = sys.argv[3]
    simulate(list_walk_lengths, trials, person)
    pass
if __name__ == "__main__":
    main()