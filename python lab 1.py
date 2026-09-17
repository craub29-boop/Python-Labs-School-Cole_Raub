def ask():
    name = input("What is ur name?")
    age = input("what is ur age?")
    color = input("what is ur fav color?")
    return name, age, color

while True:
    name, age, color = ask()
    print("Your info is:", name, age, color)
