
'''
Bailey Haskell
2/8/23

This program takes in a number of students and grades and calculates the statistics of all the students
'''

# Finds the average of all the numbers in the list
def average(list):
    total = 0
    for i in range(len(list)):
        total = total + list[i]
    total = total / len(list)
    return total

# Finds the max value of all the numbers in the list
def max(list):
    max = list[0]
    for i in range(len(list)):
        if(list[i] > max):
            max = list[i]
    return max

# Finds the minimum value of all the numbers in the list
def min(list):
    min = list[0]
    for i in range(len(list)):
        if(list[i] < min):
            min = list[i]
    return min

# Calls all three functions and stores them in a list and returns that list
def find_statistics(list):
    statistics = []
    statistics.append(average(list))
    statistics.append(max(list))
    statistics.append(min(list))

    return statistics
    

def main():

    grades = []
    # Checking if input is 0 or less than zero
    while True:
        students = int (input("Enter how many students: "))
        if(students <= 0):
            print("Please enter a number greater than 0.")
        else:
            break
    # Taking in input based off of how many students there are
    for i in range(students):
    # Checking if input is 0 or less than zero
        while True:
            grade = int (input("Input grade: "))
            if(grade <= 0):
                print("Please enter a number greater than 0.")
            else:
                break
        # Appending grades to list
        grades.append(grade)
    # Calling find_statistics function and prints out the average, min, and max values
    print("Average =" , find_statistics(grades)[0])
    print("Max =" , find_statistics(grades)[1])
    print("Minimum =" , find_statistics(grades)[2])



if __name__ == "__main__":
    # Calling main function
    main()