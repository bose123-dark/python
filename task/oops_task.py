# # class

# class Bike():

# #   variables
#     color="black"
#     mileage=50
#     bike_name="suzuki 150"
#     speed=110

# #    function
#     def brake(self):
#         print("the bike movement as stopped")

# # object
# model = Bike()

# model.mileage=55
# print(model.mileage)


# print(model.speed)

# model.brake()


# class toys():
#     def __init__(self,toysname,collection,price):
#         self.toysname=toysname
#         self.collection=collection
#         self.price=price


# God_of_war=toys("kratos",5,800)
# print(God_of_war.toysname)
# print(God_of_war.price)



# 1. Constructor (__init__)

# * Takes three parameters: make (string), model (string), and year (integer).
# * Initializes these as attributes of the class.


# class bike():
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year

# bikes=bike("suzuki","gixxer",2026)
# print(bikes.make)
# print(bikes.model)
# print(bikes.year) 



# 2. Methods:

# * display_info(self) → Prints all the car’s details as: "Car: <year> <make> <model>"
# * age(self, current_year) → Returns the age of the car: current_year - year


# class car():
#     def __init__(self,year,make,model):
#         self.year=year
#         self.make=make
#         self.model=model

#     def age(self,currentyear):
#             return currentyear - self.year

# car_1=car(2018,"BMW","BMW M3")
# print(car_1.model)

# print("car age: ",car_1.age(2026)) 



