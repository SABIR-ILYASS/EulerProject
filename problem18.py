data_string = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

data_list = li = list(data_string.split("\n"))

data = []

for i in range(len(data_list) - 1):
    data
    data.append(list(data_list[i].split(" ")))

length = len(data)

def update(list_incr):
    index = length - 1
    while (index > 0 and list_incr[index] == list_incr[index - 1] + 1):
        index -= 1
    
    list_incr[index] += 1

    for i in range(index, length): list_incr[i] = list_incr[index]

    return list_incr, index


list_step = [0 for i in range(length)]
index = length - 1
result = 0

while index > 0:
    answer = 0
    for i in range(length):
        answer += int(data[i][list_step[i]])
    if answer > result:
        result = answer
    list_step, index = update(list_step)

print(result)
