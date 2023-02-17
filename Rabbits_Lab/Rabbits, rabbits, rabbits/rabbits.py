"""
This function is used to calculate the number of months
it takes for there not to be enough cages for the total
number of bunnies
"""
def do_research(cages, adults, babies):
    month = 1
    # Opening file and writing the table information and then closing it
    with open("rabbits.csv", "w") as my_file:
        my_file.write("# Table of rabbit pairs\nMonth, Adults, Babies, Total\n")
    # Initializing the total 
    total = adults + babies
    # While loop to continue to print until the total is bigger than the number of cages
    while total < cages:
        total = adults + babies
        # Changes the ints to strings to be able to write to file
        total = repr(total)
        adults = repr(adults)
        babies = repr(babies)
        month = repr(month)
        # Writing information to file and then closing it
        with open("rabbits.csv", "a") as my_file:
            my_file.write(month + ", " + adults + ", " + babies + ", " + total + "\n")
        # Converting the strings back to ints and calculating the next row
        month = int(month)
        total = int(total)
        adults = int(adults)
        babies = int(babies)      
        month = month + 1
        babies = adults
        adults = total
    # Leaving while loop and printing the last month of when cages ran out. 
    month = month-1
    month = repr(month)
    with open("rabbits.csv", "a") as my_file:
        my_file.write("# Cages will run out in month " + month + "\n")
        my_file.write("")


