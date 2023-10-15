# Working out what this code will do

# It should times the number from 0 - 10 (row) with the number col which will equate to 0 - 10

# Testing

def main():
    for row in range(0, 11):
        print()
        for col in range(0, row+1):
            print(row*col, end=" ")
    print()

if __name__ == '__main__':
    main()

# It turns out to print different times tables in assending and growing order
