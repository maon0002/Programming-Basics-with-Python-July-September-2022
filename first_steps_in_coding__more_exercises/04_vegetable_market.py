kg_veg = float(input())
kg_fruits = float(input())
total_veg = int(input())
total_fruits = int(input())

kg_veg_euro = kg_veg / 1.94
kg_fruits_euro = kg_fruits / 1.94

veg_total = kg_veg_euro * total_veg
fruit_total = kg_fruits_euro * total_fruits

gain = format(veg_total + fruit_total, '.2f')

print(gain)
