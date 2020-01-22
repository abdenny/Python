########## Making a vehicle class
# # class Vehicle:
# #     def __init__(self, make, model, year):
# #         self.make = make 
# #         self.model = model 
# #         self.year = year 
    
# #     def print_info(self):
# #         print(self.make, self.model, self.year)


# # car = Vehicle("Nissan", "Leaf", "2015")
# # print(car.make, car.model, car.year)
# # car.print_info()

# ######### Sonny and Jordan part 2
class Person: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

    def print_contact_info(self):
        print(f"Sonny's email is : {self.email}. Sonny's phone number is: {self.phone}")
    
    def add_friend(self, fname):
        self.friends.append(fname)
    
    def num_friends(self):
        print(f"They have {len(self.friends)} friends")

    

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
sonny.print_contact_info()
sonny.friends.append(jordan)
jordan.friends.append(sonny)
print(f"{jordan.name} has {len(jordan.friends)} friends.")
print(f"{sonny.name} has {len(sonny.friends)} friends.")

jordan.add_friend(sonny)
jordan.num_friends()
jordan.greet(sonny)
print(jordan.greeting_count)