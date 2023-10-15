# Function that keeps requesting numbers until a 0 is entered
# then returns the highest value

def heighest_value():

    trigger = False
    number = 0

    while trigger == False:
        nums = int(input("Please enter a number.\n"))
        
        if nums > number:
            number = nums
        
        if nums == 0:
            trigger = True
        
    return number

if __name__ == '__main__':
    print(f"The heighest input was {heighest_value()}")