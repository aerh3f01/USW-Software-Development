# Writing the following code and explaining what it does:

def return_value_GTE_5():
    number = 0
    while number < 5:
        number = int(input("Please enter a value greater than or equal to 5.\n"))
    return number

if __name__ == '__main__':
    number = return_value_GTE_5()
    print(f"You entered {number}.")

# This function will return a value greater than or equal to 5. 
# It will keep asking the user to enter a value until
# they enter a value greater than or equal to 5.

