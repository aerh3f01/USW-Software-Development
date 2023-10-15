''' calculating the area of a rectangle'''

def area():
    length = 23
    breadth = 35
    print("This program calculates the area of a rectangle\n\n")
    print(f"When the length = {length} and the breadth = {breadth}")
    print(f"the area = {length*breadth}")

if __name__ == '__main__':
    area()

# the output does not change in the modified version of 8 as 
# the variables stored are not outputted until the function is called

def area():
    length = 23
    breadth = 35
    area_of_rectangle = length*breadth
    print("This program calculates the area of a rectangle\n\n")
    print(f"When the length = {length} and the breadth = {breadth}")
    print(f"the area of a triangle is half of the rectangle at = {area_of_rectangle/2}")

if __name__ == '__main__':
    area()