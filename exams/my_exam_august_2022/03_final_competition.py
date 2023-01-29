dancers_number = int(input())
points_number = float(input())
season = input()
place = input()
expenses = 0

money_price = 0

if place == "Bulgaria":
    money_price = dancers_number * points_number
    if season == "summer":
        money_price *= 0.95
    elif season == "winter":
        money_price *= 0.92
elif place == "Abroad":
    money_price = (dancers_number * points_number) * 1.50
    if season == "summer":
        money_price *= 0.90
    elif season == "winter":
        money_price *= 0.85

charity = money_price * 0.75
money_left = money_price * 0.25
money_per_person = money_left / dancers_number

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_person:.2f}")
