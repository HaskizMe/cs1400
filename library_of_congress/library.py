import sys

'''HINT**** Remeber to change file path before turning in'''


def store_list_to_file(list,file):
    # Creating a file to write to 
    # Writing to the file and putting in the results from out helper functions
    for i in range(len(list)):
        file.write(list[i]+"\n")

    # file.write("-----\n")

def remove_code(list, out_list):
    count = 0
    temp = ""
    '''Loops through the list'''
    for i in range(len(list)):
        pos = 0
        '''Loops through each string within the list to find the |
        symbol then cuts the string into a substring at the position
        of the | symbol and stores it into a new array'''
        for j in range(len(list[i])):
            if(list[i][j] == "|"):
                temp = list[i][0:pos]
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

    '''Looping through each string to find the first longest string'''
    for i in range(len(list_without_code)):

        for j in range(len(list_without_code[i])):
            if(len(list_without_code[i]) > longest or list_without_code[i] == longest):
                longest = len(list_without_code[j])

    result = [textword for textword in list_without_code if len(textword) == longest]
    # print(result)
    max = 0
    for i in range(len(result)):
        position = val_list.index(result[i])
        if(key_list[position] > max ):
            max = key_list[position]

    output = "Longest line ({0}): {1}".format(max, my_dict.get(max))
    return output


def my_dict(full_list, without_code):
    value = ""
    dict = {}
    pos1 = 0
    pos2 = 0
    line = ""
    lines = []
    for i in range(len(full_list)):
        line = full_list[i]
        for k in range(len(line)):
            if(line[k] == '|'):
                pos1 = k+1
                for l in range(pos1,len(line)):
                    if(line[l] == "|"):
                        pos2 = l
                        line_num = line[pos1:pos2]
                        lines.append(line_num)

    for i in range(len(without_code)):
        code = lines[i]
        value = without_code[i]
        dict[int(code)] = value
    return dict

def shortest_line(list_without_code, my_dict):
    shortest = 2000
    output = ""
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())

    '''Looping through each string to find the first longest string'''
    for i in range(len(list_without_code)):

        for j in range(len(list_without_code[i])):
            if(len(list_without_code[i]) < shortest or list_without_code[i] == shortest):
                shortest = len(list_without_code[j])

    result = [textword for textword in list_without_code if len(textword) == shortest]
    # print(result)
    max = 0
    for i in range(len(result)):
        position = val_list.index(result[i])
        if(key_list[position] > max ):
            max = key_list[position]

    output = "Shortest ({0}): {1}".format(max, my_dict.get(max))
    return output




def average_line(list_without_code):
    line_num = 0
    count = 0
    for i in range(len(list_without_code)):
        line_num += len(list_without_code[i])
        count += 1
    avg = round(line_num/count)

    return "Average length: " + str(avg)
        # for j in range(len(list_without_code[i])):

def main():
    input_file = sys.argv[1]
    # read_file(input_file)
    count = 0
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

        # file = open('./library_of_congress/novel_text.txt', 'w', encoding='utf-8')


        for line in filedata:
            if("TTL" in line):
                # print(line.rstrip('\n'))
                # file.write(line)
                list_TTL.append(line)
                count += 1
            if("ALG" in line):
                # print(line.rstrip('\n'))
                # file.write(line)

                list_ALG.append(line)
                count += 1
            if("WOO" in line):
                # print(line.rstrip('\n'))
                # file.write(line)

                list_WOO.append(line)
                count += 1
        # file.close()
    filedata.close()
    # print(list_WOO)    
    # print("count:", count)
    # print(list_ALG)
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