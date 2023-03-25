##problem one

# def sort_values(data):
#   sorted_values = tuple(sorted(data, key = lambda subtuple : sum([len(str(element)) for element in subtuple])))
#   return(sorted_values)
# print('Sorted Values:', sort_values(values))

#problem 2

# def remove_NA(data):
#     data_list = [list(subtuple) for subtuple in data]
#     updated_data = ()
#     for subtuple in data_list:
#         if 'N/A' in subtuple:
#             index_value = subtuple.index('N/A')
#             subtuple[index_value] = 'Test not taken yet'
#             updated_data += tuple(subtuple),
#         else: updated_data += tuple(subtuple),
#     return(updated_data)

# print("Updated Student Grades:", remove_NA(student_grades))

#problem 3
# dividend = (10, 100, 1000, 10000)
# divisor = (5, 50, 500, 5000)

# def find_quotient(tuple1, tuple2):
#   quotient = tuple((tuple1_element / tuple2_element) for tuple1_element, tuple2_element in zip(tuple1, tuple2))
#   return(quotient)

# print(find_quotient(dividend, divisor))


# problem 4

# numbers = (8, 5, 9, 14, 22)

# def find_adj_products(data):
#     numbers_adj_prod = tuple(left_element * right_element for left_element, right_element in zip(data, data[1:]))
#     return(numbers_adj_prod)

# print(find_adj_products(numbers))


#problem 5

# tuple_pairs = ((4, 5), (6, 14), (100, 40), (0, 83))

# def find_pair_diff(data):
#     pair_diff = [abs(subtuple[-1] - subtuple[0]) for subtuple in data]
#     return(tuple(pair_diff))

# def find_max_diff(data):
#     max_diff_subtuple = max(data, key = lambda subtuple: abs(subtuple[-1] - subtuple[0]))
#     max_diff = max(abs(subtuple[-1] - subtuple[0]) for subtuple in data)
#     return(max_diff_subtuple, max_diff)
    

# print(find_pair_diff(tuple_pairs))
# print(find_max_diff(tuple_pairs))


# lab 1 prompt 1
# def find_longest_string_and_freq(data):
#   data_split = data.split(" ")
#   longest_string = max(data_split, key = len)
#   longest_string_freq = data_split.count(longest_string)
#   return(longest_string, longest_string_freq)

# lab 1 prompt 2
# dog = 'cat'
# cat = 'dog'

# (dog, cat) = (cat, dog)
# print("Value of variable 'dog':", dog)
# print("Value of variable 'cat':", cat)


# lab 2 prompt 1
# def find_avg_grade(data):
#   sum_of_grades = 0
#   count = 0
#   for element in data:
#     sum_of_grades += element[1]
#     count += 1
#   return(round((sum_of_grades / count), 2))


# lab 2 prompt 2
# def find_unique_tuple_freq(data):
#   unique_tuple_freq = len(list(set(tuple(sorted(subtuple)) for subtuple in list(data))))
#   return(unique_tuple_freq)

# lab 3 prompt 1
# all_menu_items = ((sampler, ) + (antipasto_platter, ) + (zuchinni_sticks, ) + (garlic_bread, ) + (bruschetta_trio, ) + (stuffed_portabella, ) + (eggplant_parm_sandwich, ) + (chick_n_caesar_wrap, ) + (italian_deli, ) + (classic_burger, ) + (meatball_on_a_ciabatta, ) + (chick_n_parmesan, ) + (eggplant_parmesan, ) + (lasagna, ) + (spaghetti_meatballs, ) + (tiramisu, ) + (cannoli, ) + (chocolate_cake, ) + (chocolate_almond_croissant, ))
# print("All Menu Items:", all_menu_items)

# menu_item_ratings_list = [element[6] for element in all_menu_items]
# menu_item_ratings = tuple(menu_item_ratings_list)
# print("Menu Item Ratings:", menu_item_ratings)

# average_menu_item_rating = round((sum(menu_item_ratings)/len(menu_item_ratings)), 4)
# print("Average Menu Item Rating:", average_menu_item_rating)



# lab 3 prompt 2
# print("Menu Items Ranked In Order from Best to Worst:\n")
# for counter_value, (menu_item, menu_item_rating) in enumerate(sorted(zip(menu_items, menu_item_ratings), key = lambda element: element[1], reverse = True), 1):
#   print(counter_value, ":", menu_item, "with a rating of:", menu_item_rating, ".")
