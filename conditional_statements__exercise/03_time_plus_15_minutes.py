hour = int(input())
seconds = int(input())
extra = 15

concat_time = f'{hour}:{seconds}'

hour_calc = ''
seconds_calc = ''

if seconds + extra > 60 and seconds + extra <= 69:
    # seconds_calc = '0' + str((seconds - 60) + extra)
    seconds_calc = '0' + str((seconds + extra) - 60)
    hour_calc = hour + 1
elif seconds + extra > 69:
    seconds_calc = (seconds + extra) - 60
    hour_calc = hour + 1
elif seconds + extra == 60:
    seconds_calc = '00'
    hour_calc = hour + 1
elif seconds + extra < 60:
    seconds_calc = seconds + extra
    hour_calc = hour

if hour_calc > 24:
    print(f'{hour_calc}:{seconds_calc}')
elif hour_calc == 24:
    print(f'0:{seconds_calc}')
else:
    print(f'{hour_calc}:{seconds_calc}')
