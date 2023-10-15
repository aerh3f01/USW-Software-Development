## Find the biggest of three integers


def main():
    num1 = int(input("Please enter the first number.\n"))
    num2 = int(input("Please enter the second number.\n"))
    num3 = int(input("Please enter the third number.\n"))
    
    smallest = min(num1, num2, num3)
    largest = max(num1, num2, num3)

    sum_of_nums = smallest + largest
    print(f"The sum of the smallest and largest is {sum_of_nums}")
    

if __name__ == '__main__':
    main()