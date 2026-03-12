#  Polymorphism in Python refers to the ability of different objects to respond to the same method or function call in ways specific to their individual types.


# Method overloading is a feature where multiple methods in the same class have the same name but different parameters


# class Maths():
#     def add(self, *args):
#         return sum(args)


# obj = Maths()

# print(obj.add(6))
# print(obj.add(8, 7))


# Method overriding in Python is an object-oriented programming concept that allows a child class (subclass) to provide a specific implementation for a method that is already defined in its parent class (superclass). 


# class Animal():
#     def sound(self):
#         return(" I make Animal Sound")

# class Cow(Animal):
#     def sound(self):
#         return(" I make Cow sound ")

# class Dog(Animal):
#     def sound(self):
#         return "I make Dog Sound"


# obj1 = Animal()
# obj2 = Cow()
# obj3 = Dog()

# obj1.sound()
# obj2.sound()
# obj3.sound()


# demo = [Animal(), Cow(), Dog()]
# for x in demo:
#     print(x.sound())