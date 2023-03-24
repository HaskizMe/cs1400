import sys

'''HINT**** Remeber to change file path before turning in'''
'''DON'T EDIT THIS CODE'''

def store_list_to_file(list,file):
    # Creating a file to write to 
    # Writing to the file and putting in the results from out helper functions
    for i in range(len(list)):
        file.write(list[i])

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
                out_list.append(temp+"\n")
                # out_list.append(temp)
                count += 1
                break
            
            pos += 1

    return out_list

def longest_line(list, list_without_code):
    longest = 0
    line_num = ""
    line = ""
    output = ""
    pos1 = 1
    index = 0
    pos2 = 0
    occurences = []
    '''Looping through each string'''
    for i in range(len(list)):

        for j in range(len(list_without_code[i])):
            if(len(list_without_code[i]) > longest or list_without_code[i] == longest):
                longest = len(list_without_code[j])
                occurences = list[i]
                line = list[i]
                index = i
    # print(occurences)
    result = [textword for textword in list_without_code if len(textword) == longest]
    print(result)
    # print(list_without_code)
    # Have to -1 because in the list a \n follows and counts the n but not the \
    print(longest-1)
    # print(len(list_without_code[i]))
    # print(list_without_code)
    # print(list_without_code[i])

    # for i in range(len(list)):

    #     for j in range(len(list[i])):
    #         if(j > longest):
    #             longest = j
    #             line = list[i]
    #             index = i
    # print(longest)



    
    for k in range(len(line)):
        if(line[k] == '|'):
            pos1 = k+1
            for l in range(pos1,len(line)):
                if(line[l] == "|"):
                    pos2 = l
                    line_num = line[pos1:pos2]



    output = "Longest line ({0}): {1}".format(line_num, list_without_code[index])
    return output
def my_dict(full_list):
    key = 0
    value = ""
    dict = {}
    pos1 = 0
    pos2 = 0

    dict[code] = value
            # for l in range(pos1,len(line)):
            #     if(line[l] == "|"):
            #         pos2 = l
            #         line_num = line[pos1:pos2]


def shortest_line(list):
    pass
def average_line(list):
    pass
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
    print("count:", count)
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

    # print("ALG")
    # print(longest_line(list_ALG, list_ALG_without_code))
    print("TTL")

    print(longest_line(list_TTL, list_TTL_without_code))
    # print("WOO")

    # print(longest_line(list_WOO, list_WOO_without_code))





    output_file.close()






if __name__ == "__main__":
    main()