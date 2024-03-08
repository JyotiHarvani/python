#Q 1]  Write a Python program to print "Hello, World!"
print("Hello, World!")

#Q 2]  Calculate the sum of two numbers entered by the user.
'''a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=a+b
print("The sum of two numbers is: ",c)'''

#Q 3]  Convert temperature from Celsius to Fahrenheit.
'''c=float(input("Enter temperature in celcius: "))
f=(9/5)*c+32
print("Tempetrature in farenhite is: ",f)'''

#Q 4]  Write a Python program to calculate the area of a rectangle given its length and width
l,w=10,12
print("Area of the rectangle is: ",l*w)

#Q5] Create a program that takes a user's name and age as  input and prints a greeting message
'''name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("Hello",name,", Have a good day!")'''

# Q6]Write a program to check if a number is even or odd
n=20
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")

#Q7] Given a list of numbers, find the maximum and minimum values+
list=[25,20,63,75,22,30,89,120,56,6]
print("The maximum number in the list is: ",max(list))
print("The minimum number in the list is: ",min(list))

# q8] Create a Python function to check if a given string is a palindrome
#Method1: Using for loop
str1=input("Enter a string to be checked: ")

def is_palindrome(str):
    flag=1
    for i in  range(0,len(str)//2):
        if str1[i]==str1[-(i+1)]:
            continue
        else:
            flag=0
            break
    if flag==1:
        print("Given string is palindrome.")
    else:
        print("Given string is not palindrome.")
is_palindrome(str1)

'''#Using Indexing
str1=input("Enter a string to be checked: ")
if str1==str1[::-1]:
    print("Given string is palindrome.")
else:
    print("Given string is not palindrome.")'''

# q9) Calculate the compound interest for a given principal amount, interest rate, and time period
'''p=10000
r=10
t=3
ci=p*(1+r/100)**t-p
print("The compound interest is: ",ci)'''

# q10) Write a program that converts a given number of days  into years, weeks, and days
def year(days):
    y=days//365
    w=(days%365)//7
    d=(days%365)%7
    print("days are: ",days)
    print(f"{y} years {w} weeks {d} days")

year(401)
year(750)
year(1200)

#q11) Given a list of integers, find the sum of all positive numbers

list=[2,5,-5,-8,6,-4,1,-6,6]
t=0
for i in list:
    if i>0:
        t+=i
print("The sum of all positive numbers in the list is: ",t)

#q12) Create a program that takes a sentence as input and counts the number of words in it
'''sentence=input("Enter a sentence: ")
#Using list
list1=sentence.split(" ")
print("Number of words in the sentence are: ",len(list1))'''

#q13]Implement a program that swaps the values of two variables.
a=10
b=20
print("Before swapping: a=",a,"b=",b)
a,b=b,a
print("After swapping: a=",a,"b=",b)

#q14] Create variables for storing a person's name, age, and  average test score.
name="Tarinika"
age=15
avg_test_score=75

print(f"name= {name} age={age} average test score={avg_test_score}")

#q15] Concatenate two strings and print the result.
str1="abcd"
str2="efgh"
str3=str1+str2
print(str3)

#q16] Create a list of fruits and access elements using  indexing
fruits=['Apple','Banana','Kiwi','Grapes','strawberry']
for i in range(0,len(fruits)):
    print(f"fruits[{i}]={fruits[i]}")

#q17] Given a list of numbers, find the sum and average
list=[10,20,30,40,50,60]
print("The numbers are: ",list)
print("The sum of numbers is: ",sum(list))
print("The average of numbers is: ",sum(list)/len(list))

#q18]  Create a program that takes a temperature in Celsius and  converts it to Kelvin

'''c=float(input("Enter temp in celcius: "))
print(f"Temperature in Kelvin is: ",c+273.15)'''

#q19    s="AABBB"          o/p={'A':2,'B':3}
s="AABBB"
dict={k:s.count(k) for k in s}
print(dict)

#q20]Create a function to reverse a given string
def reverse(str):
    return str[::-1]

print(reverse("rupali"))
print(reverse("varun"))

#q21]Given a list of names, concatenate them into a single string separated by spaces
list=['Python','is','easy']
str1=' '.join(list)
print(str1)

#q22] Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)
str1='abcdefghijklmnopqrstuvwxy'
str2='my girl wove six dozen plaid jackets before she quit'
str3='The quick brown fox jumps over a lazy dog'
str4='vjbchbkgytdfijlh'
def is_pangram(str):
    str1=str.replace(" ","")       #string is immutable.changes will not reflect in origional string, that's why created new string
    #print(str1)
    set1=set(str1)
    #print(set1)
    if len(set1)==26 and all(letter.isalpha() for letter in set1):
        print(f"'{str}' is a pangram")
    else:
        print(f" '{str}' is not a pangram")

is_pangram(str1)
is_pangram(str2)
is_pangram(str3)
is_pangram(str4)

#q23]Calculate the area and circumference of a circle given its radius

r=10
area=3.14*r*r
circum=2*3.14*r
print("Area of a circle with radius ",r,"is: ",area)
print("Circumference of a circle with radius ",r,"is: ",circum)

#q24] Implement a program that converts a given number of minutes into hours and minutes
def hour_minutes(minutes):
    h=minutes//60
    m=minutes%60
    print(f"{minutes} minutes= {h} hours and {m} minutes")

hour_minutes(123)
hour_minutes(186)
hour_minutes(458)

#q25]Create a function to count the number of vowels in a given string
def vowels(str):
    count=0
    for c in str:
        if c in 'aeiou' or c in 'AEIOU':
            count+=1
    print(f"Number of vowels in '{str}' is: {count}")

vowels("Abcdefghi")
vowels("I am learning python")

#q26] Write a program to check if a number is prime.
#A prime number is defined as a natural number greater than 1 and is divisible by only 1 and itself(exactly two factors)
def check_prime(n):
    if n<2:
        print(n, " is not a Prime number")
        return
    flag=0
    for i in range(2,n//2+1):
        if n%i==0:
            flag=1
            break
    if flag==1:
        print(n, " is not a Prime number")
    else:
        print(n,"is a Prime number")
check_prime(1)
check_prime(-25)
check_prime(31)
check_prime(231)

#q27]  Write a program that checks if a given number is  positive, negative, or zero.
def check_num(n):
    if n==0:
        print(f"Number {n} is zero")
    elif n<0:
        print(f"Number {n} is negative")
    else:
        print(f"Number {n } is positive")

check_num(12)
check_num(-12)
check_num(0)
check_num(1)

#q28] Create a loop that prints the first 10 even numbers.
t=0
i=0
while t!=10:
    if i%2==0:
        print(i)
        t+=1
    i+=1

#q29] Implement a program that finds the largest number  in a list.
def max_list(list):
    print(f"Largest number in the list {list} is : {max(list)}")
max_list([10,20,52,63,12,22,5])

#qt30]Create a program that takes a year as input and checks if  it is a leap year or not)
'''year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):        #First condition checking for non-century years
    print("You entered a leap year")                    #and second condition checking for century years
else:
    print("You have not entered a leap year")'''

#qt31] Given a list of integers, find all the even numbers and store them in a new list
list=[10,13,45,26,58,59,75,76]
even_list=[n for n in list if n%2==0]
print(even_list)

#qt32] a="python is very easy programming language"
    #o/p="language programming easy very is python"
a="python is very easy programming language"
list1=a.split()
rev_list=list1[::-1]
rev_a=' '.join(rev_list)
print(rev_a)

#qt33] Create a program that generates the Fibonacci sequence upto a given numbner of terms (0,1,1,2,3,5,8,13,21,...)
t1=0
t2=1
n=10
print(f"{n} terms of fibonacci series are: ")
print(t1)
print(t2)
for i in range(0,n-2):
    t3=t1+t2
    print(t3)
    t1=t2
    t2=t3

#qt34] Given a list of names, print all names starting with the letter 'A')

names=['Amit','Vijay','Ajay','Aakash','Sagar','kailash']
names_A=[name for name in names if name[0]=='A']
print(names_A)

#qt35] Implement a program that prints the multiplication table of a given number

def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
table(5)

#qt36] Write a program that calculates the factorial of a given number
def fact(n):
    i=n
    f=1
    while i>=1:
        f=f*i
        i-=1
    print(f"Factorial of {n} is: {f}")
fact(5)

#qt37]  Create a loop that prints all prime numbers between 1 and 50
list=[]
for n in range(2,51):
    for j in range(2,n//2+1):
        if n%j==0:
            break
    else:
        list.append(n)
print("Prime numbers between 1 and 50 are: ",list)

#qt38] Given a list of words, count the number of words with more than five characters
words=['naman','kailash','aarush','amit','kavyanshi','divisha','prayan','ana','hansika','lavina','harsha']
count=0
for word in words:
    if len(word)>5:
        count+=1
print("number of words with more than five characters: ",count)

#qt 39] Calculate the sum of digits of a given number.
#using for loop
def sumd(n):
    s=str(n)
    t=0
    for digit in s:
        t+=int(digit)
    print(f"The sum of digits of number {n} is: {t}")
sumd(123)
sumd(456)

#using comprehension
n1=245
s1=str(n1)
sumd2=sum(int(digit) for digit in s1)
print(sumd2)

'''#qt40]qt 97] i/p
            a="hello" 
           b="world"
      o/p=Hello World'''

a="hello"
b="world"
c=a+' '+b
d=c.capitalize()        #str.title() method can also be used
print(d)

'''#qt41]qt 96]  Python program to print all possible substrings of a given string
s = "abcd"
o/p=
a
ab
abc
abcd
b
bc
bcd
c
cd
d'''
s="abcd"
l=len(s)
for i in range(0,l+1):
    for j in range(i,l+1):
        print(s[i:j])

#qt42] Implement a function that reverses a given string.
def rev(s):
    print(s[::-1])
rev("maharashtra")

#qt43] Given a list of numbers, create a function to find the sum of all positive numbers

def sum_pos(list):
    s=sum(num for num in list if num>0)
    print("Sum of all positive numbers is: ",s)

sum_pos([10,2,-5,2,-15,3,-7,1,-58])

#qt 44] input="python"        o/p="nothyp"

s2="python"
output=s2[::-1]
print(output)


#qt 45] Write a Python function to check if a given string is a palindrome

def is_palindrome(s):
    s1=s[::-1]
    if s==s1:
        print(f"'{s}' is palindrome")
    else:
        print(f"'{s}' is not palindrome")
is_palindrome("abbcbba")
is_palindrome("abbcba")

#qt46] qt 94]  Implement a function that takes a list of strings and returns a set of unique characters present in all strings.
def unique(list):
    str4=''.join(list)
    set4=set(str4)
    return set4
s=unique(["abcd","bcdef","fgh","xyz"])
print(s)

#qt 47] Create a function to find the square of each element in a given list
def squares(list):
    l=[x*x for x in list]
    return l

l1=squares([2,4,6,8])
print(l1)

#qt 48] Write a function to check if a number is even or odd and  return "Even" or "Odd" accordingly"

def even_odd(n):
    if n%2==0:
        return 'Even'
    else:
        return 'Odd'

print(even_odd(20))
print(even_odd(23))

#qt 49]  Calculate the area of a triangle given its base and height  using a function

def area_tri(b,h):
    return (1/2*b*h)

area=area_tri(10,5)
print(area)

#qt 50] Create a function that takes a list of strings and returns the list sorted alphabetically

l=['rajni','aniket','kamya','ankita','Vicky','Anuj','kapil','shikha']

#ascending order
def sorted(list):
    list.sort()
    return list
print("list in ascending order: ",sorted(l))

#descending order
def sorted_r(list):
    list.sort(reverse=True)
    return list
print("list in descending order: ",sorted_r(l))
