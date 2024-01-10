
#qt1) join two string inside list
"""li=["python","program"]
o/p="python program"
"""

li=["python","program"]
from functools import reduce
res=reduce((lambda x,y:x + ' ' + y),li)
print(res)


#qt2) Write a Python program to cube every number in a given list of integers using Lambda.
# i/p=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#o/p=[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes=list(map(lambda x:x**3,numbers))
print(cubes)


#qt 3) add two list using map func ?
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
add=list(map(lambda x,y:x+y,l1,l2))
print(add)


#qt 4) Write a Python program to find numbers divisible by 10 or 7 from a list of numbers using Lambda.
#l=[70,4,5,17,18,7,200,56,13,25,45,90]

l=[70,4,5,17,18,7,200,56,13,25,45,90]
x=list(filter((lambda x : (x%7==0) or (x%10==0)), l))
print(x)

"""qt 5) Write a Python program to find palindromes in a given list of strings using Lambda.
Original list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
"""
strings=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palindromes=list(filter(lambda x : x == x[::-1],strings))
print(palindromes)


"""qt 6) Write a Python program to calculate the multiplication of the positive
and negative numbers of a given list of numbers using the lambda fun
l=[4,7,-9,6,17,-24,75,89,56,-50]
"""
l=[4,7,-9,6,17,-24,75,89,56,-50]
from functools import reduce
pos=reduce((lambda x,y:x*y),(list(filter(lambda x:x>0,l))))
print("The multiplication of all the positive numbers from the list is: ",pos)

neg=reduce((lambda x,y:x*y),(list(filter(lambda x:x<0,l))))
print("The multiplication of all the negative numbers from the list is: ",neg)


"""qt 7) write a python program to find the number which is greater than 5 using lambda func ?
l=[15,5,4,3,7,8,1,2]
"""
l=[15,5,4,3,7,8,1,2]
greater=list(filter((lambda x : x>5),l))
print("The list of numbers greater than   is: ",greater)


#qt 8) Write a Python program to remove all elements from a given list present in another list using lambda.

'''list1: [10,20,30,40,50,60,70]
list2: [80,70,10,9]'''

list1=[10,20,30,40,50,60,70]
list2=[80,70,10,9]
newlist=lambda l1,l2 : set(l1) - set(l2)
print(list(newlist(list1,list2)))


"""qt 9) write a python program to calculate multiplication of numbers using tuple
tup=(10,20,30,40)
"""
tup=(10,20,30,40)
from functools import reduce
multi=reduce(lambda x,y:x*y,tup)
print("Multiplication of numbers from the tuple is: ",multi)