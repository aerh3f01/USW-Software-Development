# Explain the following code and how it works:
# Why do we not need to store the value for the current salary?


def value(prompt, low, high):
    value = int(input(f"Please enter {prompt} (value between {low} and {high} -->)"))

    while value < low or value > high:
        value = int(input(f"Please enter {prompt} (value between {low} and {high} -->)"))

    return value

def main():
    age = value("age", 10, 30) # This defines the prompt for age
    print(f"Your age is {age}") 
    print(f"Current salary is {value('current salary', 14000, 55000)}") #This defines the prompt for current salary


# Assuming technical fault in work sheet as there is no call of function (below is missing)
if __name__ == '__main__':
    main()

# This function will return a value between the low and high values.
# It will keep asking the user to enter a value until
# they enter a value between the low and high values.
# We do not need to store the value for the current salary because we are not using it again.

