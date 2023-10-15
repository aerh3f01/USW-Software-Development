# Program that inputs three integers and uses messages to display largest of the three numbers.

def larger_nums(num1, num2, num3):
    largest = max(num1, num2, num3)
    return f"The largest number is {largest}."

def main():
    num1 = int(input("Please enter a number.\n"))
    num2 = int(input("Please enter another number.\n"))
    num3 = int(input("Please enter another number.\n"))
    print(larger_nums(num1, num2, num3))

if __name__ == '__main__':
    main()