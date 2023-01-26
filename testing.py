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
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # (2) replace pass with your code
    # pass

if __name__ == "__main__":
    main()
