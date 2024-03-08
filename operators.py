#Arithmetic operators
'''a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)'''

# // floor operator
'''print(10//2)
print(10//3)
print(15//3)
print(10.12//3)
print(-10//2)
print(-10//-3)
print(10//(-3))
print(10//3.2)
print(10//-3.2)'''

'''a="suma"
b=10
c="shaikh"
#print(a+b)
print(a+c)
print(a+" "+c)
print(c*2)'''

'''a=10
b=20
print("a>b",a>b)
print("a>=b",a>=b)
print("a<b",a<b)
print("a<=b",a<=b)'''

'''a="xyz"
b="abc"
print("a>b",a>b)
print("a<b",a<b)
print("a>= b is ",a>=b)
print("a<= b is ",a<=b)'''

'''print(True>True)
print(True>=True)
print(20>=True)
print(False > True)
print(False < True)'''

#chaining relational operators

'''print(10<20)
print(10<20<30)
print(10<20<30<40)
print(10<20<30<40>50)
print(10<20<30<=40<50)
print(10<20<30>=40<50)'''


#logical operators

# x and y
'''x=10
y=0
print(x and y)
print(x or y)
print(not x)'''

#Assignment Operators

'''x=10
x+=10
print(x)
x=x+10
print(x)
x-=20
print(x)
x=x-20
print(x)'''

#Ternary Operator

'''a,b=60,20
print(a)
print(b)

x=30 if a>b else 40
print(x)'''

#identity operators

#identity operator for numeric
'''a=10
b=10
print(id(a))
print(id(b))
print(a is b)
print(a==b)'''

#identity operator for string
'''str1='python'
str2='python'
print(id(str1))
print(id(str2))
print(str1 is str2)
print(str1==str2)'''

#identity operator for tuple
'''t1=(10,20,30)
t2=(10,20,30)
print(id(t1))
print(id(t2))
print(t1 is t2)
print(t1==t2)'''



#identity operator for list
'''list_1=[10,20,30]
list_2=[10,20,30]
print(id(list_1))
print(id(list_2))
print(list_1 is list_2)
print(list_1==list_2)'''

# membership operator

#membership operator for string

'''txt="python is easy"
print('python' in txt)'''

#membership operator for list

'''list=[10,2.15,'john']
print(10 in list)
print('john' in list)
print(20 in list)'''

#membership opeartor for tuple

'''t=(10,3.14,'josh')
print(10 in t)
print(3.14 in t)'''

#operator precedence
'''
**
/,*,%,//
+,-
'''

'''a=(10+5)*10-6+32/2**4
print(a)

b=5+45*10-50+10**2+(15/5)
print(b)

c=100//5+20%2**2-15+(15/3*5)
print(c)'''


#swap two elements without using third var
'''a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(f"Before swapping a={a} and b={b}")
a=a+b
b=a-b
a=a-b
print(f"After swapping a={a} and b={b}")'''












