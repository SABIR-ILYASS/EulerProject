"""
Euler problem 08
@author: sabir
"""

# data and pre-processing

string_number = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

list_of_numbers = [x for x in string_number]
list_of_numbers = list(filter(lambda a: a != '\n', list_of_numbers))
list_of_numbers = [int(x) for x in list_of_numbers]

# function to compare two sequences of adjacentes numbers.
def compare_two_sequences_of_numbers(list1, list2, size):
    is_bigger = False
    L1, L2 = sorted(list1), sorted(list2)
    for i in range(size):
        if (0 in list2):
            return False
        if L2[size - 1 - i] > L1[size -1 - i]:
            is_bigger = True
            break
        elif (L2[size - 1 - i] < L1[size -1 - i]):
            break
    return is_bigger

# function to calculate the product of the elements of a list
def product_of_elements_of_list(L):
    prod = 1
    for i in range(len(L)):
        prod *= L[i]
    return prod

# function that determines the greatest product of the size adjacent digits        
def must_bigger_sequence(L, size):
    length = len(L)
    max = 0
    for i in range(length - size):
        num = product_of_elements_of_list(list_of_numbers[i:i + size])
        if (num > max): max = num
    return max

size = 13
max = must_bigger_sequence(list_of_numbers, size)

print(max)