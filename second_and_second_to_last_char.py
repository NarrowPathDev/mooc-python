string = input("Please type in a string: ")
index = string[-2]

if string[1] == index:
    print(f"The second and the second to last characters are {index}")
else:
    print("The second and the second to last characters are different")