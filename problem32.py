import math

def is_different_digit(n1, n2):
    str_n1, str_n2 = str(n1), str(n2)
    for i in range(len(str_n1)):
        if str_n1[i] in str_n2:
            return False
    for i in range(len(str_n2)):
        if str_n2[i] in str_n1:
            return False
    return True

def is_pandigital(n1, n2):
    product = n1 * n2
    str_n1, str_n2, str_n3 = str(n1), str(n2), str(product)
    length = len(str_n1) + len(str_n2) + len(str_n3)
    if length != 9: return False
    if not is_different_digit(n1, n2):
        return False
    if not is_different_digit(n1, product):
        return False
    if not is_different_digit(n2, product):
        return False
    
    count = 0
    for i in range(1,10):
        if str(i) in str_n1:
            count += 1
        if str(i) in str_n2:
            count += 1
        if str(i) in str_n3:
            count += 1
    return count == 9

result = 0
List_all_product = []
for n1 in range(1, 10 ** 4):
    exp = int(math.log10(n1)) + 1
    b_min, b_max = 4 - exp, 5 - exp
    for n2 in range(10 ** b_min, 10 ** b_max + 1):
        if (is_pandigital(n1, n2)):
            product = n1 * n2
            if product not in List_all_product:
                List_all_product.append(product)
                result += product

print(result)