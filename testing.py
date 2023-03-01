# # ########################################################
# # # DO NOT EDIT THE CODE IN THE SECTION BELOW
# # ########################################################
# # import sys

# # numbers = sys.argv[1:]
# # for i in range(len(numbers)):
# #   numbers[i] = int(numbers[i])
# # ########################################################
# # # Enter your code below
# # ########################################################
# # for i in range(len(numbers)):
# #   if(numbers[i]>10):
# #     numbers[i] = '*'

# # print(numbers)

# # problem 2
# ########################################################
# # DO NOT EDIT THE CODE IN THE SECTION BELOW
# ########################################################
# # import sys

# # my_list = sys.argv[1:]

# # ########################################################
# # # Enter your code below
# # ########################################################
# # if len(my_list) < 5:
# #   print(my_list * 3)
# # else:
# #   print(my_list)

# # problem 3
# # import sys

# # strings = sys.argv[1:]

# # strings.sort()
# # print(strings[0])

# # # problem 5
# # import sys

# # numbers = sys.argv[1:]
# # for i in range(len(numbers)):
# #   numbers[i] = int(numbers[i])

# # diff = numbers[1] - numbers[0]
# # numbers.append(numbers[len(numbers)-1]+diff)
# # numbers.append(numbers[len(numbers)-1]+diff)
# # print(numbers)

# # problem 6
# # import sys

# # number = int(sys.argv[1])
# # data = [[0 for i in range(number)] for j in range(number)]

# # for row in range(number):
# #   for column in range(number):
# #     if row == column:
# #       data[row][column] = 1
# #     print(f"{data[row][column]} ", end="")
# #   print()
# ########################################################
# # DO NOT EDIT THE CODE IN THE SECTION BELOW
# ########################################################
# import sys

# numbers = sys.argv[1:]
# for i in range(len(numbers)):
#   numbers[i] = int(numbers[i])

# ########################################################
# # Enter your code below
# ########################################################

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

