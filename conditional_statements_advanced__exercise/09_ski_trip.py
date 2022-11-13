va_days = int(input())
room_type = input()
judge = input()

va_nights = va_days - 1
price_per_night = 0
discount = 0
judge_validation = True

if room_type == "room for one person":
    price_per_night = 18
elif room_type == "apartment":
    price_per_night = 25
    if va_days > 15:
        discount = 0.50
    elif 10 <= va_days <= 15:
        discount = 0.35
    else:
        discount = 0.30
elif room_type == "president apartment":
    price_per_night = 35
    if va_days > 15:
        discount = 0.20
    elif 10 <= va_days <= 15:
        discount = 0.15
    else:
        discount = 0.10

subtotal = va_nights * price_per_night
total = subtotal - (subtotal * discount)

if judge == "positive":
    total = total * 1.25
else:
    total = total * 0.90

print(f"{total:.2f}")
