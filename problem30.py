import math
def is_sum_4power(n, pow):
    str_num = str(n)
    rep = 0
    for i in range(len(str_num)):
        rep += int(str_num[i]) ** pow
    return rep == n


result = 0

for i in range(2, 9 ** 6):
    if is_sum_4power(i, 5):
        result += i

print(result)
