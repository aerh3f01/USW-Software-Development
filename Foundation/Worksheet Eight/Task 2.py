# Program of 20 integers
# Each is a random number between 1 and 100

# Display all on a line
# Even on the next line
# Odd on the next
# All 20 on the last

from random import randint

def main():

    for i in range(0,20):
        number = randint(1,100)
        randlist(number)
    
    evenlist = []
    if number %2 == 0:
        evenlist.append(number)

    for i in range (0, len(evenlist)):
        print(evenlist[i], end=" ")


if __name__ == '__main__':
    main()