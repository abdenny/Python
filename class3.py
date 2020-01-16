# #### Review
# ## Need counter 
# count=0
# while count < 3:
#     print("hello")
# #### Increase count by 1 on each loop
#     count += 1


#For examples
# students = ["Matt", "Foorkan", "Alex", "Mary"]
# for variable in students:
#     print(variable)

# #Nested for example
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# agenda = ["Lecture", "Homework", "Solutions"]

# for index in range(1,17):
#     print("Week: "+ str(index))
#     for day in days:
#         print(f"  {day}")
#         for action in agenda:
#             print(f"    {action}")

###### Function Notes
# def greeting():
#     print("Hello World!")

# def names ():
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")


# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# names()
# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# names()
# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# names()


# def greeting(person):
#     print(f"hello {person}!")
# greeting("austin")

# def add(num1, num2):
#     sum = num1 + num2
#     return sum

# result = add(4,8)
# print(result)

# def concat_list(list1, list2):
#     concat = list1 + list2 
#     return concat
# print(concat_list([1,2], [2,3]))

# def cal_avg(param1, param2, param3, param4):
#     sum = param1 + param2 + param3 + param4
#     avg = sum / 4
#     return avg

# result = cal_avg(1,2,3,4)

# print(result)

def cal_avg(list_of_num):
    sum = 0
    for i in list_of_num:
        sum += i
    avg = sum / len(list_of_num)
    return avg

num_list = [1,2,3,4,5,6,7,8,9]
results = cal_avg(num_list)
print(results)

# def myFunction(num1, num2, num3):

#     return num1*2, num2*3, num3*4

# result = myFunction(1, 2, 3)
# print(result)
#
#or
#
# def myFunction(num1, num2, num3):

#     return num1*2, num2*3, num3*4

# result = myFunction(1, 2, 3)
# print(result)