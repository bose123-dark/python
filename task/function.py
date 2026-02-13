nums = [3, 6, 9, 12, 15, 18, 21, 24]
from functools import reduce

# 1. Use map() to create a list of squares of all numbers.

# squares=list(map(lambda x:x**2,nums))
# print(squares)


# 2. Use filter() to extract only even numbers.

# sum=(filter(lambda x:x %2==0,nums))
# print(nums)


# 3. Use filter() to extract numbers greater than 10.

# sum=list(filter(lambda x:x >10,nums))
# print(sum)


# 4. Use map() to convert all numbers into strings.


# sum=list(map(str,nums))
# print(sum)


# 5. Use reduce() to find the sum of all numbers.

# sum=(reduce(lambda a,b : a+b,nums))
# print(sum)


# 6. Use reduce() to find the product of all numbers.


# sum=(reduce(lambda a,b : a*b,nums))
# print(sum)



# 7. Use filter() to keep only numbers divisible by 3.



# sum=list(filter(lambda x:x % 3==0,nums))
# print(sum)



# 8. Use map() to double each number.

# squares=list(map(lambda x:x*2,nums))
# # print(squares)



# 9. Use filter() and map() to keep only even numbers and then square them.

# sum = list(map(lambda x: x*2,filter(lambda x: x % 2 == 0, nums)))
# print(sum)


# 10. Use filter(), map(), and reduce() to filter numbers greater than 10, square them, and find their total sum.

# sum = list(map(lambda x: x*2,filter(lambda x: x >10,reduce(lambda a,b :a+b,nums))))
# print(sum)
