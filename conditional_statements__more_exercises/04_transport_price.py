km = int(input())
time_of_the_day = input()

taxi_day = (km * .79) + .7
taxi_night = (km * .9) + .7
taxi_price = 0

bus_day_night = km * .09  # min 20km
bus_min_km = 20
bus_price = 0

train_day_night = km * .06  # min 100 km
train_min_km = 100
train_price = 0

best_tariff = 0

if km >= 100:
    best_tariff = train_day_night
elif km >= 20:
    best_tariff = bus_day_night
elif km < 20 and time_of_the_day == 'day':
    best_tariff = taxi_day
else:
    best_tariff = taxi_night

print(f"{best_tariff:.2f}")
