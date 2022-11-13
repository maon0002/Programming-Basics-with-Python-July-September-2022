price_travel = float(input())
puzzle_qty = int(input())
dolls_qty = int(input())
teddy_qty = int(input())
minions_qty = int(input())
truck_qty = int(input())

puzzle_price = puzzle_qty * 2.6
dolls_price = dolls_qty * 3
teddy_price = teddy_qty * 4.1
minions_price = minions_qty * 8.2
truck_price = truck_qty * 2

count_toys = truck_qty + minions_qty + dolls_qty + teddy_qty + puzzle_qty
sub_total = puzzle_price + truck_price + minions_price + dolls_price + teddy_price
total = sub_total

discount_toys = 0  # if count_toys >= 50 then -25% from total price
rent = 0.10 * total

result = total - rent

if count_toys >= 50:
    discount_toys = sub_total * 0.25
    total = sub_total - discount_toys
    rent = 0.10 * total
    result = total - rent

if price_travel > result:
    print(f"Not enough money! {price_travel - result:.2f} lv needed.")
else:
    print(f"Yes! {result - price_travel:.2f} lv left.")
