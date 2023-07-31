# Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100

from random import randint
def sum(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return n + sum(n-1)
n = ([randint(0, 101) for _ in range(10) ])
print(n)
total = 0
for number in n:
    total += number
print(total)












