# Using the code from Task 1
# write a function that only accepts and return values between 5 and 9 inclusive.

def return_value_between_5_and_9():
    number = 0
    while number < 5 or number > 9:
        number = int(input("Please enter a value between 5 and 9 inclusive.\n"))
    return number

if __name__ == '__main__':
    number = return_value_between_5_and_9()
    print(f"You entered {number}.")