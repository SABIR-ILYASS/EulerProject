import math

# The function below returns the first prime divisor of an integer:
def first_divisor(n):
    if (n == 0 or n == 1):
        return 1
    for i in range(2,n+1):
        if n%i == 0:
            return i

#the function removes repeated numbers in a given list
def no_repeat(l):
    M=[l[0]]
    for i in range(1,len(l)):
        if not (l[i] in l[:i]):
            M.append(l[i])
    return M

# This function returns the list of prime factors of an integer:
def list_of_divisor(n):
    l=[1]
    m=n
    while m!=1:
        l.append(first_divisor(m))
        m=m//first_divisor(m)
    return no_repeat(l[1:])

result = 646
while True:
    n1 = len(list_of_divisor(result))
    n2 = len(list_of_divisor(result + 1))
    n3 = len(list_of_divisor(result + 2))
    n4 = len(list_of_divisor(result + 3))
    if (n1 == 4 and n2 == 4 and n3 == 4 and n4 == 4):
        break
    result += 1

print(result)
