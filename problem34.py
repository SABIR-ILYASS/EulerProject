import math

fact_digit = [1]
for i in range(1,10):
    fact_digit.append(fact_digit[i - 1] * i)

def is_sum_fact_digit(n):
    str_n = str(n)
    sum_n = 0
    for i in range(len(str_n)):
        sum_n += fact_digit[int(str_n[i])]
    return sum_n == n

result = 0
for i in range(3, 1500000):
    if is_sum_fact_digit(i):
        result += i

print(result)