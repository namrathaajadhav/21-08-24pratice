#polymorphism
class macbook:
    def __init__(self, model,price):
     self.model = model
     self.price = price

    def colour(self):
       print("macbook is in grey colour")

class iphone:
    def __init__(self, model,price):
     self.model = model
     self.price = price

    def colour(self):
       print("iphone is in black colour")
     
class Tab:
    def __init__(self, model,price):
     self.model = model
     self.price = price

    def colour(self):
       print("Tab is in white colour")

mac = macbook("book air", 100000) 
Iphone = iphone("13 pro max", 66000)
tab = Tab("samsung", 20000)

for device in (mac,Iphone,tab):
 device.colour()



 #operator overloading
class Time:
 def __init__(self, hours, minutes, seconds):
  self.hours = hours 
  self.minutes = minutes
  self.seconds = seconds

def __add__(self, other):
 total_seconds = self.seconds + other.seconds
 total_minutes = self.minutes + other.minutes + total_seconds // 60
 total_hours = self.hours + other.hours + total_minutes // 60
 total_seconds %= 60
 total_minutes %= 60
 return Time(total_hours, total_minutes, total_seconds)

def __str__(self):
 return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

t1 = Time(10, 20, 15)
t2 = Time(2, 45, 25)

t3 = t1 + t2
print(t3) 




#overriding 

class Vehicle:
 def __init__(self, color):
  self.color = color

def move(self):
 print(f"{self.brand} vehicle started")

class Car(Vehicle):
 def __init__(self, brand, model):
  self.brand = brand
  self.model = model

def move(self):
  print(f"{self.brand} {self.model} is accelerating")

class Bicycle(Vehicle):
 def __init__(self, brand, num_gears):
  self.brand = brand  
  self.num_gears = num_gears

def move(self):
  print(f"Bicycle with {self.num_gears} gears is pedaling")

car = Car("Toyota", "white")
bicycle = Bicycle("Harley-Davidson", "V-Twin")

car.move()
bicycle.move()