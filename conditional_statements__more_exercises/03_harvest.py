import math

sqm_land = int(input())
grape_per_sqm = float(input())
needed_wine_liters = int(input())
workers_qty = int(input())

wine_production = (
                              sqm_land * grape_per_sqm) * .4  # От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
wine_liters = wine_production / 2.5  # За 1 литър вино са нужни 2,5 кг. грозде.
wine_per_worker = 0
difference = 0

if wine_liters < needed_wine_liters:
    difference = needed_wine_liters - wine_liters
    difference = math.floor(difference)
    print(f"It will be a tough winter! More {difference:.0f} liters wine needed.")
else:
    difference = wine_liters - needed_wine_liters
    difference = math.floor(difference)
    wine_per_worker = difference / workers_qty
    wine_per_worker = math.ceil(wine_per_worker)
    print(f"Good harvest this year! Total wine: {wine_liters:.0f} liters.")
    print(f"{difference:.0f} liters left -> {wine_per_worker:.0f} liters per person.")
