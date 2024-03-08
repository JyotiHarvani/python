#qt51] Write a function that takes two lists and returns their  intersection (common elements)
list1=[5,10,15,20,25,30,35,40,45,50]
list2=[10,20,30,40,50]
def common(list1,list2):
    set3=set(list1) & set(list2)
    return set3

print(common(list1,list2))

#qt52] Implement a function to check if a given year is a leap year or not
def is_leap(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        print("year",year," is a leap year")
    else:
        print("year", year, " is not a leap year")

is_leap(2000)

#qt53] Create a function that takes a number as input and prints its multiplication table.
def table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
table(99)

#qt 54]  Given two sets, find the union, intersection, and  difference between them
set1={1,2,3,4,5,6,7,8,9,10}
set2={0,2,4,6,8,10,12,14}
print(f"Union of two sets is: {set1|set2}")
print(f"Intersection of two sets is: {set1&set2}")
print(f"Difference of two sets is: {set1-set2}")

#qt 55] Given a list of words, concatenate them into a single string separated by spaces
list1=['Python','is','easy']
string=' '.join(list1)
print(string)

#qt 56] ' Given a string, write a function to remove all vowels from it and return the modified string
def remove_vowel(str):
    s2=''.join(c for c in str if c not in 'aeiouAEIOU')
    return s2
s2=remove_vowel("Attachment is done")
print(s2)

#qt 57] ' Write a Python program to find the length of the longest word in a sentence

sentence="Python is a high level programming language"
list2=sentence.split()
l=max(len(word) for word in list2)
print('length of the longest word in the sentence is: ',l)

#qt 58] Create a function that takes a sentence as input and returns the sentence in reverse order
'''def rev_sent():
    sent=input("Enter a sentence:")
    list=sent.split()
    list1=list[::-1]
    return ' '.join(list1)

s=rev_sent()
print(s)'''

#qt 59]  Given a list of names, count the number of names that start with a vowel
list3=['Naman','Aman','Ishan','manas','Ishika','Amit','Kamal']
list1=[name for name in list3 if name[0] in 'aeiouAEIOU']
print(list1)

#qt 60]  Write a function to remove all duplicate characters from a given string

def unique_char(str):
    uni_set=set(str)
    uni_str = ''
    for char in str:
        if char in uni_set and char not in uni_str:
            uni_str+=char
    return uni_str
print(unique_char('programming'))
print(unique_char('aaabbbcccdddaaabbbccc'))

#qt61] Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence.
'''sentence=input("Enter a sentence: ")
word=input("Enter a word to be checked: ")
list_of_words=sentence.split()
if word in list_of_words:
    print(f"Word '{word}' is present in the sentence '{sentence}'")
else:
    print(f"Word '{word}' is NOT present in the sentence '{sentence}'")'''

#qt 62] Given a list of numbers, find the sum and average using built-in functions.
numbers=[5,10,20,30,40,50,60]
print(f"Sum of all numbers is: {sum(numbers)}")
print(f"Average of all numbers is: {sum(numbers)/len(numbers)}")

#qt 63  Create a list of fruits and add a new fruit to the list.
fruits=['banana','apple','kiwi']
fruits.append("strawberry")
print(fruits)

#qt 64] Access elements in a tuple using indexing.
tuple=(10,20,30,40,50)
i=0
while i < len(tuple):
    print(tuple[i])
    i += 1

#qt 65] Given two lists of numbers, concatenate them into a single list
numbers1=[10,20,30,40,50]
numbers2=[60,70,80,90,100]
numbers3=numbers1+numbers2
print(numbers3)

#qt66] Write a program that finds the largest and smallest elements in a list
num_list=[55.20,45,85.30,96.60,12.20,36,78]
print(f"The largest element in the list {num_list} is: {max(num_list)}")
print(f"The smallest element in the list {num_list} is: {min(num_list)}")

str_list=['Naman','aman','Ishan','manas','Ishika','Amit','Kamal']
print(f"The largest element in the list {str_list} is: {max(str_list)}")
print(f"The smallest element in the list {str_list} is: {min(str_list)}")

#qt 67] Implement a function that takes a list of numbers and returns a new list with the squared values
def squares(list):
    list1=[x*x for x in list]
    return list1

print(squares([2,4,6,8,10]))

#qt 68]Create a program that finds the common elements  between two lists and stores them in a new list
'''def common(l1,l2):
   l3=[]
   for x in l1:
       if x in l2:
           l3.append(x)
   return l3'''
#Using comprehension
def common(l1,l2):
    l3=[x for x in l1 if x in l2]
    return l3

print(common([10,20,30,15,35,40,50],[40,50,60,70,80,15]))

#qt 69] Given a list of words, find the word with the maximum length and its length
words=['Naman','Abhishek','Ishan','manasvi','Ishika','Amitabh','Kamalnath','arundhati']
lengths=[len(word) for word in words]
for word in words:
    if len(word) == max(lengths):
        print(f"{word} is with maximum length of : {len(word)}")

#qt 70] Write a Python program to count the occurrences of each element in a given list
list3=['c','v','d','D','v','c','v','g','D','d','c']
set3=set(list3)
for ele in set3:
    print(f"'{ele}'={list3.count(ele)}")

#qt 71]Given a list of names, remove all duplicate names and print the unique names

names=['Naman','aman','Ishan','manas','Ishika','Amit','Kamal','Ishan','aman']
unique_names=set(names)
names1=list(unique_names)
print("Unique names are: ",names1)

#qt 72]Create a function that takes a list of strings and returns the list sorted by the length of the strings

def sorted_list(list):
    return sorted(list,key=len)

l_sort=sorted_list(['Dashrath','Bharat','Hanuman','Ram','Laxman','Bali','Ravan','Sita'])
print(l_sort)

#qt73] Write a program that checks if a given list is sorted in ascending order

check_list1=['aman','bharti','dinesh','rahul','yaman']
check_list2=[20,10,30,40,50]
def is_sorted(list):
    l1=sorted(list)
    if l1==list:
        print(f"The list '{list}'is sorted")
    else:
        print(f"The list '{list}'is not sorted")
is_sorted(check_list1)
is_sorted(check_list2)

#Using comprehension
def is_sorted(list):
    result=all(list[i]<=list[i+1] for i in range(0,len(list)-1))
    if result:
        print(f"The list '{list}'is sorted")
    else:
        print(f"The list '{list}'is not sorted")

is_sorted(check_list1)
is_sorted(check_list2)

#qt 74] "* Implement a function that takes two lists and returns their union (all unique elements from both lists).
def union_lists(l1,l2):
    return list(set(l1) | set(l2))

l3=union_lists([2,4,6,8,10,12,14,16,18,20],[0,5,10,15,20,25,30,35,40])
print(l3)

#qt 75] Create a dictionary to store information about a person  (name, age, address)
'''dict={'name':'','age':'','address':''}
name=input("Enter your name: ")
age=input("Enter your age: ")
address=input("Enter your address: ")
dict['name']=name
dict['age']=age
dict['address']=address
print("Your information:")
print(dict)'''

#qt 76]Add a new key-value pair to an existing dictionary.

d1={'name': 'ram', 'age': '58', 'address': 'pune'}
d1['salary']=20000
print(d1)

#qt 77] Create a set of unique numbers from a list of numbers.
numbers=[2,4,6,8,10,12,14,16,18,20,4,8,12,16,20,24,28]
uni_set=set(numbers)
print(uni_set)

#qt 78]  Given two dictionaries, merge them into a single dictionary
d1={'name':'rahul','age':'15'}
d2={'class':2,'section':'A'}
d3=d1|d2
print(d3)

#qt 79] Write a program that finds the most frequent element in a list
def most(list):
    count_set={list.count(element) for element in list}
    for n in list:
        if list.count(n) == max(count_set):
            print("the most frequent element is: ",n)
            break

most([10,20,30,40,10,20,30,40,10,20,10,20,20,40,40,40,40])

#qt 80] Implement a function that removes a key-value pair from a dictionary
def remove_pair(d,k):
    d.pop(k)
    return d
dict1={'name':'rahul','age':'15','marks':75}
new_dict=remove_pair(dict1,'age')
print(new_dict)

#qt 81]Create a program that checks if two sets have any elements in common
def is_common(s1,s2):
    set_common = s1 & s2
    if len(set_common)!=0:
        print("sets have common values")
        print(set_common)
    else:
        print("sets do not have common values")


is_common({1,2,3,4,5,6,7,8}, {2,4,6,8,10,12,14})
is_common({1,2,3,4},{5,6,7,8})

#qt 82] Write a Python program that counts the number of  occurrences of each character in a given string using a dictionary
string1='abbccdddeeffff'
dict_count={}
for c in string1:
    dict_count[c]=string1.count(c)
print(dict_count)


#t 83] Given two sets, find the union, intersection and  difference between them
set1={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
set2={0,2,4,6,8,10,12,14,16,18,20}
print(f"The union of the two sets is {set1 | set2}")
print(f"The intersection of the two sets is {set1 & set2}")
print(f"The difference of the two sets is {set1 - set2}")

#qt 84] Implement a function that takes a list of strings and returns a set of unique characters present in all strings.
def unique_char(list):
    string2=''.join(list)
    set2=set(string2)
    return set2
set2=unique_char(['abcd','bcde','cdef','defg','xyz'])
print(set2)






