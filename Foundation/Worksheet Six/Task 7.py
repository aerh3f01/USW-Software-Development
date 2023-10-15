# Function that accepts two integers
# Using two if statements, returns the values in ascending order

def ascending_order(num1, num2):
    if num1 > num2:
        return num2, num1
    if num1 < num2:
        return num1, num2
    
if __name__ == '__main__':
    num1 = int(input("Please enter a number.\n"))
    num2 = int(input("Please enter another number.\n"))
    print(ascending_order(num1, num2))