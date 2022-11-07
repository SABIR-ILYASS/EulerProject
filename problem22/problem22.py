# importing data
f = open("p022_names.txt", "r")
s = f.read()
s = s.replace('"',"")
list_s =  s.split(",")

# data traitment
data =["A", "B", "C", "D", "E",	"F", "G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def score(string):
    sc = 0
    for i in range(len(string)):
        sc += data.index(string[i]) + 1
    return sc

# sorting list_s

def compare(string1, string2):
    n = min(len(string1), len(string2))
    F = True
    i = 0
    while(i < n):
        if(string1[i] == string2[i]):
            i += 1
        else:
            break
    if (i == n):
        return False
    elif (data.index(string1[i]) < data.index(string2[i])):
        F = False
    return F


def sotring(L):
    if L == []:
        return []
    index_min = 0
    for i in range(1,len(L)):
        if (compare(L[index_min],L[i])):
            index_min = i
    min = L[index_min]
    L[index_min] = L[0]
    L[0] = min
    return [L[0]] + sotring(L[1:])

list_sorted = sorted(list_s[:])
print(list_sorted)
            
result = 0

for i in range(len(list_sorted)):
    result += score(list_sorted[i]) * (i + 1) 

print(result)
