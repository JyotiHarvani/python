#1. List of squares of numbers from 1 to 10
l=[]
for x in range(1,11):
    l.append(x**2)
print(l)

squares=[x**2 for x in range(1,11)]
print(squares)

#2. List of all even numbers from 1 to 20
l=[]
for i in range(1,21):
    if i%2==0:
        l.append(i)
print(l)

even=[x for x in range(1,21) if x%2==0]
print(even)

#3. Converting a list of temperatures from Celsius to Fahrenheit

celcius=[0,10,20,30,40,50]
t=[]
for c in celcius:
    t.append((9/5)*c+32)
print(t)

farenheit=[(9/5)*t+32 for t in celcius]
print(farenheit)

#4. Creating a flat list out of a list of lists:

nested_list=[[1,2,3],[4,5,6],[7,8,9,10]]
flat_list=[]
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)

flat_list=[item for sublist in nested_list for item in sublist]
print(flat_list)

#1. Creating a dictionary from two lists
keys=['name','age','job']
values=['Ravi','35','Engineer']

mydict={}
for i in keys:
    for j in values:
        mydict[i]=j
print(mydict)

dict={k:v for (k,v) in zip(keys,values)}
print(dict)

#Creating a dictionary with keys as numbers and values as their squares

dict={}
for i in range(1,6):
    dict[i]=i**2
print(dict)

mydict={k:k**2 for k in range(1,6)}
print(mydict)

#3. Creating a dictionary from a string where keys are characters and values are their frequencies

str=('attachment')
dict={}
for i in str:
    dict[i]=str.count(i)
print(dict)

mydict={k:str.count(k) for k in str}
print(mydict)

#4. Creating a dictionary by filtering elements from another dictionary
dict={'a':1,'b':2,'c':3,'d':4}
dict1={}
for k in dict:
    if dict[k]>2:
        dict1[k]=dict[k]
print(dict1)

dict={'a':1,'b':2,'c':3,'d':4}
new_dict={k:v for (k,v) in dict.items() if v<=2}
print(new_dict)

#1. Create a set containing squares of numbers from 1 to 5

list=[]
for i in range(1,6):
    list.append(i**2)
set1=set(list)
print(set1)

set1={x**2 for x in range(1,6)}
print(set1)

#2. Create a set containing even squares of numbers from 1 to 10

list1=[]
for i in range(1,11):
    if (i**2)%2==0:
        list1.append(i**2)
    else:
        continue
myset = set(list1)
print(myset)

set2={i**2 for i in range(1,11) if (i**2)%2 == 0}
print(set2)

#3. Create a set containing the lengths of words in a list

list_of_words=['apple','banana','kiwi','pineapple']
myset1 = set()
for words in list_of_words:
    myset1.add(len(words))
print(myset1)

set3={len(words) for words in list_of_words}
print(set3)

#4. Create a set containing uppercase characters of a string, excluding vowels

str='Python Is A Famous High Level Programming Language'
myset=set()
for i in str:
    if i.isupper()==True and i not in 'AEIOU':
        myset.add(i)
    else:
        continue
print(myset)

set1={c for c in str if c.isupper()==True and c not in 'AEIOU'}
print(set1)






