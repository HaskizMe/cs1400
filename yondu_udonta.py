'''
Project Name: 
Author: 
Due Date: MM/DD/YYYY
Course: CS1400-zzz

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
'''

def main():
    '''
    Program starts here.
    '''

    try:
        # (1) replace pass with your code
        # pass
        reavers = int(input("How many Reavers:\n"))
        units = int(input("How many units:\n"))
        yondu_percentage = (units - (reavers * 3)) * .13 
        peter_percentage = ((units - (reavers * 3)) - yondu_percentage) * .11
        crew_share = (((units - (reavers * 3)) - yondu_percentage) - peter_percentage) / 20
        crew_share_int = int((((units - (reavers * 3)) - yondu_percentage) - peter_percentage) / 20)
        yondu_share = int(yondu_percentage + crew_share)
        peter_share = int(peter_percentage + crew_share)
        print("Yondu's Share: " + str(yondu_share))
        print("Peter's Share: " + str(peter_share))
        print("Crew: " + str(crew_share_int))
        # print(int())

        base_units = units
# For sure correct code
        units = units-((reavers-2) * 3)
        yondu = int((units * 13)/100)
        units = units - yondu
        peter = int((units *11) / 100)
        units = units - peter
        crew_share = int(units/reavers)
        rbf = units - (reavers * crew_share)
        yondu_share = yondu + crew_share
        peter_share = peter + crew_share
# My code which could be incorrect
        # yondu_percentage = (units - ((reavers - 2) * 3)) * .13
        # peter_percentage = ((units - ((reavers -2) * 3)) - yondu_percentage) * .11
        # crew_share = (((units - ((reavers - 2) * 3)) - yondu_percentage) - peter_percentage) / 20
        # print(crew_share)
        # yondu_share = int(yondu_percentage) + int(crew_share)
        # peter_share = int(peter_percentage + int(crew_share))
        # rbf = units - ((int(crew_share) * (reavers-2)) + yondu_share + peter_share + ((reavers - 2) * 3))

    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or base_units < 1:
        print(units)
        print("Enter positive integers for reavers and units123.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # (2) replace pass with your code
    # pass
    print("Yondu's share:",yondu_share)
    print("Peter's share:",peter_share)
    print("Crew:",int(crew_share))
    print("RBF:", int(rbf))

if __name__ == "__main__":
    main()
