import math

def length_number(n):
    return int(math.log10(n)) + 1

def is_candidat_pandigital(string_num):
    F = True
    for i in range(1, 10):
        if (not(str(i) in string_num)):
            F = False
            break
    return F

result = 0


for i in range(1,100000):
    length = 0
    x = 1
    num_string = ""
    while(length < 9):
        power = i * x
        length += length_number(power)
        num_string += str(power)
        x += 1
    if (length == 9):
        if (is_candidat_pandigital(num_string)):
            print(num_string)
            num = int(num_string)
            print(num)
            print(i)
            
            if (result < num):
                result = num
    
print(result) 
