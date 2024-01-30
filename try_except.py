# what is a pythonic way to avoid an index out of range error?

test_list = [10, 20, 30, 40, 50, 60, 70]

try:
    a = test_list[7]
    print(a)
except IndexError:
    print("List index is out of range")

# what is a pythonic way to handle TypeError ?

def add(a,b):
    try:
        return a+b
    except TypeError:
        return ("Invalid data type!")

print(add(4,5))
print(add(4,'a'))

# Write a function to compute 5/0 and use try/except to catch the exceptions.
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return ("Can not deivide by '0'")

print(division(20,5))
print(division(5,0))

# use Multiple exceptions in one except clause
def divide(a,b):
    try:
        return a/b
    except TypeError:
        return ("Invalid data type!")
    except NameError:
        return ("Invalid parameter passed!")
    except ZeroDivisionError:
        return ("Can not divide by zero!")
    except Exception as e:
        return (e)

print(divide(20,5))
print(divide(4,'a'))
print(divide(10,0))
print(divide('k','j'))

# import module if this module not found ModuleNotFoundError exceptions ?
try:
    import module1
except ModuleNotFoundError:
    print("Please check the module name, as there is no module with this name.")
else:
    print("Module imported successfully.")

#calculate the square root of a number if number is negative then use try except
import math
def square_root(number):
    try:
        if number >= 0:
            return math.sqrt(number)
        else:
            raise Exception("Negative number is not allowed!")
    except Exception as e:
        return (e)


print(square_root(25))
print(square_root(0))
print(square_root(-64))
print(square_root('ghj'))
