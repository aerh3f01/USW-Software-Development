# read a list of any 10 positive integer values
# outputs the sum and average


def main():
    sum_of_int = 0
    count = 10

    for i in range(count):
        num = int(input("Enter a number."))
        sum_of_int += num
    
    average = sum_of_int / count

    print(f"The sum of the integers is {sum_of_int}")
    print(f"The average is {average}")

if __name__ == '__main__':
    main()