#Q1.Print Hello 5 Times Using Decorator.
def decorator(fun):
    def mf_hello():
        for x in range(5):
            fun()
    return mf_hello


@decorator
def hello():
    print("Hello")


hello()
print("Done 5 times")


#Q2.Print Hello 30 Times Using Decorator.
def decorator(fun):
    def mfx():
        for x in range(30):
            fun()
    return mfx

@decorator
def hello1():
    print("Hello")


hello1()

#Q3.print 30 times =============Hello===========
def decorator3(fun):
    def mfx():
        for x in range(30):
            print("=========="+fun()+"============")
    return mfx

@decorator3
def hello3():
    return "Hello"

hello3()



#qt4.using decorators for divided two number if denominator is 0 then print messge "can not divide by zero"

def decorator4(func):
    def mfx(a,b):
        if b==0:
            print("can not divide by zero")
        else:
            func(a,b)
    return mfx

@decorator4
def divide(num,den):
    print(num/den)

divide(10,2)
divide(5,0)


#qt5: using Chaining Decorators print hello messsage but before hello message 15 * nd 15 % symbol
#     nd after hello also 15 * nd 15 % symbol
# output
"""***************
 %%%%%%%%%%%%%%%
 Hello
 %%%%%%%%%%%%%%%
 ***************
 """
def decorator1(fun):
    def mfx():
        print(15*'*')
        fun()
        print(15*'*')
    return mfx

def decorator2(fun):
    def mfx():
        print(15*'%')
        fun()
        print(15*'%')
    return mfx

@decorator1
@decorator2
def hello():
    print("Hello")

hello()


""" qt 6 using decorators subtraction  of two number Suppose, 
    if the user passes the arguments as 5 followed by 10,
     we will end up with a negative value which is not the required output"""

def decorator5(sub):
    def mf_sub(a,b):
        if a<b:
            print("Result is negative which is not the required output ")
        else:
            sub(a,b)
    return mf_sub


@decorator5
def sub(a,b):
    print(f"The difference is: {a-b}")

sub(20,10)
