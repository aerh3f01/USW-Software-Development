# Predict the output of the following code:

# The code will print out 0,0 0,1 0,2 up to 2,3 as the first while loop will run
# 3 times and the second nested while loop will run 4 times for each time the first while loop runs

def main():
    num1 = 0
    while num1 < 3:
        num2 = 0
        while num2 < 4:
            print(f"num1 = {num1} num2 = {num2}")
            num2 += 1
        num1 += 1
    print()

if __name__ == '__main__':
    main()