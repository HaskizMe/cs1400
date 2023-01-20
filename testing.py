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
        yonduPercentage = (units - (reavers * 3)) * .13
        peterPercentage = ((units - (reavers * 3)) - yonduPercentage) * .11
        crewShare = (((units - (reavers * 3)) - yonduPercentage) - peterPercentage) / 20
        yonduShare = int(yonduPercentage + crewShare)
        peterShare = int(peterPercentage + crewShare)
        rbf = units - ((int(crewShare) * (reavers-2)) + yonduShare + peterShare + ((reavers - 2) * 3))
        
        print(yonduShare)
        print(peterShare)
        print(int(crewShare))
        print(int(rbf))
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
    pass

if __name__ == "__main__":
    main()