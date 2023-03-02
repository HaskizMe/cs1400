# import sys

# test_file = sys.argv[1]

# line_count = 0
# char_count = 0

<<<<<<< HEAD
# with open(test_file, "r") as input_file:
#     line = input_file.readline()
#     while line != "":
#         line_count += 1
#         char_count += len(line)
#         line = input_file.readline()

# print("{} lines".format(line_count))
# print("{} characters".format(char_count))

import sys

results = []
test_file = sys.argv[1]
with open(test_file, "r") as input_file:
    for row in input_file:
        results.append(row)
=======
# for i in range(len(numbers)):
#   if(numbers[i]%2 ==0):
#     numbers[i] = "even"
#   else:
#     numbers[i] = "odd"
# print(numbers)

# exercise 1
# def avg(a,b):
#     if(isinstance(a, int) and isinstance(b,int)):
#         average = (a + b)/2
#         return average

#     else:
#         return "Please use two numbers as parameters"

# Exercise 2
# def odds_or_evens(bool, list):
#     evens = []
#     odds = []
#     if(bool):
#         for i in range(len(list)):
#             if(list[i] % 2 ==0):
#                 evens.append(list[i])
#         return evens
#     elif(not bool):
#         for i in range(len(list)):
#             if(list[i] % 2 != 0):
#                 odds.append(list[i])
#         return odds         

# Exercise 3
# def search_list(lst, term):
#     """Search for item in a list
#     Return the index if found
#     Return -1 if not found"""
#     for item in lst:
#         if item.lower() == term.lower():
#             return lst.index(item)
#     return -1

# Exercise 4
# import csv

# mlb_data = "student_folder/.exercises/mlb_data.csv"

# def best_team(file):
#     """Read a CSV of baseball data.
#     Return the team name with the most wins"""
#     with open(file, "r") as csv_file:
#         reader = csv.reader(csv_file)
#         next(reader)
#         most_wins = 0
#         best_team = ""
#         for row in reader:
#             if int(row[3]) > most_wins:
#                 most_wins = int(row[3])
#                 best_team = row[0]
#         return best_team

# Exercise 5
# def is_palindrome(str):
#   if(str.lower() == str[::-1].lower()):
#     return True
  
#   return False

>>>>>>> edda75409d1b77a4fea31cf1464cf6ed8d15b1ce
