# write a for loop to display multiples of 5 backwards from 100 to 0

def main():

    for number in range(100, 0, -5):
            print(number) # a step of -5 is the same as %5 == 0 to find multiples

if __name__ == '__main__':
    main()