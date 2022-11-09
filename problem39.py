import math

def number_of_solution(n):
    count = 0
    for i in range(1, n // 3 + 1):
        for j in range(i, n):
            for k in range(j, n):
                if (i + j + k == n):
                    a = min(i,j,k)
                    c = max(i,j,k)
                    b = n - a - c
                    if (a**2 + b **2 == c**2):
                        count += 1
    return count

maximum = 0
index = 0
for i in range(1000):
    print(i)
    num = number_of_solution(i)
    if (maximum < num):
        maximum = num
        index = i

print("solution is : " + str(index))
