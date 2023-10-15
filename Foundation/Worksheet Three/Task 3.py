# Program that enters two integers and desplays in accending order, or just the value once if its the same number.


def main():
    first_number = int(input("Please enter the first number.\n"))
    second_number = int(input("Please enter a second number.\n"))

    if first_number == second_number:
        print(f"The numbers ({first_number}) were both equal.")
    elif first_number > second_number:
        print(f"The numbers in acceding order are {second_number} then {first_number}")
    else:
        print(f"The numbers in accending order are {first_number} then {second_number}")

if __name__ == '__main__':
    main()