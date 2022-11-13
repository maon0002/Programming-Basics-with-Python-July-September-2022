budget = float(input())
lame_actors_qty = int(input())
price_costume = float(input())

total_price_costume = lame_actors_qty * price_costume
decor = .1 * budget
discount_costume = 0

cost = 0

if lame_actors_qty >= 150:
    discount_costume = total_price_costume * .1
    cost = decor + (total_price_costume - discount_costume)
else:
    discount_costume = 0
    cost = decor + total_price_costume

if budget >= cost:
    print("Action!")
    print(f"Wingard starts filming with {budget - cost:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {cost - budget:.2f} leva more.")
