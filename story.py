words = ""
last_word = ""

while True:
    word = input("Please type in a word: ")
    if word == "end":
        print(words)
        break
    if last_word == word:
        print(words)
        break
    words += word + " "
    last_word = word