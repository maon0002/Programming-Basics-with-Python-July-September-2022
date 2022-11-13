city = input()
sales = float(input())
sales_rate = 0
city_validation = True
sales_validation = True

if city == "Sofia":
    if 0 <= sales <= 500:
        sales_rate = sales * 0.05
    elif 500 <= sales <= 1000:
        sales_rate = sales * 0.07
    elif 1000 <= sales <= 10000:
        sales_rate = sales * 0.08
    elif sales > 10000:
        sales_rate = sales * 0.12
    else:
        sales_validation = False
elif city == "Varna":
    if 0 <= sales <= 500:
        sales_rate = sales * 0.045
    elif 500 <= sales <= 1000:
        sales_rate = sales * 0.075
    elif 1000 <= sales <= 10000:
        sales_rate = sales * 0.10
    elif sales > 10000:
        sales_rate = sales * 0.13
    else:
        sales_validation = False
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        sales_rate = sales * 0.055
    elif 500 <= sales <= 1000:
        sales_rate = sales * 0.08
    elif 1000 <= sales <= 10000:
        sales_rate = sales * 0.12
    elif sales > 10000:
        sales_rate = sales * 0.145
    else:
        sales_validation = False
else:
    city_validation = False

if sales_validation and city_validation:
    print(f"{sales_rate:.2f}")
else:
    print("error")
