string_one = input("Please type in string 1: ")
string_two = input("Please type in string 2: ")

if len(string_one) > len(string_two):
    print(f"{string_one} is longer")
elif len(string_one) < len(string_two):
    print(f"{string_two} is longer")
else:
    print("The strings are equally long")
