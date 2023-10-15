# Display a message from a list, based on the input of two numbers conditions


def main():
    messages = ["Both numbers are less than 10", "The numbers are the same", "Neither number is less than 10", "Only one number is less than 10", "The numbers are different", "At least one number is even"]

    num1 = int(input("Please input a number"))
    num2 = int(input("Please enter another number"))

    if num1 and num2 < 10:
        print(messages[0])
    if num1 == num2:
        print(messages[1])
    if num1 and num2 > 10:
        print(messages[2])
    if num1 < 10 and num2 > 10:
        print(messages[3])
    if num1 > 10 and num2 < 10:
        print(messages[3])
    if num1 != num2:
        print(messages[4])
    if (num1 % 2) == 0 or (num2 % 2) == 0:
        print(messages[5])

if __name__ == '__main__':
    main()
    