#1 Create a dictionary to store information about a person (name, age, address).
dict={'name':'Ravi','age':45,'address':'Rewari'}
print(dict)

'''2 Add a new key-value pair to an existing dictionary
dict = {'key1':'book','key2':'horror'}
o/p={'key1': 'book', 'key2': 'horror', '3': 'is', '4': 'add'}'''

dict = {'key1':'book','key2':'horror'}
print(f'Current dictionary is: {dict}')
dict[3]='is'
dict[4]='add'
print(f'Updated dictionary is: {dict}')

'''#3 Create a set of unique numbers from a list of numbers
dup_list = [1,2,4,3,6,2,1,6]
o/p=[1, 2, 3, 4, 6]'''

dup_list = [1,2,4,3,6,2,1,6]
print(f'List of numbers: {dup_list}')
new_set=set(dup_list)
print(f'set of unique numbers from the list is: {new_set}')

'''#4 Given two dictionaries, merge them into a single dictionary
d1 = {1:'aa',2:'bb'}
d2 = {3:'cc',4:'dd'}
o/p={1: 'aa', 2: 'bb', 3: 'cc', 4: 'dd'}'''

d1 = {1:'aa',2:'bb'}
d2 = {3:'cc',4:'dd'}
print(f"dictionary 1 is: {d1}")
print(f"dictonary 2 is: {d2}")
print("merged dictionary is: ")
d1.update(d2)
print(d1)

'''#5 Write a program that finds the most frequent element in a list
list = [2,6,7,2,9,7,7,8,8,8,8]
o/p=8'''

list = [2,6,7,2,9,7,7,8,8,8,8]
t=0
most=0
for n in list:
    if list.count(n)>t:
        t=list.count(n)
        most=n
    else:
        continue
print(f'most frequent element in the given list is: {most}')

'''#6 Implement a function that removes a key-value pair from a dictionary
dict1 = {1:"one",2:"two",3:"three",4:"four"}
o/p={1: 'one', 2: 'two', 4: 'four'}'''

dict1 = {1:"one",2:"two",3:"three",4:"four"}

#method1
print(f'Given dictionary is: {dict1}')
p=dict1.pop(3)
print(f'deleted value is: {p}')
print(f'updated dictionary is: {dict1}')

'''del dict1[3]
print(dict1)'''

'''#7 Create a program that checks if two sets have any elements in common
s1 = {1,2,3,4,9}
s2 = {2,3,5,7,8}
o/p=two sets items in common{2, 3}'''

s1 = {1,2,3,4,9}
s2 = {2,3,5,7,8}
print(f"Set of common items in s1 and s2: {s1 & s2}")

'''#8 Write a Python program that counts the number of occurrences of each character in a given string using a dict
inp_str = "gobabygo"
o/p=Occurances of each character :
 {'g': 2, 'o': 2, 'b': 2, 'a': 1, 'y': 1}'''

str='gobabygo'
dict={}
for i in str:
    dict[i]=str.count(i)
print(dict)

'''#9 Given two sets, find the union, intersection, and difference between them
A = {1,8,4,7,9}
B = {1,4,9,0,8}'''

A = {1,8,4,7,9}
B = {1,4,9,0,8}

print(f"The union of two sets is: {A | B}")
print(f"The intersection of two sets is: {A & B}")
print(f"The difference of two sets is: {A - B}")

#10 Implement a function that takes a list of strings and returns a set of unique characters present in all strings

list1=['python','is','easy']
list2=['apple','is','healthy']
list3=['abc','bcd','cde','def']
def unique(list):
    str=''.join(list)
    set1=set(str)
    print(f"The set of unique characters is: {set1}")

unique(list1)
unique(list2)
unique(list3)


























