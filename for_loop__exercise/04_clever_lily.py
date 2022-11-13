age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_count = 0
money = 0

for x in range(1, age + 1):
    if x % 2 != 0:
        toy_count += 1
    else:
        money = (money + (x * 5)) - 1

toys_profit = toy_price * toy_count
savings = toys_profit + money

diff = abs(washing_machine_price - savings)

if savings >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
