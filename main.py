def has_digit(string):
    for ch in string:
        if ch.isdigit():
            return True

    return False


def check_gender(gen):
    if gen == "Male":
        return True
    if gen == "Female":
        return True
    if gen == "Other":
        return True

    return False


while True:
    name = input("Enter a name: ")
    if name == "" or has_digit(name):
        print("Please enter a proper name")
    else:
        print(f"Your name is {name}")
        break

while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError as err:
        print("Please enter a number")
    else:
        if age < 0 or age > 120:
            print("Enter your correct age")
        else:
            print(f"Your age is {age}")
            break

while True:
    gender = input("Enter your gender: ")
    if gender == "" or not check_gender(gender):
        print("Please enter a proper gender")
    else:
        print(f"Your gender is {gender}")
        break

while True:
    try:
        salary = int(input("Enter your salary: "))
    except ValueError as err:
        print("Please enter a number")
    else:
        if salary < 0:
            print("Enter your correct salary")
        else:
            print(f"Your salary is {salary}")
            break

while True:
    state = input("Enter your state: ")
    if state == "" or has_digit(state):
        print("Please enter a proper state")
    else:
        print(f"Your state is {state}")
        break

while True:
    city = input("Enter your city: ")
    if city == "" or has_digit(city):
        print("Please enter a proper city")
    else:
        print(f"Your city is {city}")
        break