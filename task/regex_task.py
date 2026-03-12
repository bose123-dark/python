import re

name_new=r"[A-Z a-z]{3,20}"









name=input("Enter The Name")

def define(pattern,value):
    return re.fullmatch(pattern,value)is not None




print("Name valid",define(name_new,name))