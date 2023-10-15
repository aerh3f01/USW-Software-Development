

def show_sum(num1, num2, num3):
    #print(f"The sum of the numbers is {num1 + num2 + num3}.")

    print()
    print(f"number one = {num1}, number two = {num2}, number three = {num3}.")
    print(f"The sum of the numbers is {num1 + num2 + num3}.")
    print()

def main():
    num1 = int(input("Please enter a number.\n"))
    num2 = int(input("Please enter another number.\n"))
    num3 = int(input("Please enter another number.\n"))
    #show_sum(num1+1, num2+1, num3+1)

    show_sum(num1, num1, num1)
    show_sum(num2, num2, num2)
    show_sum(num3, num3, num3)

if __name__ == '__main__':
    main()
