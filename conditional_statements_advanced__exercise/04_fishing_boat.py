budget = int(input())
season = input()
fisherman = int(input())

rent = 0
group_discount = 0
even_not_autumn_discount = 0

if season == "Spring":
    rent = 3000
    if fisherman <= 6:
        group_discount = rent * 0.10
    elif 7 <= fisherman <= 11:
        group_discount = rent * 0.15
    elif fisherman > 11:
        group_discount = rent * 0.25
elif season == "Summer" or season == "Autumn":
    rent = 4200
    if fisherman <= 6:
        group_discount = rent * 0.10
    elif 7 <= fisherman <= 11:
        group_discount = rent * 0.15
    elif fisherman > 11:
        group_discount = rent * 0.25
elif season == "Winter":
    rent = 2600
    if fisherman <= 6:
        group_discount = rent * 0.10
    elif 7 <= fisherman <= 11:
        group_discount = rent * 0.15
    elif fisherman > 11:
        group_discount = rent * 0.25

subtotal = rent - group_discount

if fisherman % 2 == 0 and not season == "Autumn":
    even_not_autumn_discount = subtotal * 0.05

total = subtotal - even_not_autumn_discount
diff = abs(budget - total)

if budget >= total:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
