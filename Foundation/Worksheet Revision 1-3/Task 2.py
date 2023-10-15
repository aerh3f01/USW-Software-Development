# Stock management system

# Request stock name, number of items bought, cost of item, and commission
# print out the information plus total cost of purchase

def stock_manager():

    name = input("Enter the product name\n")
    bought = int(input("Enter the quantity\n"))
    cost = float(input("Enter the price of one item\n"))
    commission = int(input("Enter the percentage commission added\n")) / 100

    total_cost = (cost * bought) * (commission + 1)

    print(f"Product: {name}\nQuantity: {bought}\nPrice per Item: £{cost}\n")
    print(f"Commission {commission * 100}%\n \nTotal Cost: £{total_cost}")

if __name__ == '__main__':
    stock_manager()
