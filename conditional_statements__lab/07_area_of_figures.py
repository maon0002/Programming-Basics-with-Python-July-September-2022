from math import pi

figure = input()

if figure == 'square':
    length_square = float(input())
    square_calc = length_square * length_square
    print(f'{square_calc:.3f}')

elif figure == 'rectangle':
    rectangle_side1 = float(input())
    rectangle_side2 = float(input())
    rectangle_calc = rectangle_side2 * rectangle_side1
    print(f'{rectangle_calc:.3f}')

elif figure == 'circle':
    r_circle = float(input())
    radius = pi * (r_circle * r_circle)
    print(f'{radius:.3f}')

elif figure == 'triangle':
    side_triangle = float(input())
    height_triangle = float(input())
    face_triangle = (side_triangle * height_triangle) / 2
    print(f'{face_triangle:.3f}')
