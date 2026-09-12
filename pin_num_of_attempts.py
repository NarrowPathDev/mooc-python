attempts = 0

while True:
    pin = int(input("PIN: "))


    if pin == 4321:
        attempts += 1
        print(f"Correct! It only took you one single attempt!")
        break
    elif pin != 4321:
        attempts += 1
        print("Wrong")