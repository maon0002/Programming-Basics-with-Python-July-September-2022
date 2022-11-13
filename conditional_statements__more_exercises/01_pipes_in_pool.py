v_liters = int(input())  # 1000
p1_liters_per_hour = int(input())  # 100
p2_liters_per_hour = int(input())  # 120
hours = float(input())  # 3

p1_contribution = hours * p1_liters_per_hour  # 3x100 = 300l
p2_contribution = hours * p2_liters_per_hour  # 3x120 = 360l
both_pipes_contribution = p1_contribution + p2_contribution  # =660l

percentage_total = (both_pipes_contribution / v_liters) * 100
# percentage_total = math.floor(percentage_total)
percentage_p1 = (p1_contribution / both_pipes_contribution) * 100
# percentage_p1 = math.floor(percentage_p1)
percentage_p2 = (p2_contribution / both_pipes_contribution) * 100
# percentage_p2 = math.floor(percentage_p2)

if v_liters >= both_pipes_contribution:
    print(f"The pool is {percentage_total:.2f}% full. Pipe 1: {percentage_p1:.2f}%. Pipe 2: {percentage_p2:.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {both_pipes_contribution - v_liters:.2f} liters.")
