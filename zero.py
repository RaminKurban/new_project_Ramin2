# import math ( вызов библеотеки математики)
#from rumath import koren
#from math import sqrt as koren  ( as - копирование из другой библиотеки)


print(" Программа для решения квадратных уравнений ")
bad_data = True
# используем try если может произойти ошибка в строке !
# #bad_data - плохие данные
while bad_data == True:
    try:
        a = int(input("введите число a:"))
        b = int(input("введите число b:"))
        c = int(input("введите число  c:"))
        bad_data = False
    except ValueError:
        print('не перевести к числу')
# except ValueError используем чтобы  выдало не ошибку, а сообщение.

D = (b * b) - (4 * a * c)
# D - дискриминант
print(D)

if D > 0:
    d = sqrt(D)
    x1 = ((-b) + d) / (2 * a)
    x2 = ((-b) - d) / (2 * a)
    print(f'уравнение имеет 2 корня. x1 = {x1} , x2 = {x2}')
elif D == 0:
    x1 = (-b) / (2 * a)
    print('уравнение имеет 1 корень. x1 = {}'.format(x1))
else:
    print('корней нет')
