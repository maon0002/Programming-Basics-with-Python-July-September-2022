sqm_nylon = int(input())
liters_paint = int(input())
blah_paint = int(input())
hours_total = int(input())

nylon_bags = 0.4
liters_paint_extra = liters_paint + liters_paint * 0.1
sqm_nylon_extra = sqm_nylon + 2

price_nylon = sqm_nylon_extra * 1.5
price_paint = liters_paint_extra * 14.5
price_blah = blah_paint * 5

total_expences = nylon_bags + price_nylon + price_blah + price_paint

rate_per_hour = hours_total * (total_expences * 0.3)
print(total_expences + rate_per_hour)
