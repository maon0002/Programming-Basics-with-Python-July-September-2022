dish_washer_bottles = int(input())
ml_liquid = dish_washer_bottles * 750
ml_for_dish = 5
ml_for_pot = 15
ml_decrease = 0
dishes = 0
clean_dishes_count = 0
clean_pots_count = 0
count_on = 0

while ml_liquid >= ml_decrease:
    dishes = input()
    if dishes != "End":
        dishes_num = int(dishes)
        count_on += 1
        if count_on % 3 != 0:
            ml_decrease += (dishes_num * ml_for_dish)
            clean_dishes_count += dishes_num
        else:
            ml_decrease += (dishes_num * ml_for_pot)
            clean_pots_count += dishes_num
    else:

        break

diff = abs(ml_liquid - ml_decrease)

if ml_liquid >= ml_decrease:
    print(f"Detergent was enough!")
    print(f"{clean_dishes_count} dishes and {clean_pots_count} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")
