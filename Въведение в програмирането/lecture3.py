#Сложен тип данни - тип, който съхранява повече от един тип данни в паметта 
#- пример списъци, класове (в другите езици и масиви)

#Какво са списъци? слицинг провери какво е?
#за разлика от стринга списъка е mutable , може да се променят цели части от тях

#
numbers = [1,2,3,4,5]

print(len(numbers))
for i in range(len(numbers)):#why it gives us i from 0 to 4 but not form 0 to 5 if len return a number of items
    print(numbers[i], end=' ')

print(len.__doc__)


for i in numbers:#its wrong because that is for each loop
    #and this loop is only for reading a list not for changing it
    i*=10#this doesnt work
print(numbers)


even = []
for n in numbers:
    if n%2==0:
        even.append(n)#add an element to the end of a list
print(even)

#slicing
print(even[-1])
even[-1]=121
print(even)
numbers[2:4] = [+111,+222,+333,+444]
print(numbers)

a,b=0,1
while b<10:#списък на фибоначи
    print(b, end=' ')
    a, b = b, a+b
print()

fib = []
a, b = 0,1
for i in range(0,10):
    fib.append(a)
    a, b = b, a+b
print(fib)

#type import datetime
import datetime

#dd-mm-yyyy input
bdate = datetime.datetime.strptime(input('bdate = '),'%d-%m-%Y')
print(datetime.datetime.strftime(bdate+datetime.timedelta(days=100),'%d-%m-%Y'))
#we add 100 days to our date of input




