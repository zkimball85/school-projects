user_age = input("Please enter your age: ")
age = int(user_age)
if age >= 0 and age <= 1:
    print("You are an infant.")
elif age > 1 and age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior citizen.")
else:
    print("Invalid age entered.")

user_month = int(input("Please enter the month you were born (1-12): "))
user_day = int(input("Please enter the day you were born (1-31): "))

