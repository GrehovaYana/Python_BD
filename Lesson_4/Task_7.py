def fact(n):
    s = 1
    for el in range(n + 1):
        yield f"{el}! = {s}"
        s *= el + 1


for el in fact(int(input("Random num for factorial: "))):
    print(el)
