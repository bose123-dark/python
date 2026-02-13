# 1. Write a Python program using match-case to display the day of the week for a number from 1 to 7.#

# day=int(input("enter the number for day"))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("invalid day")   


# 2. Write a Python program using match-case to find the season based on the month number.#                 


# month=int(input("Enter The Number For Month and Season Base"))
# day=13

# match month:
#     case 1 | 11 | 12 | 7 if day !=13 | 14 | 15 | 16:
#         print("Season : Winter Season")
#     case 3 | 4 | 2 |5 :
#         print("Season : Summer Season")
#     case 6 | 8 | 9 | 10 :
#         print("Season : Rainy season ")
#     case 13 | 14 | 15 | 16:
#         print("Week Of The Day In june month and Rainy Season ")
#     case _:
#         print("After 12 there is no month")


# 3. Write a Python program using match-case to display the grade based on mar # 

# mark =int(input("enter the mark"))

# match mark:
#     case student if mark >0 and  mark <=34:
#         print("fail")
#     case student if mark >35 and mark <=60:
#         print("Grade C")
#     case student if mark >61 and mark <=80:
#         print("Grade B")
#     case student if mark >81 and mark <=100:
#         print("Grade A")
#     case _:
#         print("invalid mark")


# 4. Write a Python program using match-case to perform basic calculator operations (+, −, ×, ÷). #


# a=int(input("Enter The First Number"))
# b=int(input("Enter The Second Number"))

# cal=input("Enter The calculation symbol(+,-,*,/,**,//)")

# match cal:
#     case "+":
#         print(a+b)
#     case"-":
#         print(a-b)
#     case"*":
#         print(a*b)
#     case"**":
#         print(a**b)     
#     case"/":
#         print(a/b)
#     case"//":
#         print(a//b)    
#     case _:
#         print("invalid symbol")

# 5. Write a Python program using match-case to check whether a number is even or odd. #

# num =int(input("Enter The Number"))

# match num %2:
#     case 0:
#         print("The Number Is Even")
#     case 1:
#         print("The Number Is Odd")

