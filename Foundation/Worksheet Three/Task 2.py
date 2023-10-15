# Program that outputs the larger of two numbers 


def main():
    first_number = int(input("Please enter a number.\n"))
    second_number = int(input("Please enter another number.\n"))

    if first_number > second_number:
        print(f"{first_number} is larger.")
    else: 
        print(f"{second_number} is larger")

if __name__ == '__main__':
    main()