import math

days_alone = int(input())
food_for_pets = int(input())
food_for_dog = float(input())
food_for_cat = float(input())
food_for_turtle = float(input())
food_for_turtle = food_for_turtle / 1000

pets_will_eat_per_day = food_for_dog + food_for_turtle + food_for_cat
total_vanished_food = pets_will_eat_per_day * days_alone

hunger_rate = 0

if total_vanished_food <= food_for_pets:
    hunger_rate = food_for_pets - total_vanished_food
    hunger_rate = math.floor(hunger_rate)
    print(f"{hunger_rate} kilos of food left.")
else:
    hunger_rate = total_vanished_food - food_for_pets
    hunger_rate = math.ceil(hunger_rate)
    print(f"{hunger_rate} more kilos of food are needed.")
