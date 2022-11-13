username = input()
password = input()
pass_try = input()

while True:
    if pass_try != password:
        pass_try = input()
    else:
        print(f"Welcome {username}!")
        break
