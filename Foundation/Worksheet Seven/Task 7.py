# Program for birth rate calculation.



def br_calc():
    # Input
    
    population = int(input("Please enter the population.\n"))
    while population < 2:  # not to accept less than 2
        population = int(input("Please enter the population.\n"))

    death_rate = int(input("Please enter the death rate.\n"))
    while death_rate < 0:  #not to accept negative numbers
        death_rate = int(input("Please enter the death rate.\n")) 

    birth_rate = int(input("Please enter the birth rate.\n"))
    while birth_rate < 0:  #not to accept negative numbers
        birth_rate = int(input("Please enter the birth rate.\n"))    
        
    number_of_years = int(input("Please enter the number of years.\n"))
    while number_of_years < 1:
        number_of_years = int(input("Please enter the number of years.\n"))

    # Calculation

    new_population = population + (birth_rate*population) - (death_rate*population)

    # Loop for the number of years

    for i in range(number_of_years - 1):

        new_population = new_population + birth_rate - death_rate

    # Output

    print(f"The new population is {new_population}.")

if __name__ == '__main__':
    br_calc()
