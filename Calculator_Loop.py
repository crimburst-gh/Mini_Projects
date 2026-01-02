def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


while True:

    print("---Calculator---\n")
    name = input("Bot: What's your name? ")
    print("\nHi!", name)

    op = input("\nBot: Select operation (+ - * /): ")
    num1 = float(input("\nBot: Select first number: "))
    num2 = float(input("\nBot: Select second number: "))

    if op == '+':
        print("\nBot:", add(num1, num2))

    elif op == '-':
        print("\nBot:", sub(num1, num2))

    elif op == '*':
        print("\nBot:", mult(num1, num2))

    elif op == '/':
        print("\nBot:", div(num1, num2))

    else:
        print("\nError")

    again = input("\nBot: Do you want to compute again? (y / n) ")
    if again != 'y':
        print("\nThank you", name)
        break
