# list_1 = []
# to_add = input("Add items to the list ")
# while len(to_add) > 0:
#     list_1.extend([to_add])
#     print(list_1)
#     to_add = input("Add items to the list ")
# print(list_1)

# numbers = [1,2,3,4,5]
# numbers.insert(3,6)

# poppedvalue = numbers.pop()
# print(poppedvalue)


# for index in range(1,1001,2):
#     print(index)

for outer_index in range(1,11):
    for inner_index in range(1,11):
        result = outer_index * inner_index
        print(f'{str(outer_index) }   x   {str(inner_index)}   =   {str(result)}')