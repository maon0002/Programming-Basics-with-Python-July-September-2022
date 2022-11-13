pens_pack = int(input())
markers_pack = int(input())
liters_liquid = int(input())
discount = int(input())
discount_perc = discount / 100

price_pens = pens_pack * 5.8
price_markers = markers_pack * 7.2
price_liquid = liters_liquid * 1.2

total = (price_pens + price_liquid + price_markers) - ((price_pens + price_liquid + price_markers) * discount_perc)
print(total)
