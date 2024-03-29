import csv
import os
'''This program checks the facts of President Clinton's statment'''
# Reads the data and stores into list
def read_data(filename):
    '''Reads in data from BLS_private.csv'''
    my_list = []
    with open(filename) as csvfile:
        # Grabbing each row and storing it to a list
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            my_list.append(row)
    # Calling the store to list function
    store_to_list(my_list)

# Filters the data to show the year and numbers in their own seperate list
def store_to_list(data_list):
    '''Stores the information into a list'''
    for i in range(6):
        # removes the header rows
        data_list.pop(0)
    for i in range(len(data_list)):
        # Removes any empty spaces
        data_list[i] = list(filter(None, data_list[i]))
        for j in range(1, len(data_list[i])):
            # Converts all numbers to ints except for dates
            data_list[i][j] = int(data_list[i][j])

    store_list_to_dict(data_list)

def convert_to_decimal(num):
    return round(num / 1000000, 1)

def add_word(num):
    '''Formatting number to millions or thousands'''
    if num < 1.0:
        return f'{num} Thousand'
    else:
        return f'{num} Million'
    
def store_list_to_dict(my_list):
    '''Stores information from list to dictionary'''
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
            j = 0
            # Checking years for John F. Kennedy
            if my_list[i][j] == '1961' or my_list[i][0] == '1963':
                if my_list[i][j] == '1961':
                    my_list[i].pop(0)
                    # January 1961
                    num1 = my_list[i][0]
                elif my_list[i][0] == '1963':
                    my_list[i].pop(0)
                    # December 1963
                    num2 = my_list[i][-1]
                    my_dict['John F. Kennedy'] = convert_to_decimal(round((num2 - num1)*1000,1))

            # Checking years for Lyndon B. Johnson
            elif my_list[i][0] == '1964' or my_list[i][0] == '1968':
                if my_list[i][0] == '1964':
                    my_list[i].pop(0)
                    # January 1964
                    num1 = my_list[i][0]
                elif my_list[i][0] == '1968':
                    my_list[i].pop(0)
                    # December 1968
                    num2 = my_list[i][-1]
                    my_dict['Lyndon B. Johnson'] = convert_to_decimal(round((num2 - num1)*1000,1))

            # Checking years for Richard M. Nixon
            elif my_list[i][0] == '1969' or my_list[i][0] == '1974':
                if my_list[i][0] == '1969':
                    my_list[i].pop(0)
                    # January 1969
                    num1 = my_list[i][0]
                elif my_list[i][0] == '1974':
                    my_list[i].pop(0)
                    # Decemeber 1974
                    num2 = my_list[i][-1]
                    my_dict['Richard M. Nixon'] = convert_to_decimal(round((num2 - num1)*1000,1))


            # # Checking years Gerald R. Ford
            elif my_list[i][0] == '1975' or my_list[i][0] == '1976':
                if my_list[i][0] == '1975':
                    my_list[i].pop(0)
                    # January 1975
                    num1 = my_list[i][0]
                elif my_list[i][0] == '1976':
                    my_list[i].pop(0)
                    # Decemeber 1976
                    num2 = my_list[i][-1]
                    my_dict['Gerald R. Ford'] = convert_to_decimal(round((num2 - num1)*1000,1))

            # # Jimmy Carter
            elif my_list[i][0] == '1977' or my_list[i][0] == '1980':
                if my_list[i][0] == '1977':
                    my_list[i].pop(0)
                    # January 1977
                    num1 = my_list[i][0]
                elif my_list[i][0] == '1980':
                    my_list[i].pop(0)
                    # Decemeber 1980
                    num2 = my_list[i][-1]
                    my_dict['Jimmy Carter'] = convert_to_decimal(round((num2 - num1)*1000,1))

            # # Ronald Reagan
            elif my_list[i][0] == '1981' or my_list[i][0] == '1988':
                if my_list[i][0] == '1981':
                    my_list[i].pop(0)
                    # January 1981
                    num1 = my_list[i][0]
                elif my_list[i][0] == '1988':
                    my_list[i].pop(0)
                    # Decemeber 1988
                    num2 = my_list[i][-1]
                    my_dict['Ronald Reagan'] = convert_to_decimal(round((num2 - num1)*1000,1))

            # # George Bush
            elif my_list[i][0] == '1989' or my_list[i][0] == '1992':
                if my_list[i][0] == '1989':
                    my_list[i].pop(0)
                    # January 1969
                    num1 = my_list[i][0]
                elif my_list[i][0] == '1992':
                    my_list[i].pop(0)
                    # Decemeber 1974
                    num2 = my_list[i][-1]
                    my_dict['George Bush'] = convert_to_decimal(round((num2 - num1)*1000,1))
            
            # # Bill Clinton
            elif my_list[i][0] == '1993' or my_list[i][0] == '2000':
                if my_list[i][0] == '1993':
                    my_list[i].pop(0)
                    # January 1993
                    num1 = my_list[i][0]
                elif my_list[i][0] == '2000':
                    my_list[i].pop(0)
                    # Decemeber 2000
                    num2 = my_list[i][-1]
                    my_dict['Bill Clinton'] = convert_to_decimal(round((num2 - num1)*1000,1))

            # # George W. Bush 
            elif my_list[i][0] == '2001' or my_list[i][0] == '2008':
                if my_list[i][0] == '2001':
                    my_list[i].pop(0)
                    # January 2001
                    num1 = my_list[i][0]
                elif my_list[i][0] == '2008':
                    my_list[i].pop(0)
                    # Decemeber 2008
                    num2 = my_list[i][-1]
                    my_dict['George W. Bush'] = convert_to_decimal(round((num2 - num1)*1000,1))
            
            # # Barrack Obama
            elif my_list[i][0] == '2009' or my_list[i][0] == '2012':
                if my_list[i][0] == '2009':
                    my_list[i].pop(0)
                    # January 2009
                    num1 = my_list[i][0]
                elif my_list[i][0] == '2012':
                    my_list[i].pop(0)
                    # Decemeber 2012
                    num2 = my_list[i][-1]
                    my_dict['Barack Obama'] = convert_to_decimal(round((num2 - num1)*1000,1))
    
    write_to_conclusions(my_dict)


def write_to_conclusions(my_dict):
    '''Write conclusions to conclusions file'''
    if os.path.isfile("./was_clinton_right/conclusions.md"):
        with open("./was_clinton_right/conclusions.md" , 'w') as file:
        # f = open("/conclusions.md" , 'w')

            file.write("Democrats:\n")
            jobs = 0
            for keys, value in my_dict.items():
                
                if keys == 'John F. Kennedy' or keys == 'Lyndon B. Johnson' or keys == 'Jimmy Carter' or keys == 'Bill Clinton' or keys == 'Barack Obama':
                    jobs += value
                    value = add_word(value)
                    file.write(keys + ' ' + value +' jobs created\n')
                
            jobs = add_word(round(jobs,1))
            file.write('\nDemocrats total jobs created: ' + jobs + '\n')
            file.write('\n-----------------------------------------------\n')
            jobs = 0
            file.write("\nRepublicans:\n")
            for keys, value in my_dict.items():
                if keys == 'Richard M. Nixon' or keys == 'Gerald R. Ford' or keys == 'Ronald Reagan' or keys == 'George Bush' or keys == 'George W. Bush':
                    jobs += value
                    value = add_word(value)
                    file.write(keys + ' ' + value+' jobs created\n')

            jobs = add_word(round(jobs,1))
            file.write('\nRepublicans total jobs created: ' + jobs + '\n')
            conclusion = """\nRegarding clinton's statement he was right. According to the numbers
the democrats produced roughly 42 million jobs and the Republicans produced 24 million
jobs. Although the numbers may not be 100 percent accurate due to some terms ending
earlier than others, we can conclude that Clinton was right that the democrats have produced
way more jobs than the republicans in the shorter amount of time the democrats have been in office."""
            file.write(conclusion)
    else:
        print("error")

def main():
    '''Main function'''
    filename = "./was_clinton_right/BLS_private.csv"
    # filename = "/BLS_private.csv"
    if os.path.isfile(filename):
        read_data(filename)
    else:
        print("error")
if __name__ == "__main__":
    main()
