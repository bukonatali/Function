# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём. Число – кол-во нечётных цифр.
# Строка – количество букв. Сделать проверку со всеми этими случаями.

def f(a):
  if type(a) == tuple:
    print('слов', len(a))
  elif type(a) == list:
    print('букв', len(list(filter(lambda x: type(x) == str, a))),
          'чисел', len(list(filter(lambda x: type(x) in (int, float), a))))
          # 'нечетных чисел', len(list(filter(lambda x: (x%2 == 0) , a))))
  elif type(a) == str:
    print('букв', len(a))
  else:
    print('Неизвестный тип')

f((1111, 2, 3, 'a','h',3))
f([1, 2, 3,5, 'a', 'b', 'c','k'])
f('abcd2356hjh')
f({5: 11})


# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа.Операции являются функциями.
# Обработать ошибку: “Деление на ноль” Ноль использовать в качестве завершения программы(сделать
# как отдельную операцию).
# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# def calc( op, a, b ):
#     match op:
#         case '+':
#             return a + b
#         case '-':
#             return a - b
#         case '*':
#             return a * b
#         case '/':
#             try:
#                 return a / b
#             except:
#                 return 'Деление на ноль'
# while True:
#     print()
#     op = input('Введите операцию (+, -, *, /, 0): ')
#     if op == '0':
#         break
#     if op in '+-*/':
#         while True:
#             try:
#                 a, b = map( float, input( 'Цифры вводить через пробел a, b = ' ).split() )
#                 print( calc( op, a, b ) )
#                 break
#             except:
#                 pass
#






