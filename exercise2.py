#####1/15 HW
### Medium 
#1.
# list_1 = [2, 4, 5]
# list_2 = [2, 3, 6]
# new_list = [(list_1[0] * list_2[0]), (list_1[1] * list_2[1]),(list_1[2] * list_2[2])]
# print(new_list)

#2.
# dim_1 = [2, -2], [5, -3]
# dim_2 = [2, -2], [5, -3]
# result_list =[]

# for d1_index in range(len(dim_1)):
#     for d2_index in range(len(dim_2)):
#         if (d1_index == d2_index):
#             working_list = []
#             sum1 = dim_1[d1_index][0] + dim_2[d2_index][0]
#             sum2 = dim_1[d1_index][1] + dim_2[d2_index][1]
#             working_list.append(sum1)
#             working_list.append(sum2)
#             result_list.append(working_list)
# print(result_list)

#3.
# dim_1 = [2, -2, 3], [5, -3, 3]
# dim_2 = [2, -2, 3], [5, -3, 3]
# result_list =[]

# for d1_index in range(len(dim_1)):
#     for d2_index in range(len(dim_2)):
#         if (d1_index == d2_index):
#             working_list = []
#             sum1 = dim_1[d1_index][0] + dim_2[d2_index][0]
#             sum2 = dim_1[d1_index][1] + dim_2[d2_index][1]
#             sum3 = dim_1[d1_index][2] + dim_2[d2_index][2]
#             working_list.append(sum1)
#             working_list.append(sum2)
#             working_list.append(sum3)
#             result_list.append(working_list)
# print(result_list)


#4.
# list_1 = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8]
# new_list = []
# for index in list_1:
#     if index not in new_list:
#         new_list.append(index)
# print(new_list)

# #5.
# A, E, G, I, O, S, T = (4, 3, 6, 1, 0, 5, 7)
# string_given = "I am a leet programmer"
# print()

#6.
# statement = ("I am a leet programmer").upper()
# leet_list = list(statement)
# for i in range(len(leet_list)):
#     if leet_list[i]== "A":
#         leet_list[i] = "4"
#     elif leet_list[i] == "E":
#         leet_list[i] = "3"
#     elif leet_list[i] == "G":
#         leet_list[i] = "6"
#     elif leet_list[i] == "I":
#         leet_list[i] = "1"
#     elif leet_list[i] == "O":
#         leet_list[i] = "0"
#     elif leet_list[i] == "S":
#         leet_list[i] = "5"
#     elif leet_list[i] == "T":
#         leet_list[i] = "7"
# leet_statement = "".join(leet_list).lower()
# print(leet_statement)
