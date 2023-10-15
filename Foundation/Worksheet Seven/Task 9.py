# Write a function named is_prime 
# Find the prime numbers between 1 and 10000


# 2, 3 and 5 are default primes, so print to make the first loop
# Then check if divisable by 2 or 3, then check if divisable by prime 
# Then return numbers in a list and print


def is_prime(number):
    
    if number <= 1:
        return False
    if number <= 3:
        return True
    
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5

    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == '__main__':
    prime_numbers = [num for num in range(1, 10001) if is_prime(num)]
    print(prime_numbers)