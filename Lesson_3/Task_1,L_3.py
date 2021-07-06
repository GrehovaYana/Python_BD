def devision_function(int1, int2):
    quotient = int1 // int2
    print(f"Quotient: {quotient}")
    pass


try:
    devision_function(int(input("Enter divisible num: ")), int(input("Enter divisor num: ")))
except ZeroDivisionError:
    print("Error")
