fruit = input()
week_day = input()
quantity = float(input())
price = 0
week_day_validation = True
fruit_validation = True

if week_day == "Monday" \
        or week_day == "Tuesday" \
        or week_day == "Wednesday" \
        or week_day == "Thursday" \
        or week_day == "Friday":
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        fruit_validation = False
elif week_day == "Saturday" \
        or week_day == "Sunday":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        fruit_validation = False
else:
    week_day_validation = False

if week_day_validation and fruit_validation:
    total = price * quantity
    print(f"{total:.2f}")
else:
    print("error")
