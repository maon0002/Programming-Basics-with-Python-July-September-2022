fee_per_year = int(input())

sneakers = 0.6 * fee_per_year
equip = 0.8 * sneakers
ball = 0.25 * equip
accessories = 0.2 * ball

total = sneakers + equip + ball + accessories + fee_per_year
print(total)
