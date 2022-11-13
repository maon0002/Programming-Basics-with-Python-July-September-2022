fuel_type = input()
existed_liters_fuel = int(input())
allowed_fuel_types = ["Diesel", "Gasoline", "Gas"]
default_existed_liters = 25

if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
    print("Invalid fuel!")
elif existed_liters_fuel >= default_existed_liters:
    print(f"You have enough {str.lower(fuel_type)}.")
else:
    print(f"Fill your tank with {str.lower(fuel_type)}!")
