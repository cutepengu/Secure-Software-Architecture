def validate_age(age_input):
    age = int(age_input)
    if 0 <= age_input <= 120:
        return(age)
    else:
        print("Please enter a valid number from 0-120")
age_input = input("Please enter your age: ")
print(f"Your age is: {age_input}")