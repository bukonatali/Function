# 1  Создайте функцию, добавьте в неё локальное значение.
# Сделайте так, чтобы другая функция принимала это значение в качестве параметра.

def function_a():
    global a
    a = 11
    b = 36
    return a + b

def function_b():
    c = 3
    return a + c

print(function_a())
print(function_b())








# 2Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.


# def is_prime(number):
#     if number > 0 and number < 1001:
#         return False
#     for b in range(2, number):
#         if number % b == 0:
#             return False
#     return True
# print(is_prime(int(input("Число: "))))










