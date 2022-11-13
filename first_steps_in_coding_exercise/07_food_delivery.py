chicken_menus = int(input())
fish_menus = int(input())
veg_menus = int(input())
delivery = 2.5

price_chicken = chicken_menus * 10.35
price_fish = fish_menus * 12.4
price_veg = veg_menus * 8.15
sub_total_price = price_veg + price_fish + price_chicken
dessert = 0.2 * sub_total_price

print(sub_total_price + dessert + delivery)
