
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    bigger = max(num1, num2)
    smaller = min(num1, num2)
    return bigger - smaller

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    bigger = max(num1, num2)
    smaller = min(num1, num2)
    return bigger / smaller

def sum_between(num1, num2): 
    bigger = max(num1, num2) # get bigger number
    smaller = min(num1, num2) # get smaller number
    sum = 0 # variable to store sum
    calc = "" # string to store calculation
    for num in range(smaller, bigger + 1): # loop through numbers
        if num != smaller: # if not first number
            calc += " + " # add plus sign
        calc += str(num) # add number to string
        sum += num # add number to sum
    return f"{calc} = {sum}" # return string and sum

def main():
    num1 = int(input("Please enter a number.\n"))
    num2 = int(input("Please enter another number.\n"))

    print(f"Addition: {addition(num1, num2)}")
    print(f"Subtraction: {subtraction(num1, num2)}")
    print(f"Multiplication: {multiplication(num1, num2)}")
    print(f"Division: {division(num1, num2)}")
    print(f"Sum between: {sum_between(num1, num2)}")

if __name__ == '__main__':
    main()