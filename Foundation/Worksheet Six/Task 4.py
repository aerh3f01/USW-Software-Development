# Enter the following code and explain what the sum+=count does:

def return_sum():
    sum = 0 
    for count in range(1, 15):
        sum += count

    return sum

if __name__ == '__main__':
    print(return_sum())

# The sum+=count adds the value of count to the value of sum.
# The value of count is incremented by 1 each time the loop runs.
# The loop runs 14 times, adding 1 to count each time.
# The sum of the numbers from 1 to 14 is 105.