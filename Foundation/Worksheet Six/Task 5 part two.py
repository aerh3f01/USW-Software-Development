# "leasure time adviser" that has a parameter of age to determine what the user should do
# instead of displaying a message, it returns advice as a string value to be displayed

def leisure_time_adviser(age):
    if age >= 18:
        cash = int(input("Please enter the amount of cash you have.\n"))
        if cash >= 20:
            return "Go to the pub for a drink." 
        else:
            return "Go for a walk."

    else:
        like_films = input("Do you like films? Y/N\n")
        if like_films == "Y" or like_films == "y":
            return "Watch netflix."
        else:
            return "Play computer games."

if __name__ == '__main__':
    age = int(input("Please enter your age.\n"))
    
    print(leisure_time_adviser(age))   
        