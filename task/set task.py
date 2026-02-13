# 1. Create a set named colors with values "red", "blue", "green". 
#    Create a copy of the colors set and add "yellow" to the copied set using add().



# colors={"red","blue","green"}
# colors.add("violet")
# print(colors)


# 2. Remove "blue" from the copied colors set using remove().


# colors={"red","blue","green"}
# colors.add("violet")
# colors.remove("blue")
# print(colors)



# 3. Try to remove "black" from the copied colors set using discard().

# colors={"red","blue","green"}
# colors.discard("red")
# print(colors)


# 4. Write code to check whether "red" exists in the copied colors set.

# colors=input("enter the colors ")

# if colors in "red" :
#     print("true")
# else:
#     print("false")



# 5. Use pop() to remove any one element from the copied colors set and print the removed value.

# colors={"red","blue","green"}

# anothercolors=colors.pop()
# thirdcolors=colors.copy()
# print(anothercolors)
# print(thirdcolors)


# 6. Create two sets A = {1, 2, 3, 4} and B = {3, 4, 5, 6}. 
#    Create copies of both sets and find their union.


# a={1,2,3,4}
# b={3,4,5,6}

# x=a.copy()
# y=b.copy()

# anotherset=x.union(y)
# print(anotherset)



# 7. Using the copied sets A and B, find their intersection.

# a={1,2,3,4,6,5,}
# b={1,2,3,6}

# num=a.intersection(b)
# print(num)




# 8. Find the difference between the copied set A and the copied set B.


# a={2,5,4,1,3,6}
# b={6}

# num=a.difference(b)
# print(num)



# 9. Create a copy of set A and add a new element to the copied set.

# data={"datatype","newdata"}

# newdata=data.add("data")
# print(data)


# 10. Clear all elements from the copied set using clear().

# name={"name","gaming"}

# newname=name.copy()
# secondname=newname.clear()
# print(newname)