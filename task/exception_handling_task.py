# # Python Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing. Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.




# a = 10
# b = 2
# try:
#    output = a/b
# except:
#     print("This is a error statement")
# else:
#     print(f"{output} My code working good")
# finally:
#     print("My Exception Hadnling Process is completed")



# 1. Asks the user to enter:

#    * First number
#    * Second number
# 2. Divides the first number by the second number.

# Requirements:
# * Use try to write the division code.
# * Use except to handle any error (like wrong input or division problem).
# * Use else to print the result if no error happens.
# * Use finally to print:



# try:

#  user=int(input("enter the number "))
#  user_1=int(input("enter the number "))


#  another_user=user/user_1

# except ValueError:
#  print("this is error statement")

# except ZeroDivisionError:
#  print("zero division error")

# else:
#  print("finished",another_user)

# finally:
#  print("output is ready")