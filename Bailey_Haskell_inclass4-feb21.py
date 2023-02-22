'''
Calculating the Min, Max, Median, and Average grades of each student
'''
import csv
import statistics

# Calculating miniumum
def min(list):
    min = list[0]
    for i in range(len(list)):
        if(list[i] < min):
            min = list[i]
    return min

# Calculating maxium
def max(list):
    max = list[0]
    for i in range(len(list)):
        if(list[i] > max):
            max = list[i]
    return max

# Calculating average
def average(list):
    total = 0
    for i in range(len(list)):
        total = total + list[i]
    total = total / len(list)
    total = round(total, 2)
    return total

# Calculating median
def median(list):
    return statistics.median(list)

# Main function
def main():

    # Opening csv file and reading through it
    # Appending all the data to a new array
    data = []
    with open("./input.csv" , 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            data.append(row)
    # Making two arrays to store just the grades and just the class numbers
    grades = []
    classNumbers = []
    # Outer loop is looping through and not including the top row
    for k in range(1,len(data)):
        # Makes a new array each time
        singleStudent = []
        # Looping through not including the first column with class numbers
        for l in range(1,len(data[0])):
            # Appending the refined data to a new list and sorting it from biggest to smallest
            singleStudent.append(int(data[k][l]))
            singleStudent.sort(reverse=True)
        # Appending that new array to a final 2D array called grades
        grades.append(singleStudent)
    # Grabbing just the class numbers and storing them in their own array
    for x in range(1,len(data)):
        classNumbers.append(data[x][0])


    # Writing to the csv file
    with open("./output.csv" , 'w', newline = '') as file:
        writer = csv.writer(file)
        #writing the header
        writer.writerow(["" , "Min","Max", "Median", "Avg"])
        # Looping through and writing out each row and calculations for the data
        for x in range(len(grades)):
            writer.writerow([classNumbers[x], min(grades[x]), max(grades[x]), median(grades[x]), average(grades[x])] )
    pass

if __name__ == "__main__":
    main()