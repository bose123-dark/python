# Encapsulation in Python is a fundamental OOP concept that involves bundling data (attributes) and methods that operate on that data into a single unit, a class

# Getters are methods used to retrieve the value of a class attribute


# setters are methods used to modify or update the value of an attribute


# class Animal():
#     def _init_(self, name , age , city):
#         # Public Attributes
#         self.name = name

#         # Prootected Attribute
#         self._age = age

#         # Private Atribute
#         self.__city = city


#         # Getter Method
#     def getcity(self):
#             return self.__city
    
#     # ✅ Proper Setter Method
#     def setcity(self, new_city):
#         self.__city = new_city


# cow = Animal("John", "25" , "Pondicherry")
# print(cow.name)
# print(cow._age)
# print(cow.getcity())
# cow.setcity("Chennai")
# print(cow.getcity())







# class bike():
#     def __init__(self,model,year,cost):
#         self.model=model
#         self._year=year
#         self.__cost=cost


#     def bike1(self):
#             return self.__cost
    
#     def bike2(self,newbike):
#          self.__cost=newbike
    
# var1=bike("yamaha","2026",15000)

# print(var1.model)
# print(var1.bike1())
# var1.bike2(1,50,000)
# print(var1.bike1())
    

