# Using task 8 as a template, generate a program to do a triangle with *


def main():

    for row in range(0, 9): # set the range for the rows
        print()
        for number in range(0, row+1): # the last number is number of the row, so + 1 to find the number before
            
            print("*", end="") # keep printing the number + 1 for that row and append "" to continue line
            
    print()
if __name__ == '__main__':
    main()