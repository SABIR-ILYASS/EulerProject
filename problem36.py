def number_to_list(n):
    string_n = str(n)
    L = []
    for i in range(len(string_n)):
        L.append(int(string_n[i]))
    return L

def is_palindrome(L):
    length = len(L)
    for i in range(length // 2):
        if (L[i] != L[length - i - 1]):
            return False
    return True

def is_both_palindrome(n):
    binary_n = bin(n).replace("0b", "")
    list_dec = number_to_list(n)
    list_bin = number_to_list(binary_n)
    return (is_palindrome(list_dec) and is_palindrome(list_dec))

result = 0
for n in range(1000001):
    binary_n = bin(n).replace("0b", "")
    list_dec = number_to_list(n)
    list_bin = number_to_list(binary_n)
    if is_palindrome(list_dec):
        if is_palindrome(list_bin):
            result += n

print(result)