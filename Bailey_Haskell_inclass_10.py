'''This program does a similar sequence of the fibonacci sequence but with different ways 
and calculates the time it takes for each'''
def recursive(one, two, three):
    
    # return recursive(one, two, three)
    pass

def memoization():
    pass

def iterative(first, second, third):
    arr = []
    arr.append(first)
    arr.append(second)
    arr.append(third)
    for i in range(30):
        fourth = first + second + third
        arr.append(fourth)
        first = second
        second = third
        third = fourth
    return arr

def main():
    first = 0
    second = 1
    third = 2
    # recursive(first, second, third)
    print(iterative(first, second, third))

    pass
if __name__ == "__main__":
    main()