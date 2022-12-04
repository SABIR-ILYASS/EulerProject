def factorielle(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

index = 1000000
number_of_digits = 10
list_of_all_digit = [i for i in range(number_of_digits)]

# find the number 
index_step = index

list_of_digit = []
for i in range(number_of_digits):
    fact = factorielle(number_of_digits - 1 - i)
    digit = index_step // fact
    current_digit = list_of_all_digit[digit]

    if (index_step == digit * fact and len(list_of_all_digit) > 1):
        current_digit = list_of_all_digit[1]

    list_of_digit.append(current_digit)
    list_of_all_digit.pop(list_of_all_digit.index(current_digit))

    index_step -= digit * fact

def list_to_int(list_of_num):
    length = len(list_of_num)
    result = 0
    for i in range(length):
        result += list_of_num[i] * (10 ** (length - 1 - i))
    return result


answer = list_to_int(list_of_digit)
print(answer)