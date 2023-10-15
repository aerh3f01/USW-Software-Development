# Modifying the code in task 5
#produce a program that lists the multiplication grid for numbers 1 to 10
# it should be in neat columns and rows using the : format operator inside an f-string {} bracket

def main():
    for row in range(1, 11):
        for col in range(1, 11):
            print(f"{row * col:3}", end=" ")
        print()

if __name__ == '__main__':
    main()