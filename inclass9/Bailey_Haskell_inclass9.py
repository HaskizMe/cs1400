import sys
import os.path

'''This program searches and prints all emails that are found in file'''

# Finds the emails and appends them to list
def find_email(my_list):
    result = []
    # Looping through list and looking at each line
    for i in range(len(my_list)):
        at_index = 0

        # Loops through if theres more than one email
        for j in range(my_list[i].count('@')):
            # If @ symbol is found then executes block
            if(my_list[i].count('@') > 0):

                # Finds the @ symbol index
                at_index = my_list[i].find('@', at_index+1)
                # Finds the space before the @ symbol
                space2 = my_list[i].find(' ',at_index)
                # Finds the space after the @ symbol
                space1 = my_list[i].rfind(' ',0 ,at_index) + 1
                # If there's no space after the @ symbol then just go to the end of the string
                if(space2 == -1):
                    space2 = (len(my_list[i]))-1
                # Makes a sub string and cuts out the email
                email = my_list[i][space1:space2]
                # Appends email to list
                result.append(email)
    # Return result list
    return result

def read_file(file):
    my_data = []
    # Open file and append all lines to a list
    with open(file, 'r') as my_file:
        for line in my_file:
            my_data.append(line)
    # Calls find emails function
    my_list = find_email(my_data)
    # Calls print emails function
    print_emails(my_list)

def print_emails(my_list):
    # Loops through results list and prints contents
    print("Printing all emails")
    for i in range (len(my_list)):
        print(i+1,my_list[i])

def main():
    # Checks to see if file exists
    if (os.path.isfile(sys.argv[1])):
        input_file = sys.argv[1]
        read_file(input_file)
    else:
        print("file does not exist")

# Calls main function
if __name__ == "__main__":
    main()