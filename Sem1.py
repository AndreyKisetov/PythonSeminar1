# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
#    является ли одно число квадратом другого.

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# if a**2 == b:
#     print(a,',', b, '-> да')
# else:
#     print(a,',', b, '-> нет')


# 2. Напишите программу, которая на вход принимает 5 чисел и находит 
#    максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a = int(input('Введите первое число: '))
b = int(input('Введите первое число: '))
c = int(input('Введите первое число: '))
d = int(input('Введите первое число: '))
e = int(input('Введите первое число: '))
if a > b:
    print(a,',', b,',', c,',', d,',', e,'->',a)
elif b > c:
    print(a,',', b,',', c,',', d,',', e,'->',b)
elif c > d:
    print(a,',', b,',', c,',', d,',', e,'->',c)
elif d > e:
    print(a,',', b,',', c,',', d,',', e,'->',d)
else:
    print(a,',', b,',', c,',', d,',', e,'->',e) 

