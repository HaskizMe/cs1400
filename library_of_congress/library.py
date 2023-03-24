import sys

def read_file(file):
    count = 0
    with open(file, 'r',encoding='utf-8') as filedata:
        for line in filedata:
            # print(line.rstrip())
            x = len(filedata.readlines())
            if("TTL" in line):
                print(line)
                count =+ 1
            if("ALG" in line):
                print(line)
                count =+ 1
            if("WOO" in line):
                print(line)
                count = count + 1
    print(x)
            

    # print(line_list)
def main():
    input_file = sys.argv[1]
    read_file(input_file)



if __name__ == "__main__":
    main()