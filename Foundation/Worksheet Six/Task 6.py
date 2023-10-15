# Function that accepts two different numbers and returns:
# True and the biggest number ( if different )
# False and 0 ( if the same )

def return_biggest_number(number_one, number_two):
    if number_one == number_two:
        return False, 0
    elif number_one > number_two:
        return True, number_one
    else:
        return True, number_two
    
if __name__ == '__main__':
    number_one = int(input("Please enter a number.\n"))
    number_two = int(input("Please enter another number.\n"))
    print(return_biggest_number(number_one, number_two))