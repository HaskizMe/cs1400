<<<<<<< HEAD
for row in range(8):
  if row % 2 == 0:
    for column in range(8):
      if column % 2 == 0:
        print("X", end='')
      else:
        print("O", end='')
    print()
  else:
    for column in range(8):
      if column % 2 == 0:
        print("O", end='')
      else:
        print("X", end='')
    print()

=======
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
#   if(numbers[i]>10):
#     numbers[i] = '*'

# print(numbers)

# problem 2
########################################################
# DO NOT EDIT THE CODE IN THE SECTION BELOW
########################################################
# import sys

# my_list = sys.argv[1:]

# ########################################################
# # Enter your code below
# ########################################################
# if len(my_list) < 5:
#   print(my_list * 3)
# else:
#   print(my_list)

# problem 3
import sys

strings = sys.argv[1:]

sorted(strings)
print(strings[0])
>>>>>>> d20e99c558d12b9214da9d0f08478a04a1969eb0
