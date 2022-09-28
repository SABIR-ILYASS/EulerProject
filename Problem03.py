""" project 02 """

def sumPairFibonnaci(n):
    L = [1,1]
    sum = 0
    i = 0
    while (L[i]<n):
        if (L[i]%2 == 0):
            sum += L[i]
        L.append(L[i]+L[i+1])
        i += 1
    return sum

""" project 03 """
# The function below returns the first prime divisor of an integer:
def firstDivisor(n):
    j = 1
    for i in range(2,n+1):
        if n%i == 0:
            j = i
            break
    return j


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
    if (l == []):
        return l
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

# The following function is a sort function of a given list
def sortList(l):
    L=l[:]
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            k = i
            if L[j] < L[k]:
                k = j
        m = l[i]
        L[k] = L[i]
        L[i] = L[k]
    return L

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
    return sortList(D)


""" project 12 """
def firstD(a):
    n = 1
    while (len(division(n*(n+1)//2)) < a):
        n += 1
    return (n+1)*(n+2)//2


""" project 04 """
L=[9,8,7,6,5,4,3,2,1,0]
# 999 * 999 = 998001

def isPalanderom (n):
    i = 0
    while (n/(10**i)>1):
        i += 1
    L = []
    for j in range(i):
        L = [(n//(10**j))%10]+L
    b = 0
    for k in range(i//2):
        if (L[k] == L[i-k-1]):
            b += 1
    if (b == i//2):
        return True
    else:
        return False

def largePalandrom (n):
    i = 0
    for j in range (10**n-1,10**(n-1),-1):
        for k in range (10**n-1,10**(n-1),-1):
            if (isPalanderom(j*k)):
                i = j*k
                break
    return i

""" project 05 """
def listOfPrimeNumber(n):
    j = 1
    for i in range(2,n+1):
        if n%i == 0:
            j = i
            break






