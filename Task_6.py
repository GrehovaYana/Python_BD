shoes = []
references = {"brand": "", "price": "", "size": ""}
analytics = {"brand": [], "price": [], "size": []}
num = 0
while True:
    if input("Ready to order? y, Continue shopping c: ") == 'y':
        break
    num +=1
    references_list = references.copy()
    for n in references:
        name = input(f'Enter characteristics:"{n}": ')
        references_list[n] = int(name) if n == "price" or n == "size" else name
        analytics[n].append(references_list[n])
        num += 1
shoes.append((num, references_list))
print(f"Cart: {shoes}")
for key,value in analytics.items():
    print(f"{key: >10} : {value}")
