limit = int(input("Limit: "))
num = 1
running_total = 0

while running_total < limit:
    running_total += num
    num += 1
print(running_total)
