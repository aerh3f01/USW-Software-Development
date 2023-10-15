# Scenario: 
# You have been hired by Logistics Ltd to help develop their logistics management system.
# One day, your boss comes in to ask you to develop a simple Python program that loads in
# both sales and purchase data, and outputs profit calculations. Thankfully, someone has
# already provided you with a main function, saving you from having to do this, and this has
# been provided for you below

# Your program should use a function called ‘load_sales_data ’to load sales data from a file
# called ‘sales_data.txt ’and a function called ‘load_purchase_data ’to load purchase data
# from a file called ‘purchase_data.txt’, both located in the same directory as your Python file


# This function takes in two lists of stock items bought and sold, and calculates and displays the profit data for each item and the total profit
def output_profit_data(stock_items_bought: list, stock_items_sold: list):
    # Create an empty list to store the profit data for each product
    product_data = []

    # Loop through the stock_items_bought list, stepping by 4 because each product has 4 lines of data
    for i in range(0, len(stock_items_bought), 4):
        # Extract the data for each product from the stock_items_bought and stock_items_sold lists
        name = stock_items_bought[i]
        no_of_items_bought = int(stock_items_bought[i+1])
        buy_price = float(stock_items_bought[i+2])
        buy_commission_rate = float(stock_items_bought[i+3])

        no_of_items_sold = int(stock_items_sold[i+1])
        sale_price = float(stock_items_sold[i+2])
        sale_commission_rate = float(stock_items_sold[i+3])

        # Calculate the money spent buying and money earned selling for each product, and the profit
        money_spent_buying = no_of_items_bought * buy_price *(1 + buy_commission_rate)
        money_earned_selling = no_of_items_sold * sale_price * (1 - sale_commission_rate)
        profit = money_earned_selling - money_spent_buying

        # Store the product data in a dictionary and append it to the product_data list
        product_info = {
            'name': name,
            'no_of_items_bought': no_of_items_bought,
            'buy_price': buy_price,
            'buy_commission_rate': buy_commission_rate,
            'no_of_items_sold': no_of_items_sold,
            'sale_price': sale_price,
            'sale_commission_rate': sale_commission_rate,
            'money_spent_buying': money_spent_buying,
            'money_earned_selling': money_earned_selling,
            'profit': profit
        }
        product_data.append(product_info)

    # Loop through the product_data list and display the profit data for each product
    for product in product_data:
        print("================================")
        print(f"{product['no_of_items_bought']} {product['name']} bought for {product['buy_price']} each ({product['buy_commission_rate']*100}% buy commission)")
        print(f"Money spent buying {product['name']} was {product['money_spent_buying']:.2f}")
        print(f"{product['no_of_items_sold']} {product['name']} sold for {product['sale_price']} each ({product['sale_commission_rate']*100}% sale commission)")
        print(f"Money earned selling {product['name']} was {product['money_earned_selling']:.2f}")
        print(f"Profit for {product['name']} was {product['profit']:.2f}")
        print("================================")

    # Calculate the total profit by summing the profit values in the product_data list, and display it
    total_profit = 0
    for product in product_data:
        total_profit += product['profit']
    print("================================")
    print(f"Total Profit: £{total_profit:.2f}")
    print("================================")

# This function takes in a filename and loads the purchase data from the file into a list
def load_purchase_data(filename: str):
    # Create an empty list to store the stock items bought
    stock_items_bought = []
    # Open the file and read each line into the stock_items_bought list
    file = open(filename)
    line = file.readline().strip()
    while line != "":
        stock_items_bought.append(line)
        line = file.readline().strip()
    file.close()
    return stock_items_bought

# This function takes in a filename and loads the sales data from the file into a list
def load_sales_data(filename: str):
    # Create an empty list to store the stock items sold
    stock_items_sold = []
    # Open the file and read each line into the stock_items_sold list
    file = open(filename)
    line = file.readline().strip()
    while line != "":
        stock_items_sold.append(line)
        line = file.readline().strip()
    file.close()
    return stock_items_sold

# If this file is being run as the main program, load the purchase and sales data and output the profit data
if __name__ == '__main__':
    stock_items_bought = load_purchase_data("purchase_data.txt")
    stock_items_sold = load_sales_data("sales_data.txt")
    output_profit_data(stock_items_bought, stock_items_sold)

