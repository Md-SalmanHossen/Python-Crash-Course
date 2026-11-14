class Employee:
   emp_num=0

   def __init__(self,first,last,pay):
      self.first=first
      self.last=last
      self.email=first+ '.'+last+'@gmail.com'
      self.pay=pay
      Employee.emp_num+=1
   
   def fullname(self):
      return f'{self.first} {self.last}'
   
emp1=Employee('Abc','Cde',5000)
print(Employee.emp_num)
print(emp1.fullname())
print(emp1.pay)
print(emp1)

print("\n")

# practice 
class Car :
   def __init__(self,brand,color):
      self.brand=brand
      self.color=color
   
   def display_info(a):
      return f"{a.color} {a.brand}"

my_car=Car("Toyota","Red")
print(my_car.display_info())
print(my_car.brand);
print(my_car.color,"\n");