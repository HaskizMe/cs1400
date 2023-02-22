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
x = 5

if(x == 4 or x == 5):
    print("true")