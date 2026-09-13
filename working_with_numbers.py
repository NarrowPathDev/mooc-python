count = 0
running_total = 0
positive_num = 0
negative_num = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    count += 1
    running_total += num
    if num > 0:
        positive_num += 1
    elif num < 0:
        negative_num += 1
mean = running_total / count

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {running_total}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive_num}")
print(f"Negative numbers {negative_num}")