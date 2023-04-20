#1
def recursive_sum(num):
    """Recursively calculate sum from 0 to the parameter"""
    if num == 0:
        return 0
    else:
        return num + recursive_sum(num - 1)
        
print(recursive_sum(17))
#2
def list_sum(my_list):
    """Recursively calculate the sum of a list of numbers"""
    if len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + list_sum(my_list[1:])
#3
def bunny_ears(bunnies):
    """Recursively determine the number of bunny ears (2 per bunny)"""
    if bunnies == 0:
        return 0
    else:
        return 2 + bunny_ears(bunnies - 1)
#4
def reverse_string(word):
    if len(word) == 1:
        return word[0]
    else:
        return word[-1] + reverse_string(word[:-1])
#5

def get_max(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0], get_max(nums[1:]))





def recursive_power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recursive_power(base, exp - 1)