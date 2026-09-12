value_of_gift = int(input("Value of gift: "))

if value_of_gift < 5_000:
    print("No tax!")

elif value_of_gift <= 25_000:
    tax_owed = (100 + (value_of_gift - 5_000) * 0.08)
    print(f"Amount of tax: {tax_owed} euros")
elif value_of_gift <= 55_000:
    tax_owed = (1_700 + (value_of_gift - 25_000) * .10)
    print(f"Amount of tax: {tax_owed} euros")
elif value_of_gift <= 200_000:
    tax_owed = (4_700 + (value_of_gift - 55_000) * .12)
    print(f"Amount of tax: {tax_owed} euros")
elif value_of_gift <= 1_000_000:
    tax_owed = (22_100 + (value_of_gift - 200_000) * .15)
    print(f"Amount of tax: {tax_owed} euros")
else:
    tax_owed = (142_100 + (value_of_gift - 1_000_000) * .17)
    print(f"Amount of tax: {tax_owed} euros")