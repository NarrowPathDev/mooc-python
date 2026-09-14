limit = int(input("Limit: "))
num = 1
running_total = 0
consecutive_sum = ""

while running_total < limit:
    running_total += num
    if running_total < limit:
        consecutive_sum += str(num) + " + "
    else:
        consecutive_sum += str(num)
    num += 1
print(f"the consecutive sum: {consecutive_sum} = {running_total}")