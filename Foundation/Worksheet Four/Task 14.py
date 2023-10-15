# Program that uses nested loops to produce an output of:
# 8 to 1 (newline) 9 to 2 (newline) 10 to 3 (newline) 11 to 4 (newline) 12 to 5

def main():
    for row in range(8, 13):
        for col in range(row, row - 8, -1):
            print(col, end=" ")
        print()

if __name__ == '__main__':
    main()