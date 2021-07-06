def my_func(x, y):
    try:
        if x <= 0 or y >= 0:
            return "You entered a number with the wrong sign! Check it out one more time"
        else:
            return x ** y
    except ValueError:
        return "Something went wrong, check it out one more time "

print(my_func(int(input("Enter positive num: ")), int(input("Enter negative num: "))))


