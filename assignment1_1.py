#Q.1  To display the sum of first n numbers

'''n=int(input("Enter a number: "))
i=1
t=0
for i in range(n+1):
    t+=i
print(f"The sum of first {n} numbers is: {t}")'''

# Q.2 To print numbers from 1 to 10 by using while loop

'''i=1
while i<=10:
    print(i)
    i+=1
'''

#Q.3 To print sum of numbers presenst inside list

'''list=[10,20,30,40,50]
t=0
for item in list:
    t=t+item
print(f"The sum of all the items of list is: {t}")'''

#Q.4 To display numbers from 10 to 1 in descending order

'''i=10
while i>=1:
    print(i)
    i-=1'''

#Q.5 To display odd numbers from 0 to 100

'''for i in range(101):
    if (i%2)!=0:
        print(i)
    else:
        continue
'''
#Q.6 To print characters present in string index wise

'''for item in "programming":
    print(item)'''
#Another way to do this

'''str=input("Enter a string: ")
i=0
for i in range(len(str)):
    print(f"str[{i}] = {str[i]}")'''

#Q.7 Write a program to find smallest of given 2 numbers?

'''a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a<b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{b} is smaller than {a}")'''

#Q.8 Write a program to find smallest of given 3 numbers?

'''a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a<b and a<c:
    print(f"{a} is the smallest number")
elif b<a and b<c:
    print(f"{b} is the smallest number")
else:
    print(f"{c} is the smallest number")'''

#Q.9 Write a program to check whether the given number is even or odd?

'''n=int(input("Enter a number to be checked: "))
if n%2==0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")'''

#Q.10 Write a program to check whether the given number is in between 1 and 100?

'''n=int(input("Enter a number to be checked: "))
if n>1 and n<=100:
    print(f"{n} is in between 1 and 100")
else:
    print(f"{n} is not in between 1 and 100")'''

#Q.11 Write a program to find biggest of given 3 numbers

'''a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a>b and a>c:
    print(f"{a} is the greatest number")
elif b>a and b>c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")'''

#Q.12 Write a program to find biggest of given 2 numbers

'''a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")'''

#Q.13 Write a program to display *'s in pyramid style(also known as equivalent triangle

'''n=int(input("Enter number of rows in the pyramid: "))
i,j=1,n
while i<=n and j>=1:
    print(' '*j + '* '*i)
    i+=1
    j-=1'''

#Q.14 Write a program to access each character of string in forward and backward direction ?

'''str='Python is easy'
print(str[::1])         #forward direction
print(str[::-1])    '''  #backward direction

#Q.15 Program to display all positions of substring in a given main string ?

'''str='Python is a programming language'
print(f"Position of substring 'Python' in str is: {str.find('Python')}")
print(f"Position of substring 'is' in str is: {str.find('is')}")
print(f"Position of substring 'a' in str is: {str.find('a')}")
print(f"Position of substring 'programming' in str is: {str.find('programming')}")
print(f"Position of substring 'language' in str is: {str.find('language')}")'''

'''str=input("Enter a string: ")
list_new=str.split(' ')
print(list_new)
i=0
while i<len(list_new):
    print(f"Position of substring '{list_new[i]}' in the given main string is: {str.find(list_new[i])}")
    i+=1'''

#Q.16 Replacing a string with another string ?

'''str="C is a high level programming language"
print(str)
print(str.replace("C","Python"))'''

#Q.17 input: Learning Python is very Easy     output: Easy Very is Python Learning

'''str='Learning Python is very Easy'
list=str.split(' ')
list2=list[::-1]
str1=' '.join(list2)
print(str1)'''

















