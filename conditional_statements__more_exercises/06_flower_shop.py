import math

magnolias = int(input())
zombies = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())

price_magnolias = 3.25 * magnolias
price_zombies = 4 * zombies
price_roses = 3.5 * roses
price_cactus = 8 * cactus
profit = price_cactus + price_roses + price_zombies + price_magnolias

bloody_tax = profit * .05

money_for_the_poor_son = profit - bloody_tax

beg_on_streets_for = 0

if gift_price > money_for_the_poor_son:
    beg_on_streets_for = gift_price - money_for_the_poor_son
    beg_on_streets_for = math.ceil(beg_on_streets_for)
    print(f"She will have to borrow {beg_on_streets_for} leva.")
else:
    beg_on_streets_for = money_for_the_poor_son - gift_price
    beg_on_streets_for = math.floor(beg_on_streets_for)
    print(f"She is left with {beg_on_streets_for} leva.")
