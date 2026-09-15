print("Welcome to the Temple. Time to clean house.")

while True:
    in_temple = input("Who is in the temple? ").lower().strip()
    if in_temple == "worshipper":
        print("Shalom, go pray.")
    elif in_temple == "merchant":
        num_of_tables = int(input("How many tables do they have? "))
        print("FLIP! " * num_of_tables)
    elif in_temple == "done":
        break