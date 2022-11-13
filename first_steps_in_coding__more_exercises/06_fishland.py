scum_per_kg = float(input())
caca_per_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
clam_kg = int(input())

price_palamud = scum_per_kg * 1.6
price_safrid = caca_per_kg * 1.8
price_clam = 7.5

total_palamud = price_palamud * palamud_kg
total_safrid = price_safrid * safrid_kg
total_clam = price_clam * clam_kg

total_all = total_clam + total_safrid + total_palamud

print(format(total_all, '.2f'))
