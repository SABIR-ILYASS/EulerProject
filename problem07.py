import math
""" project 07 """
def isPythagore(a,b,c):
    if ((a**2+b**2) == c**2):
        return True
    else:
        return False

def product(n):
    pro = 0
    for c in range (n//3,n):
        for b in range (1,n//3):
            a = math.sqrt(c**2-b**2)
            if (a == int(a) and a>0):
                if (a+b+c == n):
                    pro = c*b*a
    return pro
""" auther project """
def sum(n):
    a=int(math.log10(n))+1
    s = 0
    for i in range(a):
        s += (n//(10**i))%10
    return s

""" project 20 """
def Sumfact(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return sum(fact)

""" project 7"""
def isPrime(n):
    if (n == 1):
        return False
    else:
        f = True
        for i in range(2,int(math.sqrt(n))+1):
            if (n%i == 0):
                f = False
                break
        return f
def prime(n):
    b = 0
    s = 1
    while (True):
        if (isPrime(s)):
            b += 1
        if (b == n):
            break
        s += 1
    return s

def sumPrime(n):
    s = 0
    a = 1
    while(a<=n):
        if (isPrime(a)):
            s += a
        a += 1
    return s

def largeSum(n):
    s=n
    while(s>0):
        a = sumPrime(s)

        if (isPrime(s) and isPrime(a) and a<=n):
            break
        s -= 1
    return sumPrime(s)




