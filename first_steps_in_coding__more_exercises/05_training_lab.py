h = float(input())  # 15
w = float(input())  # 8.9

w_workplace = 70
h_workplace = 120

w_corridor = 100
h_corridor = h

w_total = ((w * 100) - w_corridor) // w_workplace
h_total = (h * 100) // h_workplace

print(int(w_total) * int(h_total) - 3)
