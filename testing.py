# import sys

# test_file = sys.argv[1]

# line_count = 0
# char_count = 0

# with open(test_file, "r") as input_file:
#     line = input_file.readline()
#     while line != "":
#         line_count += 1
#         char_count += len(line)
#         line = input_file.readline()

# print("{} lines".format(line_count))
# print("{} characters".format(char_count))

#problem 2
# import sys, csv

# test_file = sys.argv[1]

# total1 = 0
# total2 = 0
# total3 = 0
# total4 = 0
# row_count = 0

# with open(test_file, "r") as input_file:
#     reader = csv.reader(input_file)
#     for num1, num2, num3, num4 in reader:
#         row_count += 1
#         total1 += int(num1)
#         total2 += int(num2)
#         total3 += int(num3)
#         total4 += int(num4)

# print("{} {} {} {}".format(total1/row_count, total2/row_count, total3/row_count, total4/row_count))

# problem 3 
# import sys

# test_file = sys.argv[1]

# with open(test_file, "r") as input_file:
#     lines = input_file.readlines()
#     lines.reverse()
#     for line in lines:
#         print(line)
# problem 4
# import sys, csv

# test_file = sys.argv[1]
# oldest_age = 0
# oldest_name = ""

# with open(test_file, "r") as input_file:
#     reader = csv.reader(input_file, delimiter="\t")
#     next(reader)
#     for name, age, career in reader:
#         if int(age) > oldest_age:
#             oldest_age = int(age)
#             oldest_name = name
            
# print("The oldest person is {}.".format(oldest_name))

#problem 5
# import sys, csv

# test_file = sys.argv[1]
# cities = []

# with open(test_file, "r") as input_file:
#     reader = csv.reader(input_file)
#     next(reader)
#     for city, country, latitude, longitude in reader:
#         if int(latitude) < 0:
#             cities.append(city)
            
# print("The following cities are in the Southern Hemisphere: ", end="")
# for city in cities:
#     if city == cities[-1]:
#         print(city + ".")
#     else:
#         print(city, end=", ")
# with open("student_folder/.labs/myanmar.txt", "r") as input_file:
#     lines = input_file.readlines()
#     for line in lines:
#         if "Burma" in line:
#             print(line.replace("Burma", "Myanmar"), end="")
#         else:
#             print(line, end="")



# # 1
# def find_key(d, v):
#   keys = list(d.keys())
#   values = list(d.values())
#   index = values.index(v)
#   return keys[index]

# #2

# def move_to_bottom(d, k):
#   if k not in d:
#     return 'The key is not in the dictionary'
#   else:
#     value = d.pop(k)
#     d[k] = value
#     return d

# #3
# def swap(d):
#   keys = d.keys()
#   values = d.values()
#   swapped_tuples = zip(values, keys)
#   value_types = [type(elem) for elem in values]
  
#   if type({}) in value_types or type([]) in value_types:
#     return 'Cannot swap the keys and values for this dictionary'
#   else:
#     new_dict = dict(swapped_tuples)
#     return new_dict

# #4
# def is_nested(d):
#   values = d.values()
#   value_types = [type(elem) for elem in values]
#   if type(()) in value_types or type([]) in value_types or type({}) in value_types:
#     return True
#   else:
#     return False

# #5
# import json

# def compare(f1, f2):
#   with open(f1) as file1, open(f2) as file2:
#     data1 = json.load(file1)
#     data2 = json.load(file2)
#     if data1 == data2:
#       return 'The dictionaries are equal'
#     else:
#       count1 = len(data1)
#       count2 = len(data2)
#       if count1 > count2:
#         return 'Dictionary 1 is longer than dictionary 2'
#       elif count2 > count1:
#         return 'Dictionary 2 is longer than dictionary 1'
#       else:
#         return 'Dictionary 1 and dictionary 2 have the same length'


#1
def key_position(d, k):
  keys = list(d.keys())

  if k in keys:
    return keys.index(k)
  else:
    return 'Key not found'

#2

#3

#4

#5

