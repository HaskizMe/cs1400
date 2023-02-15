def do_research(cages, adults, babies):
    month = 1
    print("# Table of rabbit pairs")
    print("Month, Adults, Babies, Total")
    total = adults + babies
    while total < cages:
        total = adults + babies

        print('{0}, {1}, {2}, {3}\n'.format(month, adults, babies, total))        
        month = month + 1
        babies = adults
        adults = total
    print('The cages will run out in {0} months'.format(month-1))
    # print('{0}, {1}, {2}, {3}\n'.format(month, adults, babies, total))        
