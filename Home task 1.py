# 1
greeting = "Hello"
name = "Yana"
surname = "Grehova"
city = "Saint-Petersburg"
print(f"{greeting},my  name is {name} {surname} .I am a citizen of {city} an where are you from ?")

place_of_residence = input("Enter your place of residence: ")
print(f"Hi, i am from {place_of_residence}")
print("Cool, how old are you?")
age = int(input("Enter your age: "))
print(f"I am {age} years old")

# 2
time_in_seconds = int(input("Enter the time in seconds: "))
h = time_in_seconds // 3600
m = time_in_seconds // 60 - h * 60
s = time_in_seconds % 60
print(f"{h:02}:{m:02}:{s:02}")

# 3
n = str(input("Enter your number:"))
print(f"{n}+{n + n}+{n + n + n}={int(n) + int(n + n) + int(n + n + n)}")

# 4
random_num = int(input("Enter random number: "))
greater_num = random_num % 10
random_num = random_num // 10
while random_num > 0:
    if random_num % 10 > greater_num:
        greater_num = random_num % 10
    random_num = random_num // 10
print(greater_num)

# 5
revenue = float(input("Enter revenue values:"))
costs = float(input("Enter costs values:"))
if revenue <= costs:
    print("Loss-costs are greater than revenue")
else:
    print("Profit-revenue is more than costs")
profit = revenue - costs
if profit > 0:
    print(f"Profit - to-revenue ratio = {100 * profit / revenue}%")
    number_of_employees = float(input("Enter number of employees:"))
    print(f"Profit per employee {profit / number_of_employees}")
else:
    print("You haven't earned anything")

# 6
while True:
    a = float(input("Enter first day result in km: "))
    b = float(input("Enter final result in km: "))
    day = 1
    while a < b:
        a += a * 0.1
        day += 1
    print(f"You gain the result in {day} days")
    break
