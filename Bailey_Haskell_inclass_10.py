import time
'''This program does a similar sequence of the fibonacci sequence but with different ways 
and calculates the time it takes for each'''

def recursive(n):
    # Recursive Function
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return recursive(n-1) + recursive(n-2) + recursive(n-3)
    
def iterative(n):
    # Iterative function
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 0
        b = 1
        c = 2
        result = 0
        for i in range(3, n+1):
            result = a + b + c
            a = b
            b = c
            c = result
        return result
 
l = [0,1,2]
def memoization(n):
    # Memoization function
    n = abs(n)
    if n < len(l):
        return l[n]
    
    else:
        for i in range(len(l), n+1):
            sum = l[i-1] + l[i-2] + l[i-3]
            l.append(sum)
        return l[n]


def main():
    # timing recursive function
    start_time = time.time()
    for i in range(0,30):
        print("Recursive(", i + 1 , ")", recursive(i))
    end_time = time.time()
    print("Time to execute - recursive" ,end_time - start_time)
    print("")


    # timing Iterative function
    start_time = time.time()
    for i in range(0,30):
        print("Iterative(", i + 1 , ")", iterative(i))
    end_time = time.time()
    print("Time to execute - iterative" ,end_time - start_time)
    print("")


    # timing memoization function
    start_time = time.time()
    for i in range(0,30):
        print("Memoization(", i + 1 , ")", memoization(i))
    end_time = time.time()
    print("Time to execute - memoization" , end_time - start_time)
    print("")

if __name__ == "__main__":
    main()