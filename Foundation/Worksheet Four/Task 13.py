# Program that uses nested loops to produce an output of:
# 1 to 8 (newline) 2 to 9 (newline) 3 to 10 (newline) 4 to 11 (newline) 5 to 12

def main():
    for row in range(1, 6):
        for col in range(row, row + 8):
            print(col, end=" ")
        print()

if __name__ == '__main__':
    main()