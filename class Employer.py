class employer () :
    def __init__(self, base_salary, bonus_hrs, sales, name):
        self.base_salary = base_salary
        self.bonus_hrs = bonus_hrs
        self.sales = sales
        self.name = name 

    def calculate_net_salary (self):
        net_salary = (self.base_salary+self.bonus_hrs)
        print("the NetSalary is :",net_salary)

    def info (self):
        print(f"base salary: {self.base_salary}")
        print(f"bonus hours: {self.bonus_hrs}")
        print(f"sales: {self.sales}")
        print(f"Name: {self.name}")
    
#Main programm
emp_1 = employer(6000,100,10,"Ali")
emp_2 = employer(5000,150,15,"Mohammed")
emp_3 = employer(7000,200,20,"Kabbour")

print("\nEmployer 1:")
emp_1.info()
emp_1.calculate_net_salary()

print("\nEmployer 2:")
emp_2.info()
emp_2.calculate_net_salary()

print("\nEmployer 3:")
emp_3.info()
emp_3.calculate_net_salary()
