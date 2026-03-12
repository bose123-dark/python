# # Object-Oriented Programming (OOP) in Python is a programming paradigm that organizes code around objects, which are instances of classes. It focuses on bundling related data (attributes) and behaviors (methods) into a single, self-contained unit to create modular, reusable, and maintainable applications



# # A class is a blueprint or template used to create objects.
# # It defines variables (data) and functions (methods) that the objects will have.


# # An object is an instance of a class.
# # It represents a real-world entity and can access the data and methods defined in the class.

# # Class
# class Car():

#     # Attibutes (Varibles)
#     colour = "White"
#     speed = 200
#     milage = 15

#     # Methods(Functions)
#     def brake(self):
#         print("The Car has stopped running")



# # Object   
# Audi = Car()


# Audi.colour = "Red"
# print(Audi.colour)

# Audi.speed = 250
# print(Audi.speed)

# Audi.milage = 20
# print(Audi.milage)


# Audi.brake()



# A constructor in Python is a special method used to initialize (assign values to) the object’s data when an object is created.

# _init_()


# class Animal:

#     def  _init_(self, colour , legs , sound):
#         self.colour = colour
#         self.legs = legs
#         self.sound = sound
    





# Cow = Animal("Black", 4 , "Cowsound")
# Dog = Animal("Brown", 4 , "Barking" )
# print(Cow.colour)
# print(Dog.sound)