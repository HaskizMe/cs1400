'''
This program is supposed to add, subtract, multiply, and divide two numbers
'''
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

    try:
        x = float (input("Enter first number: "))
        y = float (input("Enter second number: "))
        addition(x,y)
        subtraction(x,y)
        multiplication(x,y)
        division(x,y)
    except ValueError:
        print("Please enter a number")

if __name__ == "__main__":
    # Calling main function
    main()