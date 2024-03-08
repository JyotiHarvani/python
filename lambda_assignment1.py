#qt 1] count the odd numbers in given list using lambda expression
#list1 = [10, 21, 4, 45, 66, 93, 11]

list1 = [10, 21, 4, 45, 66, 93, 11]
odd_numbers = list(filter(lambda x : x %2!=0,list1))
count = len(odd_numbers)
print(f"There are {count} odd numbers in the list")

#qt 2]  Python program to print odd Numbers in a List Using List Comprehension
#list1 = [10, 21, 4, 45, 66, 93, 11]

list1 = [10, 21, 4, 45, 66, 93, 11]
odd_numbers = [x for x in list1 if x%2 != 0]
print(f"Odd numbers in the list are {odd_numbers}")

#qt 3] string1 = "Hello World" split this string1 using lambda function

string1 = "Hello World"
list1 = (lambda x : x.split())(string1)
print(f"Splitted string is: {list1}")

#qt 4] my_dict = {'a': 1, 'b': 2, 'c': 3}  add the values of a dictionary using lambda function

from functools import reduce
my_dict = {'a': 1, 'b': 2, 'c': 3}
sum = reduce(lambda x,y : x+y, my_dict.values())
print(f"The sum of all the values of my_dict is: {sum}")

#qt 5] list1 = [1, 2, 3, 4]
#list2 = [5, 6, 7, 8]
#add this two list using lambda function
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

list3 = list(map(lambda x,y: x+y, list1, list2))
print(f"The addition of list1 and list2 is: {list3}")

#qt 6] calculate the total multiplication of all elements in a list use lambda function
#my_list = [1, 2, 3, 4, 5]

my_list = [1, 2, 3, 4, 5]
product = reduce(lambda x,y : x*y, my_list)
print(f"The product of all the numbers in the list is: {product}")

#qt 7] calculate the total addition of all elements in a list use lambda function
#my_list = [1, 2, 3, 4, 5]

my_list = [1, 2, 3, 4, 5]
total = reduce(lambda x,y : x+y, my_list)
print(f"The total of all the numbers in the list is: {total}")

#qt 8] my_string = "Hello   World" remove space inside a string using a lambda function o/p = = HelloWorld

my_string = "Hello   World"
new_string = (lambda x : x.replace(' ',''))(my_string)
print(f"The string after removing whitespaces is : {new_string}")