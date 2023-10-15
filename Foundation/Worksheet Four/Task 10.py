# write double loops for making a full arrow



def main():

    for row in range(0, 9):
        print()
        for number in range(0, row+1): 
            print("*", end="") 
            
    for row in range(9, 0, -1):
        print()
        for number in range(0, row-1):
            print("*", end="")

    print()
if __name__ == '__main__':
    main()