class Task:
    def __init__(self,name):
        self.list_of_tasks = {
            'jan': "Identify your strengths!",
            'feb': "Control your anger and jealousy!",
            'mar': "Stop making excuses!",
            'apr': "Start doing meditation!",
            'may': "Read good books!",
            'jun': "Identify your skills and and work on them!",
            'jul': "Raise money for charity!",
            'aug': "Be more self-aware!",
            'sep': "Be thankful and appreciative!",
            'oct': "Love yourself!",
            'nov': "Practice self-control!",
            'dec': "Be honest,be helpful and try to make people happy!"
        }
        self.n = name
        print(f"Hi {self.n}!")
        print("Welcome to the Task Manager!")
        print("Follow these tasks monthwise to become a better version of yourself this year:")

    def show_task_of_month(self,month):
        print(f"Your task for {month} month is: ")
        print(self.list_of_tasks[month])

    def show_all_tasks(self):
        for k,v in self.list_of_tasks.items():
            print(f"{k} : {v}")

    def modify_task(self):
        mon = input("\nEnter which month's task you want to modify: ")
        if mon not in self.list_of_tasks.keys():
            mon = input("Please enter a valid month name: ")
        task = input(f"\nEnter the new task you want to add to month {mon}: ")
        self.list_of_tasks[mon] = task
        print("\nNow your new list of tasks is: ")
        self.show_all_tasks()



t1 = Task("Siya")
t1.show_all_tasks()

modify = input("\nEnter yes if you want to modify any task else no: ")
if modify == 'yes':
    t1.modify_task()
month = input("\nEnter month to know your current task: ")
t1.show_task_of_month(month)


class Employee:
    def __init__(self,name,age,address,salary,experience,department):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.experience = experience
        self.department = department

    def show(self):
        print("\nEmployee details are: ")
        print(f"employee name = {self.name}")
        print(f"age = {self.age}")
        print(f"address = {self.address}")
        print(f"salary = {self.salary}")
        print(f"experience = {self.experience} years")
        print(f"department = {self.department}")

emp = Employee('Rajseh',35,'Pune',45000,10,'HR')
emp.show()
