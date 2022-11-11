def collatz(n):
    if (n % 2 == 0):
        return n // 2
    else:
        return 3 * n + 1

def number_of_terms_collatz(n):
    collatz_step = n
    count = 1
    while (collatz_step != 1):
        collatz_step = collatz(collatz_step)
        count += 1

    return count

result = 1
max_numbers_of_terms = 0
for i in range(1,1000001):
    count = number_of_terms_collatz(i)
    if (count > max_numbers_of_terms):
        max_numbers_of_terms = count
        result = i

print(result)