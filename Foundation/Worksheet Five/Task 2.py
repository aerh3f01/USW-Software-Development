# Using code from task 1, write a program that will accept a list of positive integers, terminated by entering 0
# Should output the sum and their average

def main():
    sum_of_nums = 0
    count = 0

    num = int(input("Enter a number."))
    while num != 0:
        sum_of_nums += num
        count += 1
        num = int(input("Enter another number. To end the program, enter a 0.\n"))

    average = sum_of_nums / count

    print(f"The sum of the integers is {sum_of_nums}")
    print(f"The average is {average}")

if __name__ == '__main__':
    main()