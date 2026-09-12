print("Welcome to the journey to Jerusalem!")
traveling = input("Are you traveling to Jerusalem for the Feast of Tabernacles? (Y or N):")

if traveling == "N":
    print("Rejoice in Yahweh where you live!")
else:
    print("Let's prepare for the trip!")
    age = int(input("How old are you? "))
    travel_fund = 0
    if age < 12:
        travel_fund += 0
        print(f"You are young, come learn the Torah.")
    elif age >= 12 and age <= 19:
        travel_fund += 3
        print(f"You are coming of age.")
    else:
        travel_fund += 5
        print(f"You are of the census age.")
    freewill_offering = input("Will you bring a freewill offering for Yahweh? (Y or N): ")
    if freewill_offering == "Y":
        travel_fund += 10
    print(f"Your final travel fund needed is ${travel_fund}")