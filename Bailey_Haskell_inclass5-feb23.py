'''
This program is supposed to add, subtract, multiply, and divide two numbers using command line arguments
'''
import sys

# Addition function
def addition(x,y):
  print(x, " + ", y ," = ",x + y)

# Subtraction function
def subtraction(x,y):
  print(x, " - ", y ," = ",x - y)

# Multiplication function
def multiplication(x,y):
  print(x, " * ", y ," = ",x * y)

# Division function
def division(x,y):
  print(x, " / ", y ," = ",x / y)

# Main function
def main():
    # Checking to see if there are too many arguments
    if(len(sys.argv) > 4):
        print("Too many arguments")

    # Checking to see if there are too many arguments
    elif(len(sys.argv) < 4):
        print("Not enough arguments")

    # If there are the right amount of arguments then verify that the last 2 arguments are numbers
    else:
        try:
            # Verifying that the two inputs are integers
            x = float(sys.argv[2])
            y = float(sys.argv[3])

            # Checking to see if the input are negative integers
            if(x < 0 or y < 0):
                print("Please enter non negative integers")
            # Checking choices
            elif(sys.argv[1] == "mul"):
                multiplication(x,y)
            elif(sys.argv[1] == "add"):
                addition(x,y)
            elif(sys.argv[1] == "sub"):
                subtraction(x,y)
            elif(sys.argv[1] == "div"):
                division(x,y) 
            else:
                print("Please enter: 'mul', 'div', 'sub', or 'add'")
        # If input is not an integer throw error
        except ValueError:
            print("Please enter a number")
            
if __name__ == "__main__":
    # Calling main function
    main()