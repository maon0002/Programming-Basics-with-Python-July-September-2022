fuel = input()
fuel_liters = float(input())
card_issued = input()

fuel_price = 0
card_discount = 0
liters_discount = 0
total = 0

if card_issued == "No":
    if fuel == "Gas":
        fuel_price = fuel_liters * 0.93
    elif fuel == "Gasoline":
        fuel_price = fuel_liters * 2.22
    elif fuel == "Diesel":
        fuel_price = fuel_liters * 2.33
elif card_issued == "Yes":
    if fuel == "Gas":
        discount = 0.08
        fuel_price = fuel_liters * (0.93 - discount)
    elif fuel == "Gasoline":
        discount = 0.18
        fuel_price = fuel_liters * (2.22 - discount)
    elif fuel == "Diesel":
        discount = 0.12
        fuel_price = fuel_liters * (2.33 - discount)

if 20 <= fuel_liters <= 25:
    liters_discount = fuel_price * 0.08
    fuel_price = fuel_price - liters_discount
elif fuel_liters > 25:
    liters_discount = fuel_price * 0.10
    fuel_price = fuel_price - liters_discount

print(f"{fuel_price:.2f} lv.")
