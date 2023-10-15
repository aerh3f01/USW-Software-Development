# Using a for loop to promt the input of 5 numbers.
# Call a function named even_or_odd that will display the number is even or odd.

def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


def main():
    for i in range(5):
        number = int(input("Please enter a number.\n"))
        even_or_odd(number)

if __name__ == '__main__':
    main()

