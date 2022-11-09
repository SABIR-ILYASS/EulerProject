import math

# list of all permutation possible for a giving number n
def list_premutation(n):
    atom_list = [i for i in range(1, n + 1)]
    list_of_all_premutation = []
    list_of_all_premutation.append(atom_list)
    for k in range(0,n-1):
        for i in range(0, len(list_of_all_premutation)):
            premutation_step = list_of_all_premutation[i][:]
            for c in range(0,n-k-1):
                premutation_step.append(premutation_step.pop(k))
                if (premutation_step not in list_of_all_premutation):
                            list_of_all_premutation.append(premutation_step[:])
    return list_of_all_premutation

# Primality test function
def is_prime(n):
    F = True
    x = int(math.sqrt(n)) + 1
    for i in range(2,x):
        if (n % i == 0):
            F = False
            break
    return F

# transform a list of integers to an integer
def list_to_number(list):
    n = ""
    for i in range(len(list)):
        n += str(list[i])
    return int(n)

result = 0
for j in [4,7]:
    list_perm = list_premutation(j)
    for i in range(len(list_perm)):
        num = list_to_number(list_perm[i])
        if (is_prime(num)):
            if (num > result): 
                result = num

print(result)