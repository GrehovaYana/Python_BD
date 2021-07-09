from itertools import count,cycle

for el in count(9):
    if el > 25:
        break
    else:
        print(el)

#
i = 0
for n in cycle (["cat","dog",1,2, True]):
    if i > 13:
        break
    print(n)
    i +=1

