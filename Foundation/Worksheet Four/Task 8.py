# two loops nested to display numbers 1 - 9 in triangle style


def main():

    for row in range(0, 9): # set the range for the rows
        print()
        for number in range(0, row+1): # the last number is number of the row, so + 1 to find the number before
            
            print(number+1, end="") # keep printing the number + 1 for that row and append "" to continue line
            
    print()
if __name__ == '__main__':
    main()