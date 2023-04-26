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

def convert_to_decimal(num):
    if num > 1000000:
        return f'{round(num / 1000000, 1)}M'
    else:
        return f'{round(num / 1000000, 1)}K'
    
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
    num1 = 0
    num2 = 0
    for i in range(len(my_list)):

        for j in range(len(my_list[i])):
            # Checking years for John F. Kennedy
            if my_list[i][0] == '1961' or my_list[i][0] == '1962' or my_list[i][0] == '1963':
                if my_list[i][0] == '1961':
                    my_list[i].pop(0)
                    my_list[i].sort()
                    num1 = my_list[i][-1]
                elif my_list[i][0] == '1963':
                    my_list[i].pop(0)
                    my_list[i].sort()
                    num2 = my_list[i][-1]
                    my_dict['John F. Kennedy'] = convert_to_decimal(round((num2 - num1)*1000,1))

            # Checking years for Lyndon B. Johnson
            elif my_list[i][0] == '1964' or my_list[i][0] == '1965' or my_list[i][0] == '1966' or my_list[i][0] == '1967' or my_list[i][0] == '1968' or my_list[i][0] == '1969':
                if my_list[i][0] == '1964':
                    my_list[i].pop(0)
                    my_list[i].sort()
                    num1 = my_list[i][-1]
                    print(num1)
                elif my_list[i][0] == '1969':
                    my_list[i].pop(0)
                    my_list[i].sort()
                    num2 = my_list[i][-1]
                    print(num2)
                    my_dict['Lyndon B. Johnson'] = convert_to_decimal(round((num2 - num1)*1000,1))

            # Checking years for Richard M. Nixon
            elif my_list[i][0] == '1964' or my_list[i][0] == '1965' or my_list[i][0] == '1966' or my_list[i][0] == '1967' or my_list[i][0] == '1968' or my_list[i][0] == '1969':
                if my_list[i][0] == '1964':
                    my_list[i].pop(0)
                    my_list[i].sort()
                    num1 = my_list[i][-1]
                    print(num1)
                elif my_list[i][0] == '1969':
                    my_list[i].pop(0)
                    my_list[i].sort()
                    num2 = my_list[i][-1]
                    print(num2)
                    my_dict['Lyndon B. Johnson'] = convert_to_decimal(round((num2 - num1)*1000,1))

    print(my_dict.get('John F. Kennedy'))
    print(my_dict.get('Lyndon B. Johnson'))


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
