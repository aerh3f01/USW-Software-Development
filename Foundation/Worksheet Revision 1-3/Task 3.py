# writing out the first three fibonacci numbers
# displaying the first three numbers
def display_fibonacci():

    num_fibonacci = int(input("Enter the number of fibonacci numbers to display")) # number of figures to display

    num1, num2 = 0, 1 # first two numbers in sequence

    for i in range(num_fibonacci):
        print(num1)
        num1, num2 = num2, num1 + num2 #adding the two numbers and resetting the sequence

if __name__ == '__main__':
    display_fibonacci()
