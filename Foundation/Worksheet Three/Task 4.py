## Find the biggest of three integers


def main():
    num1 = int(input("Please enter the first number.\n"))
    num2 = int(input("Please enter the second number.\n"))
    num3 = int(input("Please enter the third number.\n"))
    
    if num1 > num2 > num3:
        print(f"{num1} is the biggest")
    elif num2 > num1 > num3:
        print(f"{num2} is the biggest")
    else:
        print(f"{num3} is the biggest")


if __name__ == '__main__':
    main()