import csv
# Reads the data and stores into list
def read_data(filename):
    my_list = []
    with open(filename) as csvfile:
        # Grabbing each row and storing it to a list
        csvReader = csv.reader(csvfile, delimiter=',')
        for row in csvReader:
            my_list.append(row)
    # Calling the store to list function
    store_to_list(my_list)

# Filters the data to show the year and numbers in their own seperate list
def store_to_list(data_list):
    for i in range(6):
        # removes the header rows
        data_list.pop(0)
    for i in range(len(data_list)):
        # Removes any empty spaces
        data_list[i] = list(filter(None, data_list[i]))
        for j in range(1, len(data_list[i])):
            # Converts all numbers to ints except for dates
            data_list[i][j] = int(data_list[i][j])

    Store_list_to_dict(data_list)

def Store_list_to_dict(my_list):
    my_dict = {
        'John F. Kennedy': 0, 
        'Lyndon B. Johnson': [], 
        'Richard M. Nixon': [],
        'Gerald R. Ford': [],
        'Jimmy Carter': [],
        'Ronald Reagan': [],
        'George Bush': [],
        'Bill Clinton': [],
        'George W. Bush': [],
        'Barack Obama': [],
        }
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if my_list[i][0] == '1961' or my_list[i][0] == '1962' or my_list[i][0] == '1963':
                my_list[i].pop(0)
                num = my_dict.get('John F. Kennedy') + sum(my_list[i])
                my_dict['John F. Kennedy'] = num
    # print(sum(my_dict.get('John F. Kennedy')))
    print(my_dict.get('John F. Kennedy'))
    
    # for i in range(len(my_list)):
    #     for j in range(len(my_list[i])):
    #         my_list[i].pop(0)
    #         print(sum(my_list[i]))
    print(my_list[0])
    print(my_list[1])
    print(my_list[2])
    print((sum((my_list[0]))/ len(my_list[0])) + (sum((my_list[1]))/ len(my_list[1]))+ (sum((my_list[2]))/ len(my_list[2])))
def main():
    # John F. Kennedy 1961 - 1963 Democrat
    # Lyndon B. Johnson 1963 - 1969 Democrat
    # Richard M. Nixon 1969 - 1974 Republican
    # Gerald R. Ford 1974 - 1977 Republican
    # Jimmy Carter 1977 - 1981 Democrat
    # Ronald Reagan 1981 - 1989 Republican
    # George Bush 1989 - 1993 Republican
    # Bill Clinton 1993 - 2001 Democrat
    # George W. Bush 2001 - 2009 Republican
    # Barack Obama 2009 - 2017 Democrat
    filename = "./was_clinton_right/BLS_private.csv"
    read_data(filename)
if __name__ == "__main__":
    main()
