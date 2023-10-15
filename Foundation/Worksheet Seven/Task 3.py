# input prompt for two integers and calls function that displays largest number

def larger_nums(num1, num2):
    if num1 > num2:
        return f"The first number is larger. {num1}"
    elif num1 < num2:
        return f"The second number is larger. {num2}"
    else:
        return f"The numbers are the same. {num1}"
    
def main():
    num1 = int(input("Please enter a number.\n"))
    num2 = int(input("Please enter another number.\n"))
    print(larger_nums(num1, num2))

if __name__ == '__main__':
    main()