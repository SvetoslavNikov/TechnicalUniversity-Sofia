import math
import random
import cmath

print(random.random())  # random number between 0 and 1
print(random.randint(-10, 30))  # start, end
print(random.randrange(1, 10, 1))  # start, end , step
print(random.uniform(-100, 99))  # random float

a = random.randint(-10, 10)
b = random.randint(-10, 10)
c = random.randint(-10, 10)

print(f'{a}x**2+{b}x+{c}=0')  # f - formatirasht list imeenata na promenliwi w skobite shte se zamenqt ot stojnostite # im
print('{0}x**2+{1}x+{2}=0'.format(a, b, c))

if a == 0:
    print('No solution..')
else:
    d = b ** 2 - 4 * a * c
    x1 = (-b - cmath.sqrt(d)) / (2 * a)
    x2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('x1=', x1, '\nx2=', x2)

    # %f - float, %d - int, %s - string
    print('a=%4f\ntb=%.2f' % (a, b))

    # float precision failure
    print(0.1 + 0.2)

    # so we round them
    print(round(0.1 + 0.2, 10))
    print(math.floor(0.1 + 0.2))
    print(math.ceil(0.1 + 0.2))

s = '0123456789X'
print(s[0], s[1])
print(s[-4], s[-1])
print(s[5:])
print(s[:3])
print(s[5:10])
# s[1] = 'X' == TypeError: 'str' object does not support item assignment
# защото стринг е immutable or other called const

print(s + '!!')
# print(s + 3.14) - false
print(s + '3.14')
print(3 * s.split(" "))

# a = """Lorem ertd"""#тройните кавички дават възможност за документиране на кода search more info
print(cmath.sqrt.__doc__)  # име на модул име на функция . док и дава документацията на функцията

# .length in java in python is len()
print(s[len(s) - 1])  # we put - 1 because len count starting with 1, but the index start at 0

# s съдържа ли 'X'
print('x' in s)
print('X' in s)

# search methods in python in web 3 scools
# upper(), title(), isalnum(), isdigit(), isdecimal(), isnumeric, istitle(), islower(),
# isspace() - ima li whitespace - това са управляващи символи like \ check what they are
# isprintable() - да не съдържа управляващи символи, под 32 в Ascii table

s1 = "Hello, python!"
print(s.islower())
print(s.isalpha())
print('C:\some\name')
print(r'C:\some\name')  # r показва че управляващите знаци като \ are String

# index - give symbol and the method search in the String if there is a such symbol
# and return the index of the first found such symbol, otherwise it returns - 1

print(s1.index('H'))
if 'h' in s:
    print(s.index('h'))

print(s.find('h'))
# endwith() - check if string end with()
# rindex() - search right to left
# rfind() - search right to left
# rsplit() - split but right tp left
# map () - lecture 1
print(s1.replace('H', 'h'))  # it replace it just for this line
print(s1)

s1 = s1.replace('H', 'h')  # replace it
print(s1)

s2 = s1 * 3
# s2 = s2.replace('H','h', 0)#replace every H with h
print(s2)

# goal to replace all the H with h but skiiiping the first
# but it doesnt working - how to fix it?
i = s2.find('H')
if i > -1:
    print(s2[:(i + 1)] + s2[(i + 1):].replace('H', 'h'))

# lorem ipsum -  random latin text that contain every combination of symbols?
# lipsom.com - text genarator that you can format

# LOOPS while, for, for each
# iteration - обхождане на цикъла
# there is no do while loop in python

# for each
for ch in s2:
    print(ch)

# range(горна граница на интервала) долната си е 0, само цели числа
for n in range(5):
    print(n, end=' ')
print()

for n in range(-5, 10, 2):  # стъпка2
    print(n, end=' ')
print()

# за range version with floating ponts we use arange(), but for this function we need to install a modul with this function
# how to install search and test the fallowing code
# for x in np.arange(0.1, 10, 3):
#     print(x, end=' ')
# print()

sodd = seven = 0
for n in range(0, 10):  # range = 1 2 3 4 5 6 7 8 9
    if n % 2 == 0:
        seven += n
    else:
        sodd += n

print('Sum of Odd:', sodd, 'Sum of Even:', seven)

sodd = seven = 0
for i in range(10):  # range = 1 2 3 4 5 6 7 8 9
    n = random.randint(-15, 10)
    print(n, end=' ')
    if n % 2 == 0:
        seven += n
    else:
        sodd += n
print()
print('Sum of Odd:', sodd, 'Sum of Even:', seven)

init = True
while True:
    n = int(input('n='))
    if n == 0:
        break
    # първа работа
    if init:
        max = n  #
        init = not init  # става false and it doesnt repeat
    elif max < n:
        max = n
if init:
    print('No data')
else:
    print('Max=', max)
