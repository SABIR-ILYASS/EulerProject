import math

def is_prime(n):
    if (n == 0 or n == 1):
        return False
    x = int(math.sqrt(n)) + 1
    for i in range(2,x):
        if (n % i == 0):
            return False
    return True

def number_prime_consecutive(a,b):
    fun = lambda n : n ** 2 + a * n + b
    count, index  = 0, 0
    num = fun(index)
    while( is_prime(num)):
            count += 1
            index += 1
            num = fun(index)
            if (num < 0): break

    return count

max_number_prime_consecutive = 0
a_max, b_max = 0, 0
for b in range(2, 1001):
    if (is_prime(b)):
        for a in range(-999, 1000):
            number = number_prime_consecutive(a,b)
            if (number > max_number_prime_consecutive):
                max_number_prime_consecutive = number
                a_max, b_max = a, b

print(a_max * b_max)
