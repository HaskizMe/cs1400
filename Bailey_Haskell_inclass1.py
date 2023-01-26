try:
    val = float (input("Enter a dividend: "))
    val2 = float (input("Enter a divisor: "))
    total = val / val2
    print(total)

except ValueError:
    print("Please enter a number")


