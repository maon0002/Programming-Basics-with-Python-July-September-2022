x = float(input())  # x – височината на къщата – реално число в интервала [2...100]
y = float(input())  # y – дължината на страничната стена – реално число в интервала [2...100]
h = float(input())  # h – височината на триъгълната стена на прокрива – реално число в интервала [2...100]
green_paint_sqm_per_litre = 3.4
red_paint_sqm_per_litre = 4.3

front_door = 2 * 1.2
side_windows = 1.5 * 1.5

front_wall = x * x - front_door
back_wall = x * x
side_walls = ((x * y - side_windows) * 2)

roof_sides = (x * y) * 2
roof_triangles = ((x * h) / 2) * 2
# Triangle area = (height * base) / 2
total_walls_sqm = front_wall + back_wall + side_walls
total_roof_sqm = roof_triangles + roof_sides

green_sqm = format(total_walls_sqm / green_paint_sqm_per_litre, '.2f')
red_sqm = format(total_roof_sqm / red_paint_sqm_per_litre, '.2f')

print(green_sqm)
print(red_sqm)
