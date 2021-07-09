from sys import argv


def employees_salary():
    working_hours, rate_per_hour, reward = map(float, argv[1:])
    print(f"Employees salary - {working_hours * rate_per_hour + reward}")

employees_salary()
