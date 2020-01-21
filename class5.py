###### Tuesday 1/21
##Passed by ref example, shows the need for oop
# myList = [1,2,3,4]

# def change_list(alist):
#     alist[0] = 5

# print(myList)

# change_list(myList)

# print(myList)

##### Objects Notes
# Global data can be easily corrupted when using functional programming. 
# Problems with structured programming:
#     Emphasises functionality, not data. Data is so valuable.
#     Limitations. Functional programming becomes hard to maintain with large code bases.
#     Gap in developer client communication. General public thinks in objects, not functions. 
# Data is the most important part of a program
#Objects 
#Class - Models the template for the objects 
#Abstraction - Narrow your focus to the attributes that you need
#Encapsulation - Solves the problem of data integ. Allows us to protect our data. Public/Private functions. Access when necc.
#Inheritance - Objects dont exist by themselves. Allows us to inherit functionally from a parent. 

#Class - Container to hold constructs 
#class className:     Class is a keyword.
#    block or pass
# class Greeting:
#     def say_hello(self):
#         print("Hello there!")

###Dot operator       Creating a new object from a class
# new_greeting_object = Greeting()
# new_greeting_object.say_hello()


###Create a class called student the makes a method that says "Good Morning". From this create 3 students 
# class Student: 
#     def say_good_morning(self):
#         print("Good morning!")
# ##Created object
# alina = Student()
# ##call method
# alina.say_good_morning()

# Alex = Student()
# Alex.say_good_morning()

# Sean = Student()
# Sean.say_good_morning()

###Self 
# Points back to memory object in original objects

#### Working with Constructors
# In a constructor objects are always called
# class Student: 
#     def __init__(self):
#         print("Const. called")

#     def say_good_morning(self):
#         print("Good morning!")

# Alex = Student()
    #### Calls Const without dot function . We can also use methods for entire classes of objects like strings 


#### Distinguishing between objects that are pointing to the smae class by using name
# class Animal:
#     def __init__(self, name):
#         self.name = name

# dog = Animal("dog")
# cat = Animal("cat")
# horse =Animal("horse")
# print(dog.name.capitalize())
# print(cat.name)
# print(horse.name)

####First parameter is always self (by convention)

###### Student constructor callling name 
# class Student: 
#     def __init__(self, name):
#         ###Setting an instance variable to whats passed in
#         self.name = name

#     def say_good_morning(self):
#         print("Good morning!")

#     #maps to name in method parameters
# alina = Student("Alina")
# print(alina.name)



# import datetime

# class Person: 
#     def __init__(self, fname, lname, birthdate, address, email):
#         self.fname = fname 
#         self.lname = lname 
#         self.birthdate = birthdate
#         self.address = address
#         self.email = email
    
#     def age(self):  ####USing the info passed into the class in another metod to reurn age
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year
#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1
        
#         return age


# sammy = Person("sammy", "kry", datetime.date(1998, 8, 21), "123 Ses St", "Email")

# print(f"{sammy.fname} {sammy.lname}")
# print(sammy.lname)

# age = sammy.age()
# print(age)
##########
# def greeting(name):
#     count = 0
#     print(f"hello {name}")
#     count += 1
#     print(count)

# greeting("Austin")
# greeting("Alex")
# greeting("Jaye")
# greeting("Meryem")
#
#or
#
# class Person:
#     def __init__(self, name):
#         self.name = name 
#         self.count = 0

#     def greeting(self):
#         print(f"Hello {self.name}")
#         self.count += 1
    
#     def print_count(self):
#         print(self.count)

# austin = Person("austin")
# austin.greeting()
# austin.greeting()
# austin.greeting()
# austin.greeting()
# austin.greeting()
# austin.print_count()

###########
# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
# sonny.greet(jordan)
# jordan.greet(sonny)
# print(f"Sonny's email address is {sonny.email}. Sonny's phone number is {sonny.phone}")
# print(f"Jordan's email address is {jordan.email}. Jordans phone number is {jordan.phone}")

######## Starting methods with underscore is the convention for not accessing private methods, double underscore is super private. However, python still allows it.

####Inheritance
# all strings are objects based on the string class
# inherit base class of string, creating a reverse string
# class  Vstring(str):
#     def reverse(self, name):
#         rstring = ""
#         for char in name:
#             rstring = char + rstring
#         return rstring
# my_string = Vstring("hello")
# print(my_string.capitalize())
# reversed = my_string.reverse("hello")
# print(reversed)

###########################
# class Character:
#     def __init__(self, name, power, health):
#         self.name = name 
#         self.power = power 
#         self.health = health 

# class Hero(Character):
#     def __init__(self, weapon, name, power, health):
#         self.weapon = weapon 
#         super(Hero, self).__init__(name, power, health)

# alina = Hero("pinkgun", "alina", 3, 10)

# #####only alina.weapon is initialized, we have to intialize the attributes from the base class. Since it has one init it's satisfied. We have to call super().
# print(alina.power)

########## Making a vehicle class
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model 
#         self.year = year 
    
#     def print_info(self):
#         print(self.make, self.model, self.year)


# car = Vehicle("Nissan", "Leaf", "2015")
# print(car.make, car.model, car.year)
# car.print_info()

######### Sonny and Jordan part 2
# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone


#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

#     def print_contact_info(self):
#         print(f"Sonny's email is : {self.email}. Sonny's phone number is: {self.phone}")

# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
# sonny.print_contact_info()