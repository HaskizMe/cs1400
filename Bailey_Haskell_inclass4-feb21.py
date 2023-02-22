'''
Ranking the students based on their grades
'''
import csv

def main():
    #input
    # students = int(input("How many students: "))
    # courses = int(input("How many courses: "))
    # grades = []

    # for i in range(students):
    #     singleStudent = []
    #     for j in range(courses):
    #         print('Grades for Stu#,', i+1, 'course#' , j+1)
    #         g = int(input())
    #         singleStudent.append(g)
    #     grades.append(singleStudent)

    # rank = []

    # for idx in range(len(grades)):
    #     total = sum(grades[idx])
    #     rank.append([total, idx+1])
    # rank.sort(reverse=True)

    # for idx, value in enumerate(rank):
    #     print('Student#', value[1], 'ranked', idx+1, 'total points:', value[0])
    # #calculation
    # #output
    data = []
    with open("C:/users/MFIAdmin/Desktop/Homework/cs1400/input.csv" , 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            data.append(row)
    grades = []

    for k in range(1,len(data)):
        singleStudent = []
        # grades.append(data[k])
        for l in range(1,len(data[0])):
            singleStudent.append(data[k][l])
        grades.append(singleStudent)
    print(grades)
    # Writing the top row
    with open("C:/users/MFIAdmin/Desktop/Homework/cs1400/output2.csv" , 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["" , "Min","Max", "Median", "Avg"])

    pass

if __name__ == "__main__":
    main()