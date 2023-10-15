# Using code from Task 2
# write a function that only accepts and return values between 5 and 9 inclusive.
# If a negative value is entered, the function should display "negative numbers are never accepted".

def return_value_between_5_and_9():
    number = 0
    while number < 5 or number > 9:
        number = int(input("Please enter a value between 5 and 9 inclusive.\n"))
        if number < 0:
            print("Negative numbers are never accepted.")
    return number

if __name__ == '__main__':
    number = return_value_between_5_and_9()
    print(f"You entered {number}.")