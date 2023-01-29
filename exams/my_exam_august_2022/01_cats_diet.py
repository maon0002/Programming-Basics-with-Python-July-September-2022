percentage_fats = int(input())
percentage_proteins = int(input())
percentage_carbs = int(input())
total_calories = int(input())
percentage_water = int(input())

fats_per_gram = 9  # calories
proteins_per_gram = 4  # calories
carbs_per_gram = 4  # calories

fats = (total_calories * (percentage_fats / 100)) / fats_per_gram
proteins = (total_calories * (percentage_proteins / 100)) / proteins_per_gram
carbs = (total_calories * (percentage_carbs / 100)) / carbs_per_gram

total_grams_elements = (fats + proteins + carbs)
calories_per_gram = total_calories / total_grams_elements
water = calories_per_gram * (percentage_water / 100)
print(f"{calories_per_gram - water:.4f}")
