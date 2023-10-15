## Task 4
 
print("\nTask 4 & 5\n")

def main():
    pounds = int(input("Please enter the number of pounds to convert \n"))
    # exchanges at the time of writing are correct 3/10 12:27
    
    exchange_pd = 1.21
    service_charge = 0.1
    
    pound_dollar = pounds * exchange_pd
    
    print(f"If I convert £{pounds} to dollars, I get ${pound_dollar}.")
    '''adding service charge'''
    gross_exchange_int = pound_dollar * (1-service_charge)
    charge = pound_dollar - gross_exchange_int
    print(f"After applying a 10% service charge ({round(charge, 2)}) to the pounds exchange, you are left with ${round(gross_exchange_int, 2)}")
if __name__ == '__main__':
    main()
    