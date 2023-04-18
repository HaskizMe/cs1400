<<<<<<< HEAD
# # 1
# txt = input()
# first = txt[0]
# last = txt[-1]
# print("{} is the first character and {} is the last character".format(first, last))

# # 2
# txt = input()
# for i in range(len(txt)):
#     print(txt * len(txt))

# # 3
# txt = input()
# second_string = ""
# for char in txt:
#     if char.islower():
#         second_string += "l"
#     elif char.isupper():
#         second_string += "u"
#     else:
#         second_string += "-"

# print(second_string)

# # 4
# txt = input()
# midpoint = len(txt) // 2
# first_half = txt[:midpoint]
# second_half = txt[midpoint:]
# print(first_half)
# print(second_half)

# # 5
# txt = input()
# length = len(txt)
# swapped_string = ""
# for i in range(0, length - 1, 2):
#     swapped_string += txt[i + 1]
#     swapped_string += txt[i]

# print(swapped_string)
# txt = input()
# length = len(txt)
# swapped_string = ""

# for i in range(0, length - 1, 2):
#     swapped_string += txt[i + 1]
#     swapped_string += txt[i]

# print(swapped_string)
=======
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
>>>>>>> 61f71549ff62e72d1c3ce31eabd33c0bc720d22e




<<<<<<< HEAD
# my_string = "Hobbes"
# vowels = "aeiou"

# for vowel in vowels:
#     my_string = my_string.replace(vowel, "*")
=======
# string = "Mar  9 11:10:37 server spamdyke[29207]: DENIED_RDNS_MISSING from: spam@mail.spam-source.net to: recipient@example.com origin_ip: 203.0.113.66 origin_rdns: (unknown) auth: (unknown) encryption: (none) reason: (empty)"
# first = string.find('@')
# second = string.find('@', first+1)
# print(first)
# print(second)

# # print(len("Mar  9 11:10:37 server spamdyke[29207]: DENIED_RDNS_MISSING from: spam@mail.spam-source.net to: recipient@example.com origin_ip: 203.0.113.66 origin_rdns: (unknown) auth: (unknown) encryption: (none) reason: (empty)"))
>>>>>>> 61f71549ff62e72d1c3ce31eabd33c0bc720d22e

# print(my_string)

<<<<<<< HEAD
print("testing")
=======

# import sys
# import os.path


# def find_email(line):
#     email = ""
#     for i in range(len(line)):
#         if(line[i] == '@'):
#             at_index = line.find('@')
#             if(line.count('@') > 1):
#                 # print("second @")
#                 at_index2 = line.find('@', at_index+1)
   
#                 space2 = line.find(' ',at_index2)
#                 space1 = line.rfind(' ',0,at_index2) + 1
#                 # if(space2 == -1):
#                 #     space2 = (len(line))-1
            
#                 email = line[space1:space2]
#                 # return email
#             space2 = line.find(' ',at_index)
#             space1 = line.rfind(' ',0,at_index) + 1
#             if(space2 == -1):
#                 space2 = (len(line))-1
            
#             email = line[space1:space2]
#             # return email
        
#     return email

# def read_file(file):
#     result = []
#     with open(file, 'r') as my_file:
#         for line in my_file:
#             # find_email(line)
#             if(find_email(line) != ""):
#                 result.append(find_email(line))
#     print_emails(result)

# def print_emails(my_list):
#     for i in range (len(my_list)):
#         print(i+1,my_list[i])
# def main():
#     if (os.path.isfile(sys.argv[1])):
#         input_file = sys.argv[1]
#         read_file(input_file)
# if __name__ == "__main__":
#     main()
print("hello world")
>>>>>>> 61f71549ff62e72d1c3ce31eabd33c0bc720d22e
