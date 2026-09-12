attempts = 0

while True:
    pin = int(input("PIN: "))
    attempts += 1

    if pin == 4321:
        if attempts == 1:
            print(f"Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    elif pin != 4321:
        print("Wrong")