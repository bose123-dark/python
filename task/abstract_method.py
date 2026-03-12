# # from abc import ABC , abstractmethod

# # class showroom(ABC):
# #     def brand(self):
# #         return "There no bike imported"

# #         @abstractmethod
# #         def brand1(self):
# #             pass

# # class brand2(showroom):
# #     def brand1(self):
# #         print("new bike are imported")

# # result=brand2()

# # result.brand1()
# # print(result.brand)





# # Implement method overloading in a class Calculator using *args:
# # If 2 numbers are passed, return their multiplication.
# # If 3 numbers are passed, return their average.
# # If more than 3 numbers are passed, return their sum.

# class Calculator:
    
#     def calculate(self, *args):
#         count = len(args)
#         print("how many arguments:", count)

#         if count == 2:
#             return args[0] * args[1]

#         elif count == 3:
#             return sum(args) / 3

#         elif count > 3:
#             return sum(args)

#         else:
#             return "Provide at least 2 numbers"


# calc = Calculator()

# print(calc.calculate(5, 4))            
# print(calc.calculate(10, 20, 30))      
# print(calc.calculate(1, 2, 3, 4, 5))