# Print all the odd numbers between 1 - 100

def main():

    for number in range(1, 101):
        if number %2 != 0:
            print(number)


if __name__ == '__main__':
    main()