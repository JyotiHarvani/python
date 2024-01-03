#1.	What is the output of print(2 ** 3 ** 2)
print(2 ** 3 ** 2)      #o/p=512

#2.	What is the output of the expression  print(-18 // 4)
print(-18 // 4)         #o/p=-5

#3.	What is the value of the following Python Expression print(36 / 4)
print(36 / 4)           #o/p=9.0

#4.  What is the output of print(2 * 3 ** 3 * 4)
print(2 * 3 ** 3 * 4)       #o/p=216

'''#5.  What is the output of the following assignment operator
    y = 10
    x = y += 2
    print(x)'''
'''y = 10
x = y += 2                   #SyntaxError: invalid syntax
print(x)'''

#5.	What is the output of print(2%6)
print(2%6)          #o/p=2

#6.	What is the output of print(10 - 4 * 2)
print(10 - 4 * 2)       #o/p=2

#7.	What is the output of the following code
#print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

#o/p= False True True True

'''#8.  What is the output of the following function call
def fun1(name, age=20):
    print(name, age)
fun1('Emma', 25)'''

def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25)            #o/p= Emma 25

'''9. What is the output of the add() function call
def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)'''

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)                       #o/p=(8,7)

'''#10.What is the output of the following function call
def fun1(num):
    return num + 25

fun1(5)
print(num)'''

'''def fun1(num):
    return num + 25

fun1(5)
print(num)'''          #o/p= NameError: name 'num' is not defined

'''#11. What is the output of the following display() function call
def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)'''

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)       #o/p: emp   salary

def display1(**kwargs):
    for (i,v) in kwargs.items():
        print(i,'=',v)

display1(emp="Kelly", salary=9000)      #o/p:   emp = Kelly   salary = 9000

'''#12.    What is the output of the following display_person() function call
def display_person(*args):
    for i in args:
        print(i)

display_person(name="Emma", age="25")'''

'''def display_person(*args):
    for i in args:
        print(i)
display_person(name="Emma", age="25")'''

#o/p:   TypeError: display_person() got an unexpected keyword argument 'name'

#13. correct ways to get the value of marks key.

'''student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}'''
student = {"name": "Emma","class": 9,"marks": 75}
v=student["marks"]
print(f'value of marks key is: {v}')

#14.    Select the all correct way to remove the key marks from a dictionary

student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

#method 1:
#del student["marks"]

#method 2:
#student.pop("marks")

#method 3:
#student.popitem()

print(student)

#15.    What is the output of the following dictionary operation

dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)
#print(dict1['age'])             #key error

#o/p: None

#16.    correct ways write a code how to copy a dictionary in Python

#Using for loop
d1={"name": "Amit", "salary": 10000}
d2={}
for (k,v) in d1.items():
    d2[k]=v
print("copied dictionary is: ",d2)

#Using copy function
d1={"name": "Aarush", "salary": 18000}
d2=d1.copy()
print("copied dictionary is: ",d2)

#17.    What is the output of the following

sampleDict = dict([
    ('first', 1),
    ('second', 2),
    ('third', 3)
])
print(sampleDict)

#o/p:   {'first': 1, 'second': 2, 'third': 3}

#17.    Select the correct way to access the value of a history subject

sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

history_marks = sampleDict["class"]["student"]["marks"]["history"]
print(history_marks)

#18.    Select the correct way to print Emma’s age.

student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}

print(f"Emma's age is: {student[1]['age']}")

#19.    What is the output of the following code

dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)

#o/p: True

'''#20.    using function nd also normal way
swapping first n last number in list
l =[21,4,6,2]
o/p=[2, 4, 6, 21]'''

#without function using tuple unpacking method
l=[21,4,6,2]
l[0],l[-1]=l[-1],l[0]
print(l)

#with function
l=[20,40,60,80]
def swap(list):
    list[0],list[-1]=list[-1],list[0]
    return list
swap(l)
print(l)

'''#21.    sum of all items in dict
d = {'a':350,'b':35}
o/p=sum of all items in dict: 385'''

d = {'a':350,'b':35}
list=d.values()
t=0
for n in list:
    t+=n
print(f"Sum of all values in the dict is: {t}")









