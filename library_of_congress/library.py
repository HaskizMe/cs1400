'''HINT**** Remeber to change file path before turning in'''
'''This program takes in book data thats scammbled and prints it out in order and 
prints longest, shortest, and average line of each section'''
import sys

def store_list_to_file(my_list,file):
    # Creating a file to write to
    # Writing to the file and putting in the results from out helper functions
    for i in range(len(my_list)):
        file.write(my_list[i]+"\n")

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

    # Looping through each string to find the first longest string
    for i in range(len(list_without_code)):

        for j in range(len(list_without_code[i])):
            if(len(list_without_code[i]) > longest or list_without_code[i] == longest):
                longest = len(list_without_code[j])

    result = [textword for textword in list_without_code if len(textword) == longest]
    # print(result)
    my_max = 0
    for i in range(len(result)):
        position = val_list.index(result[i])
        if key_list[position] > my_max:
            my_max = key_list[position]

    output = "Longest line ({0}): {1}".format(my_max, my_dict.get(my_max))
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
                for l in range(pos1,len(line)):
                    if line[l] == "|":
                        pos2 = l
                        line_num = line[pos1:pos2]
                        lines.append(line_num)

    for i in range(len(without_code)):
        code = lines[i]
        value = without_code[i]
        my_dict[int(code)] = value
    return my_dict

def shortest_line(list_without_code, my_dict):
    shortest = 2000
    output = ""
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())

    # Looping through each string to find the first shortest string
    for i in range(len(list_without_code)):

        for j in range(len(list_without_code[i])):
            if(len(list_without_code[i]) < shortest or list_without_code[i] == shortest):
                shortest = len(list_without_code[j])

    result = [textword for textword in list_without_code if len(textword) == shortest]
    # print(result)
    my_shortest = 0
    for i in range(len(result)):
        position = val_list.index(result[i])
        if key_list[position] > my_shortest:
            my_shortest = key_list[position]

    output = "Shortest ({0}): {1}".format(my_shortest, my_dict.get(max))
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
    input_file = sys.argv[1]
    list_ALG = []
    list_ALG_without_code = []

    list_TTL = []
    list_TTL_without_code = []

    list_WOO = []
    list_WOO_without_code = []

    TTL_dict = {}
    ALG_dict = {}
    WOO_dict = {}

    with open(input_file, 'r',encoding='utf-8') as filedata:
        '''Reading file and separating the lines into 3 different lists'''

        for line in filedata:
            if "TTL" in line:
                list_TTL.append(line)

            if "ALG" in line:
                list_ALG.append(line)

            if "WOO" in line:
                list_WOO.append(line)

    filedata.close()

    # This needs to be uncommented out to turn in and other line needs to be commented out
    # output_file = open('./novel_text.txt', 'w')
    output_file = open('./library_of_congress/novel_text.txt', 'w', encoding='utf-8')
    list_ALG_without_code = remove_code(list_ALG, list_ALG_without_code)
    list_TTL_without_code = remove_code(list_TTL, list_TTL_without_code)
    list_WOO_without_code = remove_code(list_WOO, list_WOO_without_code)


    output_file.write("ALG\n")
    store_list_to_file(list_ALG_without_code, output_file)
    output_file.write("-----\n")
    output_file.write("TTL\n")

    store_list_to_file(list_TTL_without_code, output_file)
    output_file.write("-----\n")
    output_file.write("WOO\n")

    store_list_to_file(list_WOO_without_code, output_file)
    TTL_dict = my_dict(list_TTL, list_TTL_without_code)
    ALG_dict = my_dict(list_ALG, list_ALG_without_code)
    WOO_dict = my_dict(list_WOO, list_WOO_without_code)

    # This needs to be uncommented out to turn in and other line needs to be commented out
    # output_file_summary = open('./novel_summary.txt', 'w')
    output_file_summary = open('./library_of_congress/novel_summary.txt', 'w', encoding='utf-8')

    output_file_summary.write("ALG\n")
    output_file_summary.write(longest_line(list_ALG_without_code, ALG_dict)+"\n")
    output_file_summary.write(shortest_line(list_ALG_without_code, ALG_dict)+"\n")
    output_file_summary.write(average_line(list_ALG_without_code)+"\n")
    output_file_summary.write("\n")

    output_file_summary.write("TTL\n")
    output_file_summary.write(longest_line(list_TTL_without_code, TTL_dict)+"\n")
    output_file_summary.write(shortest_line(list_TTL_without_code, TTL_dict)+"\n")
    output_file_summary.write(average_line(list_TTL_without_code)+"\n")
    output_file_summary.write("\n")

    output_file_summary.write("WOO\n")
    output_file_summary.write(longest_line(list_WOO_without_code, WOO_dict)+"\n")
    output_file_summary.write(shortest_line(list_WOO_without_code, WOO_dict)+"\n")
    output_file_summary.write(average_line(list_WOO_without_code)+"\n")

    output_file.close()

if __name__ == "__main__":
    main()
