#Q.18  input: B4A1D3      Output: ABD134

'''str='B4A1D3'
t=''
lst=list(str)
#print(lst)
lst.sort()
#print(lst)
print(f"input string: {str}")
print(f"Output string: ",end='')
for i in lst:
    if i.isalpha():
        print(i,end='')
    elif i.isnumeric():
        t+=i
print(t)'''

#Q.19 input: a4b3c2       output: aaaabbbcc

'''str='a4b3c2'
print("Input string is: " + str)
print("Output string is: ",end='')
i,j=0,1
while i<len(str) and j<=len(str):
    str1=str[i]*int(str[j])
    print(str1,end='')
    j+=2
    i+=2'''

'''Q.20  Write a program to remove duplicate characters from the given input string  input: ABCDABBCDABBBCCCDDEEEF
output: ABCDEF ?'''

'''str='ABCDABBCDABBBCCCDDEEEF'
print("Input string is: " + str)
print("Output sting with unique characters is: ",end='')
set1=set(str)
str_new=''.join(set1)
print(str_new)'''


'''Q.21  Write a program to find the number of occurrences of each character present in the given String
  input: ABCABCABBCDE
 output: A-3,B-4,C-3,D-1,E-1'''
'''str='ABCABCABBCDE'
set1=set(str)
for i in set1:
    count=0
    for j in str:
        if i==j:
            count+=1
    print(f"{i} - {count}")'''


#Q.22 i/p="Learning Python is very very easy !!!"  o/p= ['Learning', 'Python', 'is', 'very', 'very', 'easy', '!!!']

'''str="Learning Python is very very easy !!!"
print("Input string: " + str)
lst=str.split(' ')
print("output list: " )
print(lst)'''


'''Q.23  n=[1,2,3,4,5,6,7,8,9,10] 
        o/p =[3, 5, 7] 
       o/p=[5, 7, 9] 
      o/p=[4, 5, 6, 7] 
      o/p=[9, 7, 5] 
     o/p=[5, 6, 7, 8, 9, 10]'''

'''lst=[1,2,3,4,5,6,7,8,9,10]
print(lst[2:7:2])
print(lst[4:9:2])
print(lst[3:7:1])
print(lst[8:3:-2])
print(lst[4::1])'''


#Q.24 To display only even numbers: n=[0,1,2,3,4,5,6,7,8,9,10]

'''n=[0,1,2,3,4,5,6,7,8,9,10]
for i in n:
     if i%2==0:
         print(i)
     else:
         continue'''

'''Q.25  To display elements by index wise: l=["A","B","C"] 
       o/p =A is available at positive index: 0 and at negative index: -3 
                B is available at positive index: 1 and at negative index: -2 
                C is available at positive index: 2 and at negative index: -1 '''

'''l=["A","B","C"]
print(f"l[0]={l[0]} and l[-3]={l[-3]}")
print(f"l[1]={l[1]} and l[-2]={l[-2]}")
print(f"l[2]={l[2]} and l[-1]={l[-1]}")'''

#Q.26 list=[]       o/p=['A', 'B', 'C']

'''list=[]
list.append('A')
list.append('B')
list.append('C')
print(list)'''

'''Q.27 To add all elements to list upto 100 which are divisible by 10
     o/p=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] '''

'''list=[]
for i in range(101):
    if i%10==0:
        list.append(i)
    else:
        continue
print(list)'''

'''Q.28 order1=["Chicken","Mutton","Fish"] 
       order2=["RC","KF","FO"] 
      o/p= ['Chicken', 'Mutton', 'Fish', 'RC', 'KF', 'FO'] '''

'''order1=["Chicken","Mutton","Fish"]
order2=["RC","KF","FO"]
order3=order1+order2
print(order3)'''

'''Q.29 order=["Chicken","Mutton","Fish"] 
        o/p=['Chicken', 'Mutton', 'Fish', 'M', 'u', 's', 'h', 'r', 'o', 'o', 'm'] '''

'''order=["Chicken","Mutton","Fish"]
print(f"Input list: {order}")
print("Output list: ",end='')
str='Mushroom'
lst=list(str)
print(order+lst)'''

#Q.30 n=[10,20,10,30]        o/p= [20, 10, 30]

'''n=[10,20,10,30]
print(f"Input list: {n}")
n.remove(10)
print(f"The list after removing 10 is: {n}")'''

#Q.31  n=[10,20,30,40]          o/p=[40, 30, 20, 10]

'''n=[10,20,30,40]
print(f"Input list is: {n}")
print(f"Output list in reverse order is: ",end='')
print(n[4::-1])'''

#Q.32  n=[20,5,15,10,0]       o/p=[0,5,10,15,20]

'''n=[20,5,15,10,0]
print(f"Input list is: {n}")
n.sort()
print(f"Output list in Ascending order is: {n}")'''
