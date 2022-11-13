from math import pi

r = float(input())

face = pi * (r * r)  # формула за лице на кръг S = πr²
perimeter = (2 * pi) * r  # P = 2π.R

print(format(face, '.2f'))
print(format(perimeter, '.2f'))
