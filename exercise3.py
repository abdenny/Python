##### 1/16
### Small
# 1.
# def madlib (name, subject):
#     statement = (f"{name}\'s favorite subject is {subject}")
#     return statement

# results = madlib("austin", "biology")
# print(results)


#2.
# def c_to_f (temp):
#     F = (temp * 9/5) + 32
#     return F

# temperature = c_to_f(56)
# print(temperature)


#3.
# def f_to_c (temp):
#     C = (temp - 32) * (5 / 9)
#     return C

# temperature = f_to_c(100)
# print(temperature)

######testing for nesting 
# def c_to_f (temp):
#     F = (temp * 9/5) + 32
#     return F


# def f_to_c (temp):
#     C = (temp - 32) * (5 / 9)
#     return C

# print(c_to_f(f_to_c(25)))



# 4. 
# def is_even (number):
#     if (number % 2) == 0:
#         return(True)
#     else:
#         return(False)

# print(is_even(35))


# #5.
# def is_odd (is_even):
#     if is_even != True:
#         return("The number is odd")
#     else:
#         return("the number is even")

# print(is_odd(is_even))


#6.
# def only_evens (list_of_numbers):
#     even_numbers = []
#     for i in list_of_numbers:
#         if (i % 2) == 0:
#             even_numbers.append(i)
#     return(even_numbers)

# print(only_evens([1,2,4,5,56,89,102]))

#7.
# def only_odds (list_of_nums):
#     odd_numbers = []
#     for i in list_of_nums:
#         if (i % 2) != 0:
#             odd_numbers.append(i)
#     print(odd_numbers)

# only_odds([1,2,56,78,99,456,477])

### Medium
#1.
# def smallest (list_nums):
#     return (min(list_nums))

# print(smallest([34,67,89,101]))

#or 




# #2.
# def largest (list_nums):
#     return(max(list_nums))

# print(largest([34,67,89,101]))

3. ### Using pythons key parameter to specify sorting value. Setting this equal to the len function to fid the shortest value.
def shortest (list_of_strings):
    return(min(list_of_strings, key=len))

print(shortest(["dog", "bird", "pizza"]))

#4.
# def longest (list_of_strings):
#     return(max(list_of_strings, key=len))

# print(longest(["dog", "bird", "pizza"]))


