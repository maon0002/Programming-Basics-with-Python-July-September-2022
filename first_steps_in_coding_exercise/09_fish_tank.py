length = int(input())
wide = int(input())
height = int(input())
percent = float(input())

percentage_calc = percent / 100
dm = (length * wide * height) / 1000

free_aquarium_space = dm - dm * percentage_calc
liters_water = free_aquarium_space

print(liters_water)
