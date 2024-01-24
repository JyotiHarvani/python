#qt] create class  initialize  emp_name,emp_address and show employee emp_name,emp_address

class Employee:
    def __init__(self,name,address):
        self.n=name
        self.a=address
    def show(self):
        print("name of the employee: ",self.n)
        print("Address of the employee: ",self.a)

e1=Employee('Ravi','Nasik')
e2=Employee('Anuj','Pune')
e1.show()
e2.show()

#qt] declare instance var Inside Constructor

class Student:
    def __init__(self,name,grade):
        self.n=name
        self.g=grade
        self.address='Pune'
    def show(self):
        print("name:",self.n)
        print("grade:",self.g)
        print("address:",self.address)

s=Student('Rajesh',5)
s.show()

#qt] declare instance var Inside Method
class Marks:
    def __init__(self,term1_marks,term2_marks,term3_marks):
        self.m1=term1_marks
        self.m2=term2_marks
        self.m3=term3_marks
    def avg_marks(self):
        self.avg=(self.m1+self.m2+self.m3)/3

marks1=Marks(80,70,60)
marks1.avg_marks()
print("Average marks are: ",marks1.avg)

#qt] declare instance var Outside class
class Students:
    def __init__(self, name, grade):
        self.n = name
        self.g = grade
        self.address = 'Pune'

    def show(self):
        print("name:", self.n)
        print("grade:", self.g)
        print("address:", self.address)


s = Student('Rajesh', 5)

s.marks=90
print(s.__dict__)

#qt] create class family and count the Number of members inside family
class Family:
    def __init__(self):
            self.members=[]
    def add_member(self,name):
        self.members.append(name)
    def count_members(self):
        return len(self.members)

family1=Family()
family1.add_member('Raj')
family1.add_member('Ravina')
family1.add_member('Rakesh')
family1.add_member('Rajat')

n=family1.count_members()
print("Number of members in family1 is: ",n)

#qt] create class Fruits display your favorite fruit

class Fruits:
    def __init__(self,fav_fruit):
        self.f=fav_fruit
    def display(self):
        print("Your favourite fruit is: ",self.f)

my_fav_fruit=Fruits('Banana')
my_fav_fruit.display()


