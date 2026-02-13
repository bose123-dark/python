
# 1. Create a dictionary with keys name, age, and status. Print the dictionary.


# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }
# print(my_dictionary)


# # 2. Create a dictionary that contains duplicate keys. Print the dictionary and observe the result.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# print(my_dictionary)

# 3. Find and print the length of a dictionary.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# length=len(my_dictionary)
# print(length)

# 4. Print the data type of a dictionary.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# length=(type(my_dictionary))
# print(length)


# 5. Convert a list into a set and print the result.


# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# length=(list(my_dictionary))
# print(length)


# 6. Create a dictionary using the dict() constructor.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# length=(dict(my_dictionary))
# print(length)


# 7. Access a value from a dictionary using the get() method.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# name=my_dictionary.get("age")
# print(name)


# 8. Access a value from a dictionary using square brackets.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# print(my_dictionary["age"])

# 9. Check whether a specific key exists in a dictionary using the in operator.


# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# if "age" in my_dictionary:
#     print("key exits")
# else:
#     print("key exits does not exits")
    

# 10. Add a new key-value pair to an existing dictionary.


# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }
# my_dictionary["num"]="5"
# print(my_dictionary)


# 11.Modify the value of an existing key in a dictionary.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }
# my_dictionary["age"]="22"
# print(my_dictionary)


# 12. Remove a key from a dictionary using the del keyword.


# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# del(my_dictionary["name"])
# print(my_dictionary)


# 13. Remove a specific key from a dictionary using the pop() method.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# var=my_dictionary.pop("age")
# print(var)


# 14. Remove the last inserted item from a dictionary using popitem().


# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# var=my_dictionary.popitem()
# print(var)


# 15. Clear all elements from a dictionary.


# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }
# var=(my_dictionary.clear())
# print(var)


# 16. Make a copy of a dictionary and print both dictionaries.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# var=my_dictionary.copy()

# print(my_dictionary)
# print(var)


# 17. Modify the original dictionary after copying it and compare both dictionaries.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# my_dictionary1=my_dictionary.copy()

# my_dictionary["name"]="dark"
# my_dictionary1["class"]=10

# print("orginal dic",my_dictionary)
# print("duplicate dic",my_dictionary1)


# 18. Loop through a dictionary and print only the keys.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# for loop in my_dictionary:
#     print(loop)


# 19. Loop through a dictionary and print only the values.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# for values in my_dictionary.values():
#     print(values)


# 20. Loop through a dictionary and print key-value pairs using the items() method.


# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# for values in my_dictionary.items():
#     print(values)



# 24. Update a dictionary using the update() method.

# my_dictionary={
#     "name" : "hello",
#     "status" : "class",
#     "age" : "21"

# }

# my_dictionary.update({"name" : "dark"})
# print(my_dictionary)


