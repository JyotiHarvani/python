'''qt1] Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
Consider use range(#begin, #end) method'''

print("The desired numbers in the range are: ")
for n in range(2000,3201):
    if(n%7==0 and n%5!=0):
        print(n,end=',')

'''qt2]Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input'''

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

number=int(input("\nEnter a number: "))
print(f"Factorial of {number} is: ",fact(number))

'''qt3] With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number 
between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()'''

#using for loop
n=int(input("Enter a number: "))
output={}
for i in range(1,n+1):
    output[i]=i*i
print(output)

#using comprehension
out={k:k*k for k in range(1,n+1)}
print(out)

'''qt4] Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple'''

sequence=input("Enter a sequence of numbers separated by comma: ")
list2=sequence.split(',')
print(list2)
print(tuple(list2))

'''qt5] Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

lines=[]
while True:
    line=input("Enter a line or press enter to finish:")
    if not line:
        break
    lines.append(line)

list1=[line.upper() for line in lines]
for line in list1:
    print(line)

'''qt 6] Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words 
and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
'''
words=input("Enter a sequence of whitespace separated words: ")
list_words=words.split(' ')
set_words=set(list_words)
sorted_words=sorted(set_words)
for word in sorted_words:
    print(word,end=' ')

'''qt 7]  Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

for n in range(1000,3001):
    s=str(n)
    even= all(int(c)%2==0 for c in s)
    if even is True:
        print(s,end=',')

'''qt 8] Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

sentence=input("\nEnter a sentence: ")
letter=0
digit=0
for ch in sentence:
    if ch.isalpha():
        letter+=1
    elif ch.isdigit():
        digit+=1
print(F"LETTERS {letter} \nDIGITS {digit}")

'''qt 9]
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

sentence=input("\nEnter a sentence: ")
upper=0
lower=0
for ch in sentence:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
print(f"UPPER CASE {upper}\nLOWER CASE {lower}")

'''qt 10]  Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''


a=input("\nEnter a number: ")
total=int(a)+int(a+a)+int(a+a+a)+int(a+a+a+a)
print(f"Total of {a}+{a}{a}+{a}{a}{a}+{a}{a}{a}{a} is: ",total)

'''qt 11]  Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

sequence=input("\nEnter a sequence of comma-separated numbers: ")
numbers=sequence.split(',')
squares=[int(n)*int(n) for n in numbers if int(n)%2!=0]
for n in squares:
    print(n,end=',')

'''qt 12] Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

amount=0
while True:
    transaction=input("Enter a transaction or press enter to finish: ")
    if not transaction:
        break
    if transaction[0]=='D':
        amount+=int(transaction[2:])
    else:
        amount-=int(transaction[2:])
print("The net amount in the account is : ",amount)

"""
qt 13] A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
def check(str):
    pwds=str.split(',')
    valid=[]
    for pwd in pwds:
        if 6<=len(pwd)<=12:
            if any(c.islower() for c in pwd) and any(c.isupper() for c in pwd) and any(c.isdigit() for c in pwd) and any(c in ('@','#','$') for c in pwd):
                valid.append(pwd)
    return valid

pwds=input("\nEnter passwords separated by commas to check: ")
print("Valid passwords are: ",check(pwds))


'''qt 14] Question:Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
Hints:
Consider use yield'''

class divisibleby7:
    def inputdata(self):
        self.n=int(input("Enter a number: "))

    def div7_gen(self):
        for i in range(1,self.n+1):
            if i%7==0:
                yield i

a=divisibleby7()
a.inputdata()
print(f"Numbers divisible by 7 in range 1 to {a.n} are:")
gen=a.div7_gen()
for i in gen:
    print(i)

'''qt 15] Question:Write a method which can calculate square value of number
Hints:Using the ** operator'''

def square(n):
    return n**2
number=int(input("Enter a number: "))
print(f"Square of {number} is: ",square(number))

"""qt 16] Define a function which can compute the sum of two numbers.
Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value."""

def add(a,b):
    return a+b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(f"Sum of {a} and {b} is: ",add(a,b))

"""qt 17] Question:
Define a function that can convert a integer into a string and print it in console.
Hints:Use str() to convert a number to string."""
def int_to_str(n):
    string=str(n)
    return string

num=int(input("Enter a number: "))
print(f"Type of int {num} is converted to : ",type(int_to_str(num)))

'''qt 18] Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
Hints:Use int() to convert a string to integer.'''

def sum():
    numbers=input("Enter two numbers separated by comma: ")
    l=(numbers.split(','))
    return int(l[0])+int(l[1])

print(sum())

'''qt 19] Question:Define a function that can accept two strings as input and concatenate them and then print it in console.
Hints:Use + to concatenate the strings'''

def concat(s1,s2):
    print(s1+s2)

s1=input("Enter first string: ")
s2=input("Enter second string: ")
concat(s1,s2)

'''qt 20] Question:
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line.
Hints:Use len() function to get the length of a string'''
def max_len(s1,s2):
    if len(s1) > len(s2):
        print("String with max length is: ",s1)
    elif len(s2) > len(s1):
        print("String with max length is: ",s2)
    else:
        print("Both the strings have equal length:")
        print(s1)
        print(s2)

max_len('python','language')

'''qt 21] Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
Hints:Use % operator to check if a number is even or odd.'''

def even_odd(n):
    if n%2==0:
        print("It is an even number")
    else:
        print("It is an odd number")

even_odd(20)

'''qt 22] Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
Hints:Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.'''

def sq_dic_comprehension():
    dict={x:x**2 for x in range(1,4)}
    print(dict)

def sq_dic():
    dict={}
    for i in range(1,4):
        dict[i]=i**2
    print(dict)
sq_dic_comprehension()
sq_dic()

'''qt 23] Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
Hints:Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
'''
def sq_dict():
    dict={}
    for i in range(1,21):
        dict[i]=i**2
    print(dict)
sq_dict()

'''qt 24] Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
The function should just print the values only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.'''

def sq_dict():
    dict={}
    for i in range(1,21):
        dict[i]=i**2
    print("Dictionary values are:")
    for k,v in dict.items():
        print(v)
sq_dict()

'''qt 25]  Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
The function should just print the keys only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.'''
def sq_dict():
    dict={}
    for i in range(1,21):
        dict[i]=i**2
    print("Dictionary keys are:")
    for k in dict:
        print(k)
sq_dict()

'''qt 26] Question:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.'''
def squares():
    list_sq=[]
    for i in range(1,21):
        list_sq.append(i**2)
    print("The list of squares is:")
    print(list_sq)
squares()

'''qt 27] Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the first 5 elements in the list.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list'''
def squares():
    list_sq=[]
    for i in range(1,21):
        list_sq.append(i**2)
    print("The first five elements of the list are:")
    print(list_sq[0:5])
squares()

'''qt 28] Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list'''

def squares():
    list_sq=[]
    for i in range(1,21):
        list_sq.append(i**2)
    print("All the values of the list except first 5 elements are:")
    print(list_sq[5:])
squares()

'''qt 29] Question:
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.'''

def squares_tuple():
    list_sq=[]
    for i in range(1,21):
        list_sq.append(i**2)
        sqt=tuple(list_sq)
    print("The tuple of squares from 1 to 20 is:")
    print(sqt)
squares_tuple()

'''qt 30] Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
Hints:
Use [n1:n2] notation to get a slice from a tuple.'''

t=(1,2,3,4,5,6,7,8,9,10)
print("First half of the tuple is: ",t[0:5])
print("Second half of the tuple is: ",t[5:])

'''qt 31] Question:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
Hints:Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.'''

t=(1,2,3,4,5,6,7,8,9,10)
l=[]
for i in t:
    if i%2==0:
        l.append(i)
t_new=tuple(l)
print("New tuple with only even numbers is: ",t_new)

'''qt 32] Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
Hints:Use if statement to judge condition.'''

string=input("Enter a string(yes/Yes): ")
if string in ('yes','YES','Yes'):
    print("Yes")
else:
    print("No")

'''qt 33] Question:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
Hints:Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.'''

list1=[1,2,3,4,5,6,7,8,9,10]

even=filter(lambda x:x%2==0,list1)
print(list(even))

'''qt 34] Question:Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
Hints:Use map() to generate a list.
Use lambda to define anonymous functions.'''

list1=[1,2,3,4,5,6,7,8,9,10]
squares=map(lambda x:x**2,list1)
print(list(squares))

'''qt 35] Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
Hints:Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.'''

list1=[1,2,3,4,5,6,7,8,9,10]
even_squares= map(lambda x:x**2,filter(lambda x:x%2==0,list1))
print(list(even_squares))


'''qt 36] Question:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
Hints:
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.'''

even=list(filter(lambda x:x%2==0,range(1,21)))
print(even)


'''qt 37]
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
Hints:Use map() to generate a list.
Use lambda to define anonymous functions.'''

squares=map(lambda x : x**2,range(1,21))
print(list(squares))
