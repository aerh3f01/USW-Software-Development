# Two for loops nested to display 1 - 100
# 10 numbers per line, across 10 lines


def main():
    for row in range(10):
        print()
        for number in range(1 + row * 10, 11 + row * 10): # calculates based on line number (1 - 10, 11 - 20, 21- 30 etc)
            print(number, end=" ")
    print()

if __name__ == '__main__':
    main()