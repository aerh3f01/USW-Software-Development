# Modifying code from task two, if a negative number is entered a message should be displayed and the number ignored
# needing to use if-else statements

def main():
    sum_of_nums = 0
    count = 0

    num = int(input("Enter a number."))
    while num != 0:
        if num < 0:
            print("Negative numbers are not allowed.")
        else:
            sum_of_nums += num
            count += 1
        num = int(input("Enter another number. To end the program, enter a 0.\n"))

    average = sum_of_nums / count

    print(f"The sum of the integers is {sum_of_nums}")
    print(f"The average is {average}")

if __name__ == '__main__':
    main()