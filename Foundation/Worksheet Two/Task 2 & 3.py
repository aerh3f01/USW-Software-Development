## Task 2 & 3       
print("\n\nTask 2 & 3\n")

'''task two and three combined
the main code calculates the tax paid with a little message to output gross salary and tax
the BTI scale is included in this'''
def main():
    salary = 50000
    
    basic_tax_income = 10000
    basic_tax = 0.2
    higher_tax = 0.3
    
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
    

