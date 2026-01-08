
print("\n---ChatBot---\n")

bot = "Bot:"

name = input(bot + "What's your name?\nYou:")
print(bot + "Nice to meet you", name)

while True:
    concern = input("\n" + bot + "How can i help you today?\nYou: ")
    print(bot + "That's nice to hear!")

    ass = input(
        bot + "Do you want to help you with your assignment? (y / n)\nYou: ")

    if ass == "y":
        print(bot + "Great! I love to help you with that")

    # q1 = What color is the sun?
    # q2 = How many legs does a dog have?
        question = input(
            bot + "So please tell me the exact question so i can assist you\nYou:")

        if question.lower() == "what color is the sun?":
            print(bot + "The sun is yellow.")
        elif question.lower() == "how many legs does a dog have?":
            print(bot + "A dog has four legs.")
        else:
            print(bot + "Sorry i don't know")

    elif ass == "n":
        print(bot + "Allright then, goodbye!")
        break
    else:
        print(bot + "Error: Please answer y or n")

    exit = input("You want to ask for more? (y / n)\nYou:")

    if exit == "y":
        continue
    else:
        print(bot + "Goodbye!")
        break
