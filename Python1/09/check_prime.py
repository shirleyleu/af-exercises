# check_prime implements a algorithmically naive, but easily readable, test for primes
from math import sqrt


# Function is_prime returns True if a given number is prime
def is_prime(n):
    # Edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Check if test number is divisible by remaining numbers less than its square root
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
