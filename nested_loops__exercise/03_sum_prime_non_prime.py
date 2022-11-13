input_line = input()

prime_number_sum = 0
non_prime_number_sum = 0

while input_line != "stop":
    number = int(input_line)
    while True:

        if number < 0:
            print("Number is negative.")

        elif number == 2 or number == 3:
            prime_number_sum += number
        elif number == 0:
            pass
        else:
            if number % 2 == 0 or number % 3 == 0:
                non_prime_number_sum += number
            else:
                prime_number_sum += number

        input_line = input()
        break

if input_line == "stop":
    print(f"Sum of all prime numbers is: {prime_number_sum}")
    print(f"Sum of all non prime numbers is: {non_prime_number_sum}")
