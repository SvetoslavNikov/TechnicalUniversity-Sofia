
def fib(limit):#function , limit is a parameter
    a,b = 0,1
    while a<limit:
       print(a, sep = '-', end=' ')#point your mouse at print
       a, b = b, a+b
    print()

fib(100)#calling of a function should be after its definition
fib(1000)
print(fib)#calling the adress in the memory
print(fib(200))#return 'None' because we haven't set a return value

def fib2(upper=10):#sets a default value of upper 10
    result= []
    a, b = 0,1
    for i in range(upper):
        result.append(a)
        a, b = b, a+b
    return result
print(fib2)
print(fib2())
print(fib2(20))

#съответстие на формални и действителни аргументи??? Ключово съответствие 

#print(a, end=' ') а - предаване позиционно(първо се подават позиционните винаги!),
#  а енд ключово предаване???
# ключов означава  име на формалния параметър = стойност 'end = " "', а позиционен е 'а' например
###Питай позиционния параметър е някой който не се седържа във функцията въобще ли?

def mySum(list=[]):
    sum = 0
    for n in list:
        sum+=n
    return sum
print(mySum([1,2,3,4,5]))
#list is one parameter, now we write a function with changing number of parameters
def mysum2(*values):# '*' - the argument number will be changing
    print(values)#values is not a list the parentases are rounded, it is tuple! 
    #tuple is immutable like str, its not mutable like a list
    print(type(values), values)
    sum = 0
    for i in values:
        sum+=i
    return sum
print(mysum2(11,22,33,44,55,66))
print('I am here')



def standard(arg1):
    print(arg1)

def positional_only(pos, /):
    print(pos)

def keyword_only(*, keyword):
    print(keyword)

def all(pos, /, combined, *, keyword):
    print(pos, combined, keyword)
    
standard(22) #positional predavane na argument
standard(arg1=11) #keyword argument

positional_only(13)
#positional_only(pos = 44)#returns an error, because we have typed that we only 
#can use a positional argument like 

keyword_only(keyword=44)
#keyword_only(55) greshka pak

all(100, 200, keyword = 300)
all(1000, combined = 2000, keyword = 3000)#example how we use only positional, 
#only keyword or combined, combined work for both






numbers =[]
for i in range(3):
    numbers.append(int(input('n=')))
print(numbers)
print(type(numbers), numbers) # input in ints

numbers = input('list: ').split()
print(type(numbers), numbers) # we see that the input is always str type so we use map

#map fuction research web3scools
numbers = list(map(int, input('list:').split()))#map returns a map object,
#so we use list () to make it a list
print(type(numbers), numbers)

numbers.sort()#най-малко към най-голямо
print(numbers)


#lambda function research!