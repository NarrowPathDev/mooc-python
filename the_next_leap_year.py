year = int(input("Year: "))
year2 = year + 1
while True:
    
    if year2 % 100 == 0:
            if year2 % 400 == 0:
                  print(f"The next leap year after {year} is {year2}")
                  break
    elif year2 % 4 == 0:
            print(f"The next leap year after {year} is {year2}")
            break
    year2 += 1