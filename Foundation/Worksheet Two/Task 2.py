
        
## Task 2        
print("\n\nTask 2 & 3\n")

'''task two and three combined
the main code calculates the tax paid with a little message to output gross salary and tax
the BTI scale is included in this'''
def main():
    salary = 10000
    
    basic_tax_income = 10000
    basic_tax = 0.2
    higer_tax = 0.3
    
    paid_under = 0
    paid_over = 0
    gross = 0
    tax_paid = 0
    
    
    if salary > basic_tax_income:
        paid_under = basic_tax_income * basic_tax
    else:
        paid_under = salary * basic_tax
    
    if salary > basic_tax_income:
        paid_over = (salary - basic_tax_income) * higher_tax
        
    tax_paid = (paid_over + paid_under)
    gross = salary - tax_paid
    
    print(f"The salary is {salary}, the client has paid {tax_paid} in taxes and has a gross salary of {gross}") 
if __name__ == '__main__':
    main()
    
# Task 4 
print("\nTask 4 & 5\n")

def main():
    pounds = int(input("Please enter the number of pounds to convert \n"))
    dollars = 0
    # exchanges at the time of writing are correct 3/10 12:27
    exchange_dp = 0.83
    exchange_pd = 1.21
    service_charge = 0.1
    
    dollar_pound = dollars * exchange_dp
    pound_dollar = pounds * exchange_pd
    
    print(f"If I convert £{pounds} to dollars, I get ${pound_dollar}.")
    '''adding service charge'''
    gross_exchange_int = pound_dollar * (1-service_charge)
    charge = pound_dollar - gross_exchange_int
    print(f"After applying a 10% service charge ({round(charge, 2)}) to the pounds exchange, you are left with ${round(gross_exchange_int, 2)}")
if __name__ == '__main__':
    main()
    
    
# Task 5 

print("\nTask 5 \n")

def velocity():
    u = 0
    a = float(input("Please enter the acceleration in metre per second\n")) 
    t = float(input("Please enter the time in seconds\n"))
    v = u + (a*t)
    print(f"Assuming the car started from rest, the final velocity in {t} seconds would be {v}m/s/s")
    
if __name__ == '__main__':
    velocity()

def distance1():
    v = float(input("\nPlease enter the final velocity of the car\n"))
    u = 0
    t = float(input("Please enter the time of travel\n"))
    
    s = 0.5 * (v+u) * t
    print(f"Distance 1 is {s}")
    
if __name__ == '__main__':
    distance1()
    
def distance2():
    u = float(input("\nPlease enter the initial velocity of the car\n"))
    a = float(input("Please enter the acceleration of the car\n"))
    t = float(input("Please enter the time of travel\n"))
    
    s = (u*t) + (0.5 * (a * (t*t)))
    print(f"Distance 2 is {s}")
    
if __name__ == '__main__':
    distance2()
    
def v_squared():
    u