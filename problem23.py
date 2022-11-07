import math

def is_prime(n):
    F = True
    x = int(math.sqrt(n)) + 1
    for i in range(2,x):
        if (n % i == 0):
            F = False
            break
    return F

# The function below returns the first prime divisor of an integer:
def firstDivisor(n):
    if (n == 0 or n == 1):
        return 1
    for i in range(2,n+1):
        if n%i == 0:
            break
    return i

# This function returns the list of prime factors of an integer:
def listOfDivisor(n):
    l=[1]
    m=n
    while m!=1:
        l.append(firstDivisor(m))
        m=m//firstDivisor(m)
    return l[1:]

#the function removes repeated numbers in a given list
def noRepeat(l):
    M=[l[0]]
    for i in range(1,len(l)):
        if not (l[i] in l[:i]):
            M.append(l[i])
    return M

# The following function returns the p-adic valuation of an integer, where p is a prime number
def counter(n):
    l = listOfDivisor(n)
    M = noRepeat(l)
    K = []
    for i in M:
        K.append(l.count(i))
    return K

# This increment function proposes an increment method to browse a list, it will help us to
# determine the divisors of an integer
def incr(l,K):
    i=0
    while l[i] == K[i]:
        if i < len(l)-1:
            i = i+1
        else:
            break
    l[i] = l[i]+1
    for j in range(i):
        l[j]=0
    return l

# The following function will help us calculate the number of divisors of an integer
def prod(l):
    p=1
    for i in range(len(l)):
        p=p*(1+l[i])
    return p

# The main function: gives the list of positive divisors of an integer given as input
def division(n):
    l = listOfDivisor(n)
    M = noRepeat(l)
    K = counter(n)
    D = [1]
    L = [0 for i in range(len(K))]
    for i in range(prod(K)-1):
        d = 1
        Y = incr(L,K)
        for i in range(len(M)):
            d = d*(M[i]**Y[i])
        D.append(d)
    return sorted(D)

def sum_proper_divisors(n):
    L = division(n)
    return sum(L[:-1])

def is_abundant(n):
    m = sum_proper_divisors(n)
    return (m <= n)

result = 0
for i in range(24, 28):
    # 28124
    for j in range(12, i - 11):
        x = True
        if (is_abundant(j) and is_abundant(i - j)):
            x = False
            break
        if (x):
            result += i
            print(i)

print(result)