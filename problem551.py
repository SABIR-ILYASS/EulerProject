""" probleme 551 - project Euler
By SABIR Ilyass.
"""

x, count = 1,0

def sum_digits(n):
   rest = 0
   while (n != 0):
       rest, n = rest + n % 10, n // 10
   return rest

def answer_problem_551(n):
    global x, count
    if (count >= n):
        return -1
    else:
        for i in range (n - count - 1):
            x += sum_digits(x)
            count += 1
        return x


print(answer_problem_551(10 ** 15))

