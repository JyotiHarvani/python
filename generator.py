#qt] use decorators print message Good Morning!,Good Afternoon!,Good Evening!,Good Night! using datetime module
from datetime import datetime

def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        current_hour = datetime.now().hour
        greeting_message = ""

        if 5 <= current_hour < 12:
            greeting_message = "Good Morning!"
        elif 12 <= current_hour < 17:
            greeting_message = "Good Afternoon!"
        elif 17 <= current_hour < 22:
            greeting_message = "Good Evening!"
        else:
            greeting_message = "Good Night!"

        msg = kwargs.get('msg', '')
        print(f"{greeting_message} {kwargs['name']}: {msg}")
        return func(*args, **kwargs)

    return wrapper

@greeting_decorator
def greet(name, msg):
    print("Greetings of the day!")

greet(name='Ravi Gupta', msg='Have a good day!')




#qt] perform,add,sub,mul,div using decorators if user use string the show message Arguments must be numbers (int or float)

def decor_input(func):
    def wrapper(x, y):
        if type(x) not in (int, float) or type(y) not in (int, float):
            return "Arguments must be numbers (int or float)"
        return func(x, y)

    return wrapper


@decor_input
def add(a, b):
    return a+b

@decor_input
def sub(a, b):
    return a-b

@decor_input
def mul(a, b):
    return a*b

@decor_input
def div(a, b):
    if b!=0:
     return a/b
    else:
        return "Can not be divided by Zero"

print(add(10,20))
print(sub(20,10))
print(mul(5,10))
print(div(5,2))
print(add('c','d'))
print(mul(5,'v'))
print(div(15,0))
print(div(45,'a'))


#qt] get a simple vowel use generator
def gen_vowel():
    for v in 'aeiou':
        yield v

print("Vowels are: ")
x=gen_vowel()
print(next(x))
print(next(x))
print(next(x))
for i in x:
    print(i)

#qt] n=1 output 1 2 3 use generators
def generate_numbers(n):
    for i in range(n,n+3):
        yield i

x=generate_numbers(1)
print(next(x))
print(next(x))
print(next(x))

#qt] str=hello output=olleh use generators

def gen_rev_str(str):
    for c in str[::-1]:
        yield c

rev=gen_rev_str('hello')
for c in rev:
    print(c,end='')

print('\n')


#qt] print 1 to 50 numbers use generators
def gen_num(n):
    for n in range(1,n+1):
        yield n

x=gen_num(50)
for n in x:
    print(n)

#qt] print odd even number use generators
def gen_even_odd(n,str):
    if str=='even':
        for n in range(0,n+1):
            if n%2==0:
                yield n
    else:
        for n in range(0,n+1):
            if n%2!=0:
                yield n

even=gen_even_odd(50,'even')
odd=gen_even_odd(50,'odd')
print("Even numbers are: ")
for e in even:
    print(e,end=' ')
print("\nOdd numbers are: ")
for o in odd:
    print(o,end=' ')
