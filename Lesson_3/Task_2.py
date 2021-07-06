def personal_inf(**kwargs):
    return " ".join(kwargs.values())


print(personal_inf(name=input("Enter your name: "), surname=input("Enter your surname: "),
              year_of_birth=input("Enter your birth year: "), city_of_residence=input("Enter your residence city: "),
              email=input("Enter your email: "), phone_number=input("Enter your phone_number: ")))
