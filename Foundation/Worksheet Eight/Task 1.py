# create a list of i + 19
# multiply by 7

# then create three rows of output, with the middle row being reversed


def forwards(number, multi):
    step = 0
    for i in range(0, 20):
        print (step*multi, end=" ")
        step += number

def backwards(number, multi):
    step = number * 19
    for i in range(0,20):
        print(step*multi, end=" ")
        step -= number


if __name__ == '__main__':
    num = int(input("Please enter a number.\n"))
    multi = 7
    forwards(num, multi)
    print()
    backwards(num, multi)
    print()
    forwards(num, multi)