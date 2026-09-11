print("The Berean Discernment Scale")

teaching_or_song = input("What is the title of the teaching or song? ")
score = int(input("Berean accuracy score (On a scale of 1-10): "))

if score == 10:
    print("This teaching holds fast to the narrow path.")

elif score >= 7:
    print("Warning: Test the material further.")

else:
    print("Guard your Emunah!")