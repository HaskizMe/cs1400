import csv
def read_data(filename):
    my_list = []
    with open(filename) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        for row in csvReader:
            my_list.append(row)
    store_to_list(my_list)

def store_to_list(data_list):
    
    for i in range(6, len(data_list)):
        for j in range(1, len(data_list[i])):
            if(data_list[i][j].isdigit()):
                data_list[i][j] = int(data_list[i][j])
            print(data_list[i][j])
        # print(data_list[i])
    # print(data_list)
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
