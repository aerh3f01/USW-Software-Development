# Modular program to calculate paint required for a room and labour cost
# 110 sq ft per gallon of paint and 8 hours of labour
# Labour rate is £20 per hour

# Validations 
# no less than one for number of rooms, no less than £10 in value
# no more than £40 for a gallon pf paint
# no negatives in square footage

# Input

# number of rooms
def get_number_of_rooms():
    number_of_rooms = int(input("Please enter the number of rooms.\n"))
    while number_of_rooms < 1:
        number_of_rooms = int(input("Please enter the number of rooms. (must be more than one room)\n"))
    return number_of_rooms

# square footage per room
# using for loop based on number of rooms
def get_square_footage(number_of_rooms):
    total_square_footage = 0
    for i in range(number_of_rooms):
        square_footage = int(input("Please enter the square footage of the room.\n"))
        while square_footage < 0:
            square_footage = int(input("Please enter the square footage of the room. (must be more than zero)\n"))
        total_square_footage += square_footage
    return total_square_footage

# paint price per gallon
def get_paint_price():
    paint_price = float(input("Please enter the price of the paint per gallon.\n"))
    while paint_price < 10 or paint_price > 40:
        paint_price = float(input("Please enter the price of the paint per gallon. (must be between £10 and £40)\n"))
    return paint_price

# Output

# paint required
def get_paint_required(total_square_footage):
    paint_required = total_square_footage / 110
    return paint_required

# labour required
def get_labour_required(total_square_footage):
    labour_required = total_square_footage / 8
    return labour_required

# cost of paint
def get_cost_of_paint(paint_required, paint_price):
    cost_of_paint = paint_required * paint_price
    return cost_of_paint

# cost of labour
def get_cost_of_labour(labour_required):
    cost_of_labour = labour_required * 20
    return cost_of_labour

# total cost
def get_total_cost(cost_of_paint, cost_of_labour):
    total_cost = cost_of_paint + cost_of_labour
    return total_cost

# main function

def main():
    # data required
    # gallons of paint required
    # hours of labour required
    # cost of paint
    # cost of labour
    # total cost
    number_of_rooms = get_number_of_rooms()
    total_square_footage = get_square_footage(number_of_rooms)
    paint_price = get_paint_price()
    paint_required = get_paint_required(total_square_footage)
    labour_required = get_labour_required(total_square_footage)
    cost_of_paint = get_cost_of_paint(paint_required, paint_price)
    cost_of_labour = get_cost_of_labour(labour_required)
    total_cost = get_total_cost(cost_of_paint, cost_of_labour)
    # output
    print(f"You require {round(paint_required)} gallons of paint.")
    print(f"You require {labour_required:2f} hours of labour.")
    print(f"The cost of paint is £{cost_of_paint:2f}.")
    print(f"The cost of labour is £{cost_of_labour:2f}.")
    print(f"The total cost is £{total_cost:2f}.")
    print("Thank you for using the paint calculator.")

if __name__ == '__main__':
    main()
