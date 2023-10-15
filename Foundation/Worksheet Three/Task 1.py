def main():
    age = int(input("Please enter your age: \n"))

    if age>= 18:
        print("You can vote!")
    else: 
        print("Sorry! You are too young to vote.")

if __name__ == '__main__':
    main()


# 1.2

def main():
    age = int(input("Please enter your age: \n"))

    if age >= 18:
        cash= int(input("How much money do you have? \n"))
        if cash >= 20:
            print("I suggest you go to the pub for a drink.")
        else: 
            print("I suggest you go for a walk.")
    else:

        like_films = input("Do you like films? (Enter Y or N)\n")
        if like_films == "Y" or like_films == "y":
            print("I suggest you watch Netflix.")
        else: print("I suggest you play a computer game.")

if __name__ == '__main__':
    main()