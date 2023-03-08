'''
This program calculates the radius, area, and circumference of a circle
'''
import sys
import math
def radius(x2, y2):
    x1 = 0
    y1 = 0
    # using distance formula
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return round(distance,2)

def circum(a, b):
    # Circumference formula
    r = radius(a,b)
    circumference = 2*math.pi*r
    return round(circumference,2)

def area(a, b):
    r = radius(a,b)
    # Area formula
    area = math.pi*r**2
    return round(area,2)


def main():
# Checking to see if there are too many arguments
    if(len(sys.argv) > 4):
        print("Too many arguments")

    # Checking to see if there are too many arguments
    elif(len(sys.argv) < 4):
        print("Not enough arguments")

    # If there are the right amount of arguments then verify that the last 2 arguments are numbers
    else:
        calc = sys.argv[1]
        try:
            # Checking to see if the last 2 arguments are numbers
            x = float(sys.argv[2])
            y = float(sys.argv[3])
            # If Radius then call radius function
            if(calc.lower() == "radius"):
                print(radius(x, y))
            # if Area then call Area function
            elif(calc.lower() == "area"):
                print(area(x, y))
            # if Circum call cicum function
            elif(calc.lower() == "circum"):
                print(circum(x, y))
            # If none of those then print error message
            else:
                print("Please enter 'radius', 'area', or 'circum' for the first argument:") 
        # Throw error if the first 2 arguments are not numbers          
        except ValueError:
            print("please enter two numbers for the last two arguments")

if __name__ == "__main__":
    main()