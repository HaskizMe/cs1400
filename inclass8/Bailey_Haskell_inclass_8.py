import csv
import sys
import os.path
'''This program reads a csv file and puts the gpa's in a tuple
it then uses that tuple to find the cumulative gpa and writes that to a new file
with the students name'''
def extract_data(file):
    names = []
    scores = []

    # Opening file and storing each line in a list
    with open(file, 'r') as filedata:
        csvReader = csv.reader(filedata, delimiter=',')
        for line in csvReader:
            # Grabbing just the names and putting them in a list
            # names.append(line[0])
            if not line.strip().split(','):
                print(line)
                scores.append(line)
    # loops through the lines and gets rid of the first element which is the names
    print(len(scores))
    # print(scores)
    for i in range(1, len(scores)):
        # print(scores)
        names.append(scores[i][0])
        # print(names)
        # print(i)
        scores[i].pop(0)
        for j in range(len(scores[1])):
            # Coverting the string to a float
            print(scores[i][j])
            # scores[i][j] = float(scores[i][j])

    # Calling the pack tuples function to store in a dictionary
    pack_tuples(names, scores)



def pack_tuples(names, scores):
    # Making two dictionaries one with all gpas and one with just cgpa
    all_gpas = {}
    cgpas = {}
    # Storing all gpas as a tuple to the student's names
    for i in range(len(names)):
        all_gpas[names[i]] = tuple(scores[i])
    # Storing just the cgpas into a different dictionary
    for i in range(len(scores)):
        # Calculating cgpa by calling function
        cgpas[names[i]] = calculateCGPA(scores[i])

    # Opening and writing to a new file
    file = "./cgpa.csv"
    with open(file, 'w') as filedata:
        # Writing a header
        filedata.write("Name - Cumulative GPA\n")
        # Looping through key and values and writing them to the file
        for k, v in cgpas.items():
            line = "{} - {}\n".format(k, v)       
            filedata.write(line)   


def calculateCGPA(unpackedGpas):
    # Returns the sum of the list divided by the number of elements in the list
    return round(sum(unpackedGpas) / len(unpackedGpas), 2)

def main():
    # Checking to see if there are too many arguments
    if(len(sys.argv) > 2):
        print("Too many arguments")

    # Checking to see if there are too many arguments
    elif(len(sys.argv) < 2):
        print("Not enough arguments")

    else:
        # Checking to see if file exists
        if (os.path.isfile(sys.argv[1])):
            input_file = sys.argv[1]
            extract_data(input_file)
        else:
            print("File does not exist")

if __name__ == "__main__":
    main()