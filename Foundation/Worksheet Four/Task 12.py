# Program to take an interger input and create a multiplication table
# for that number up to 12.

def main():
    num = int(input("Enter a number."))
    for i in range(1, 13):
        print(f"{i} x {num} = {num * i}")

if __name__ == '__main__':
    main()