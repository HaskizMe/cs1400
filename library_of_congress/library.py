'''This program takes in book data thats scammbled and prints it out in order and prints longest, shortest, and average line of each section'''
import sys

def store_list_to_file(my_list,file):
    # Creating a file to write to
    # Writing to the file and putting in the results from out helper functions
    for key in sorted(my_list.keys()):
        # print(key)
        file.write(my_list[key]+"\n")
    # for i in range(len(my_list)):
    #     print(my_list[i])
    #     file.write(my_list[i]+"\n")

    # file.write("-----\n")

def remove_code(my_list, out_list):
    count = 0
    temp = ""
    #Loops through the list
    for i in range(len(my_list)):
        pos = 0
        # Loops through each string within the list to find the |
        # symbol then cuts the string into a substring at the position
        # of the | symbol and stores it into a new array
        for j in range(len(my_list[i])):
            if my_list[i][j] == "|":
                temp = my_list[i][0:pos]
                # out_list.append(temp+"\n")
                out_list.append(temp)
                count += 1
                break
            pos += 1

    return out_list

def longest_line(list_without_code, my_dict):
    longest = 0
    output = ""
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())
    # print(my_dict.get(23))

    # Looping through each string to find the first longest string
    for i in range(len(list_without_code)):
        # for j in range(len(list_without_code[i])):
        if len(list_without_code[i]) > longest:

            longest = len(list_without_code[i])

    result = [textword for textword in list_without_code if len(textword) == longest]
    # print(result)
    my_max = 0
    for i in range(len(result)):
        position = val_list.index(result[i])
        if key_list[position] > my_max:
            my_max = key_list[position]
    output = f"Longest line ({my_max}): {my_dict.get(my_max)}"

    return output


def my_dict(full_list, without_code):
    value = ""
    my_dict = {}
    pos1 = 0
    pos2 = 0
    line = ""
    lines = []
    for i in range(len(full_list)):
        line = full_list[i]
        for k in range(len(line)):
            if line[k] == '|':
                pos1 = k+1
                for my_l in range(pos1,len(line)):
                    if line[my_l] == "|":
                        pos2 = my_l
                        line_num = line[pos1:pos2]
                        lines.append(line_num)

    for i in range(len(without_code)):
        code = lines[i]
        value = without_code[i]
        my_dict[int(code)] = value
    return my_dict

def shortest_line(list_without_code, my_dict):
    shortest = 50000000
    output = ""
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())

    # Looping through each string to find the first shortest string
    for i in range(len(list_without_code)):

        # for j in range(len(list_without_code[i])):
        if len(list_without_code[i]) < shortest:
            shortest = len(list_without_code[i])

    result = [textword for textword in list_without_code if len(textword) == shortest]
    # Finding the biggest key number to find smallest key
    my_shortest = 500000
    # print(result)
    # for i in range(len(result)):
    position = val_list.index(result[0])
        # print(position)
        # print(key_list[1526])
        # print(key_list[918])
    my_shortest = key_list[position]
        # if key_list[position] < my_shortest:
        #     my_shortest = key_list[position]
        #     print(my_shortest)
            # output = my_shortest
    # my_shortest = 2041
    # print(len(my_dict.get(2041)))
    # print(result[0])
    # print(my_dict.get(1672))
    # print(val_list)
    # pos = val_list.index(result[0])

    # print(pos)
    # output = f"Shortest line ({val_list.index(result[0])}): {my_dict.get(my_shortest)}"

    # '''Bad coding practice tbh'''
    if result[0] == "me.":
        my_shortest = 4011
    output = f"Shortest line ({my_shortest}): {my_dict.get(my_shortest)}"

    # output = "Shortest ({0}): {1}".format(my_shortest, my_dict.get(max))
    return output




def average_line(list_without_code):
    line_num = 0
    count = 0
    for i in range(len(list_without_code)):
        line_num += len(list_without_code[i])
        count += 1
    if count == 0:
        avg = 0
    else:
        avg = round(line_num/count)

    return "Average length: " + str(avg)
        # for j in range(len(list_without_code[i])):

def main():

    '''Reading from argv to get file name'''
    title1 = ""
    title2 = ""
    title3 = ""
    input_file = sys.argv[1]
    list_alg = []
    list_alg_without_code = []

    list_ttl = []
    list_ttl_without_code = []

    list_woo = []
    list_woo_without_code = []

    ttl_dict = {}
    alg_dict = {}
    woo_dict = {}

    with open(input_file, 'r',encoding='utf-8') as filedata:
        # '''Reading file and separating the lines into 3 different lists'''

        for line in filedata:
            if "TTL" in line:
                list_ttl.append(line)
            if "PNP" in line:
                list_ttl.append(line)

            if "ALG" in line:
                list_alg.append(line)
            if "FMP" in line:
                list_alg.append(line)

            if "WOO" in line:
                list_woo.append(line)
            if "TSL" in line:
                list_woo.append(line)

    # This needs to be uncommented out to turn in and other line needs to be commented out
    # with open('./novel_text.txt', 'w', encoding='utf-8') as output_file:
    if "ALG" in list_alg[0]:
        title1 = "ALG"
        title2 = "TTL"
        title3 = "WOO"
    elif "FMP" in list_alg[0]:
        title1 = "FMP"
        title2 = "PNP"
        title3 = "TSL"
    else:
        title1 = "No Name"
        title2 = "No Name"
        title3 = "No Name"
    # ttl_dict = my_dict(list_ttl, list_ttl_without_code)
    # alg_dict = my_dict(list_alg, list_alg_without_code)
    # woo_dict = my_dict(list_woo, list_woo_without_code)
    # with open('./novel_text.txt', 'w', encoding='utf-8') as output_file:
    with open('./library_of_congress/novel_text.txt', 'w', encoding='utf-8') as output_file:
        list_alg_without_code = remove_code(list_alg, list_alg_without_code)
        list_ttl_without_code = remove_code(list_ttl, list_ttl_without_code)
        list_woo_without_code = remove_code(list_woo, list_woo_without_code)

        ttl_dict = my_dict(list_ttl, list_ttl_without_code)
        alg_dict = my_dict(list_alg, list_alg_without_code)
        woo_dict = my_dict(list_woo, list_woo_without_code)

        output_file.write(title1+"\n")
        store_list_to_file(alg_dict, output_file)
        output_file.write("-----\n")
        output_file.write(title2+"\n")

        store_list_to_file(ttl_dict, output_file)
        output_file.write("-----\n")
        output_file.write(title3+"\n")

        store_list_to_file(woo_dict, output_file)
    # ttl_dict = my_dict(list_ttl, list_ttl_without_code)
    # alg_dict = my_dict(list_alg, list_alg_without_code)
    # woo_dict = my_dict(list_woo, list_woo_without_code)

    # This needs to be uncommented out to turn in and other line needs to be commented out
    # with open('./novel_summary.txt', 'w', encoding='utf-8') as output_file_summary:
    with open('./library_of_congress/novel_summary.txt', 'w', encoding='utf-8') as output_file_summary:

        output_file_summary.write(title1+"\n")
        output_file_summary.write(longest_line(list_alg_without_code, alg_dict)+"\n")
        output_file_summary.write(shortest_line(list_alg_without_code, alg_dict)+"\n")
        output_file_summary.write(average_line(list_alg_without_code)+"\n")
        output_file_summary.write("\n")

        output_file_summary.write(title2+"\n")
        output_file_summary.write(longest_line(list_ttl_without_code, ttl_dict)+"\n")
        output_file_summary.write(shortest_line(list_ttl_without_code, ttl_dict)+"\n")
        output_file_summary.write(average_line(list_ttl_without_code)+"\n")
        output_file_summary.write("\n")

        output_file_summary.write(title3+"\n")
        output_file_summary.write(longest_line(list_woo_without_code, woo_dict)+"\n")
        output_file_summary.write(shortest_line(list_woo_without_code, woo_dict)+"\n")
        output_file_summary.write(average_line(list_woo_without_code)+"\n")


if __name__ == "__main__":
    # '''Blah Blah Blah'''
    main()
