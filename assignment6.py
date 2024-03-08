#1. Reversing a String using an Extended Slicing Technique
def rev_string(str):
    return str[::-1]


string = input("Enter a string: ")
print("Reverse string is: ",rev_string(string))

#2. Counting Vowels in a Given Word
def vowels_in_word(word):
    count = 0
    for ch in word:
        if ch in 'aeiouAEIOU':
            count+=1
    return count


word = input("Enter a word: ")
print(f"Number of vowels in {word} is:",vowels_in_word(word))

#3. Counting Consonants in a Given Word
def consonants_in_word(word):
    count = 0
    for ch in word:
        if ch.isalpha() and ch not in 'aeiouAEIOU':
            count += 1
    return count


word = input("Enter a word: ")
print(f"Number of Consonants in {word} is: ",consonants_in_word(word))

#4. Counting the Number of Occurances of a Character in a String
def char_count(string,char):
    return string.count(char)


string = input("Enter a string: ")
char = input("Enter a character from the string: ")
print(f"The number of occurance of '{char}' in '{string}' is: ",char_count(string,char))

#5. Writing Fibonacci Series
def fibonacci(n):
    print(f"Fibonacci series upto {n} terms is:")
    t1,t2 = 0,1
    print(t1)
    print(t2)
    for i in range(0,n-2):
        t1,t2 = t2,t1+t2
        print(t2)
        i += 1


number = int(input("Enter number of terms: "))
fibonacci(number)


#6. Finding the Maximum Number in a List

numbers = [25,45,20,56,52,41,32]
print("Maximum number in the list is: ",max(numbers))

#7. Finding the Minimum Number in a List
numbers = [25,45,20,56,52,41,32]
print("Minimum number in the list is: ",min(numbers))

#8. Finding the Middle Element in a List

def middle_element(list):
    if len(list) % 2 == 0:
        mid = (len(list) - 1) // 2
        print(f"There are two middle elements in the list {list}: {list[mid]} and {list[mid+1]}")
    else:
        mid = len(list) // 2
        print(f"The middle element is the list {list} is: {list[mid]}")


list1 = ['first','second','third','fourth','fifth','sixth','seventh']
middle_element(list1)
list2 = ['first','second','third','fourth','fifth','sixth','seventh','eighth']
middle_element(list2)

#9. Converting a List into a String

list3 = ['Python' , 'is' , 'easy']
string = ' '.join(list3)
print("Converted string is: ",string)

#10. Adding Two List Elements Together
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
add = map(lambda x,y : x+y,list1,list2)
list3 = list(add)
print("Final list after addition is: ",list3)

#11. Comparing Two Strings for Anagrams

def is_anagram(s1,s2):
    if set(s1) == set(s2):
        return f"Strings '{s1}' and '{s2}' are anagrams of each other"
    else:
        return f"Strings '{s1}' and '{s2}' are not anagrams of each other"

print(is_anagram('meera','reema'))
print(is_anagram('ram','rama'))
print(is_anagram('ram','ramayan'))

#12. Checking for Palindrome Using Extended Slicing Technique
def is_palindrome(string):
    if string == string[::-1]:
        return f"{string} is a palindrome"
    else:
        return f"{string} is not a palindrome"

print(is_palindrome('123454321'))
print(is_palindrome('python'))

'''13. Counting the White Spaces in a String
     ex    string = "P r ogramm in g "
'''
def count_whitespace(string):
    count = 0
    for ch in string:
        if ch == ' ':
            count += 1
    return count

string = "P r ogramm in g "
print(f"Number of whitespaces in string '{string}' are: ",count_whitespace(string))

'''#14. Counting Digits, Letters, and Spaces in a String
 ex     name = 'Python is 1'
 '''
def count_DLS(string):
    digit,letter,space=0,0,0
    for ch in string:
        if ch.isdigit():
            digit += 1
        elif ch.isalpha():
            letter += 1
        elif ch == ' ':
            space += 1
    print(f"In given string {string} there are:")
    print(f"Digits: {digit} \nLetters: {letter} \nSpaces: {space}")

string="My age is 35"
count_DLS(string)

'''#15. Counting Special Characters in a String
  ex    spChar = "!@#$%^&*()"'''

def count_special_char(string):
    count = 0
    for ch in string:
        if ch in '!@#$%^&*()':
            count += 1
    return count

string = "Password for my email id - jyoti@gmail.com is Jyoti@#$(123)"
print(f"Number of special characters in the string '{string}' is: ",count_special_char(string))

'''16. Removing All Whitespace in a String
ex  string = "C O D E"'''

string = "C O D E"
list_temp = string.split(' ')
string_new = ''.join(list_temp)
print(f"String after removing whitespaces is: {string_new}")

#17. Building a Pyramid in Python

def pyramid(n):
    for i in range(1,n+1):
        print(' '*(n-i),'* '*i)

pyramid(5)
pyramid(10)

#18]  Creating a String with triple Quotes

string='''I love python'''
print(string)

#19]. Converting a List into a Tuple
list4 = [10,20,30,40,50]
tuple4 = tuple(list4)
print("After conversion the type is: ",type(tuple4))

#20]. Converting a List into a Set
list4 = [10,20,30,40,50]
set4 = set(list4)
print("After conversion the type is: ",type(set4))

#21] Removing the elements from a dictionary.
dict = {1:'ram',2:'shyam',3:'radha',4:'bharat'}
dict.pop(3)
print("Dictionary after deletion of one element is: ",dict)


#22] Iterating Through a Dictionary
student = {1:'ravi',2:'raj',3:'radha',4:'ravina'}
print("The student record is: ")
for k,v in student.items():
    print(f"{k} : {v}")

#23] Reverse a string.
'''If the input is : Hello World!
The output should be: !dlroW olleH'''
def reverse(string):
    return string[::-1]

print(reverse("Hello World!"))

#24] Reverse a number

def rev_num(number):
    string = str(number)
    return int(string[::-1])

print(rev_num(4567))

#25]  remove all duplicate characters from  string.
def remove_dup(string):
    set_temp = set(string)
    new_str = ''
    for ch in string:
        if ch in set_temp and ch not in new_str:
            new_str = new_str + ch
    return new_str

print(remove_dup("programming"))

#26] find the second largest number in the list.

def second_largest(list):
    desc_list = sorted(list , reverse = True)
    return desc_list[1]

list_num = [15,12,18,13,17]
list_words = ['what','when','where','why','how']

print(f"Second largest in the {list_num} is: ",second_largest(list_num))
print(f"Second largest in the {list_words} is: ",second_largest(list_words))

#27]write python program to find the area of circle using class

class Circle:
    def __init__(self,radius):
        self.r = radius

    def area(self):
        return 3.14 * self.r *self.r

circle1 = Circle(15)
print(f"The area of a circle with radius {circle1.r} is: ",circle1.area())

#28]Write a program to create a class by name Persons and initialize attributes like name, Age, and Address while creating an object.

class Persons:
    def __init__(self,name,age,address):
        self.n = name
        self.a = age
        self.ad = address

    def show(self):
        print("Name: ",self.n)
        print("Age: ",self.a)
        print("Address: ",self.ad)

person1 = Persons('Amit','35','Pune')
person1.show()


#29]Write a program to create a class by name cars and initialize attributes like name while creating an object. display this names

class Cars:
    def __init__(self,name,model):
        self.n = name
        self.m = model

    def display(self):
        print("Name: ",self.n,end = '\t')
        print("Model: ",self.m)

car1 = Cars('KIA', 'Carans')
car1.display()
car2 = Cars('Maruti','Suzuki')
car2.display()
car3 = Cars('Honda','Amaze')
car3.display()


#30] create class with static variable,instance var,local var

class Student:
    univ = ''                           #Initialize univ as a static variable
    def __init__(self,name,roll_no):    #name and roll_no are local variables
        self.n = name                   #self.n self.r are instance variables
        self.r = roll_no
        Student.univ = 'RTU'

    def display(self):
        print("Name: ",self.n)
        print("Roll no.: ",self.r)
        print("University: ",Student.univ)

student1 = Student('Rahul',15)
student1.display()


#31] create class with static method

class Student:
    univ = ''                           #Initialize univ as a static variable
    def __init__(self,name,roll_no):    #name and roll_no are local variables
        self.n = name                   #self.n self.r are instance variables
        self.r = roll_no
        Student.univ = 'Rajasthan University'

    def display(self):
        print("Name: ",self.n)
        print("Roll no.: ",self.r)
        print("University: ",Student.univ)

    @staticmethod                           #static method
    def modify():
        Student.univ = 'Rajasthan Technical University'
        print("New University is: ",Student.univ)

student1 = Student('Ajay Kumar',20)
student1.display()
Student.modify()


#32] create class by name of class and perform all arithmetic operations

class Operations:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"{self.a} + {self.b} = ",self.a + self.b)
    def subtract(self):
        print(f"{self.a} - {self.b} = ",self.a - self.b)
    def multiplication(self):
        print(f"{self.a} * {self.b} = ",self.a * self.b)
    def division(self):
        if self.b == 0:
            print("can not divide by 0")
        else:
            print(f"{self.a} / {self.b} = ",self.a/self.b)

op1 = Operations(20,10)
op1.add()
op1.subtract()
op1.multiplication()
op1.division()