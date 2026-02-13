# 1. Write a function named greet() that prints "Hello, Welcome to Python!". Call the function.

# def greet(name):
#     print(f"welcome to python {name}")

# greet("bose")


# 2. Write a function say_hello(name) that takes one parameter name and prints "Hello, <name>".


# def hello(name):
#     print(f"hello {name}")

# hello("dark")



# 3. Create a function add_numbers(a, b) that accepts two parameters and returns their sum. Print the returned value.


# def addnumbers(a,b):
#     return a+b
# result=addnumbers(4,4)
# print(result)




# 4. Write a function calculate_area(length, width) that returns the area of a rectangle. Call the function using positional arguments.

# def calculate_area(length,width):
#     return length * width
# calculate=calculate_area(5,10)
# print(calculate)



# 5. Create a function power(base, exponent=2) that returns the value of base raised to the power of exponent. Call the function once with default argument and once by passing both arguments.

# def power(base,exponent=2):
#     return base ** exponent

# answer=power(5)
# print(answer)

# answer1=power(5,4)
# print(answer1)



# 6. Write a function student_info(name, age, course) that prints student details. Call the function using keyword arguments in any order.

# def studentinfo(name,age,course):
#     print(f"student name : {name}")
#     print(f"student age : {age}")
#     print(f"student course : {course}")

# studentinfo(name="dark",age="21",course="python")
# print(studentinfo)



# 7. Create a function calculate_salary(basic_salary, bonus=2000) that returns the total salary. Call the function once with only basic_salary and once with both arguments.

# def calculate_salary(basic_salary, bonus=2000):
#     return basic_salary + bonus

# result=calculate_salary(3000)
# print(result)

# result1=calculate_salary(3000,4000)
# print(result1)


# 8. Write a function book_ticket(movie, seats, price=150) that returns the total ticket cost. Call the function using positional arguments and keyword arguments.


# def book_ticket(movie,seats,price=150):
#     return movie+seats+price

# total_ticket_cost=book_ticket(100,20,30)
# print(f"movie name bad : price :{total_ticket_cost}")

# total_ticket_cost2=book_ticket(100,50,50)
# print(f"movie name avatar3 : price :{total_ticket_cost2}")




# 9. Create a function math_operations(a, b) that returns sum, difference, and multiplication of the two numbers. Capture and print all returned values.


# def math_operations(a,b):
#     sum=a+b
#     diff=a-b
#     multi=a*b

#     return sum,diff,multi

# var=sum,diff,multi=math_operations(2,3)

# print(f"add :{var}")
# print(f"diff :{var}")
# print(f"multi :{var}")


