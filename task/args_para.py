# 1. Write a function that uses *args to print all numbers passed to it.

# def numbers(*args):
#     for all in args:
#       print(all)
# numbers(10,20,30)


# 2. Write a function that uses *args to find the largest number.

# def num(*args):
#     print(max(args))
# num(1,8,5,10,23,27,14,17)


# 3. Write a function that uses *args to count how many values were passed.

# def num(*args):
#     print(len(args))
# num(1,8,5,10,23,27,14,17)

# 4. Write a function that uses *args to return all arguments as a list.

# def all_list(*args):
#     return list(args)

# result=all_list(10,20,30,40)
# print(result)

# 5. Write a function that uses **kwargs to print all keys and values.

# def all_keys(**kwargs):
#     for key,values in kwargs.items():
#         print(f"{key},{values}")
# all_keys(name="dark",age=21)


# 6. Write a function that uses **kwargs to return only the keys.


# def all_keys(**kwargs):
#     return list(kwargs.keys())
# var=all_keys(name="dark",age=21)
# print(var)


# 7. Write a function that uses **kwargs to return only the values.

def all_keys(**kwargs):
    return list(kwargs.values())
var=all_keys(name="dark",age=21)
print(var)


# 8. Write a function that uses **kwargs to check if a specific key exists.


# def key_exists(key, **kwargs):
#     if key in kwargs:
#         print("Key exists")
#     else:
#         print("Key does not exist")

# # Example call
# key_exists("name", name="dark", age=21)



# 9. Write a function that uses both *args and **kwargs and prints them separately.

# def both_arguments(*args,**kwargs):
#     print("argument:",args)
#     print("keyword:",kwargs)

# var=both_arguments(10, 20, name="dark",age=21)
# print(var)

