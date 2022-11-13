week_day = int(input())
week_day_eng = ""

if week_day == 1:
    week_day_eng = "Monday"
elif week_day == 2:
    week_day_eng = "Tuesday"
elif week_day == 3:
    week_day_eng = "Wednesday"
elif week_day == 4:
    week_day_eng = "Thursday"
elif week_day == 5:
    week_day_eng = "Friday"
elif week_day == 6:
    week_day_eng = "Saturday"
elif week_day == 7:
    week_day_eng = "Sunday"
else:
    week_day_eng = 'Error'

print(week_day_eng)
