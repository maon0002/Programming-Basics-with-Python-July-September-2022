flowers_type = input()
flowers_qty = int(input())
budget = int(input())

# price_roses = flowers_qty * 5
# price_dahlias = flowers_qty * 3.80
# price_tulips = flowers_qty * 2.80
# price_narcissus = flowers_qty * 3
# price_gladiolus = flowers_qty * 2.50
# subtotal = price_flowers - discount + plus_extra

price_flowers = 0
discount = 0
plus_extra = 0

if flowers_type == "Roses":
    if flowers_qty > 80:
        price_flowers = flowers_qty * 5
        discount = price_flowers * 0.1
    else:
        price_flowers = flowers_qty * 5
elif flowers_type == "Dahlias":
    if flowers_qty > 90:
        price_flowers = flowers_qty * 3.80
        discount = price_flowers * 0.15
    else:
        price_flowers = flowers_qty * 3.80
elif flowers_type == "Tulips":
    if flowers_qty > 80:
        price_flowers = flowers_qty * 2.80
        discount = price_flowers * 0.15
    else:
        price_flowers = flowers_qty * 2.80
elif flowers_type == "Narcissus":
    if flowers_qty < 120:
        price_flowers = flowers_qty * 3
        plus_extra = price_flowers * 0.15
    else:
        price_flowers = flowers_qty * 3
elif flowers_type == "Gladiolus":
    if flowers_qty < 80:
        price_flowers = flowers_qty * 2.50
        plus_extra = price_flowers * 0.2
    else:
        price_flowers = flowers_qty * 2.50

total = price_flowers - discount + plus_extra
diff = abs(budget - total)

if budget >= total:
    print(f"Hey, you have a great garden with {flowers_qty} {flowers_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
