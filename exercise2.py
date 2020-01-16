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


# 4.
# list_1 = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8]
# new_list = []
# for number in list_1:
#     if number not in new_list:
#         new_list.append(number)
# print(new_list)

#5.
# statement = ("I am a leet programmer").upper()
# leet_list = list(statement)
# for letter in range(len(leet_list)):
#     if leet_list[letter]== "A":
#         leet_list[letter] = "4"
#     elif leet_list[letter] == "E":
#         leet_list[letter] = "3"
#     elif leet_list[letter] == "G":
#         leet_list[letter] = "6"
#     elif leet_list[letter] == "I":
#         leet_list[letter] = "1"
#     elif leet_list[letter] == "O":
#         leet_list[letter] = "0"
#     elif leet_list[letter] == "S":
#         leet_list[letter] = "5"
#     elif leet_list[letter] == "T":
#         leet_list[letter] = "7"
# leet_statement = "".join(leet_list).lower()
# print(leet_statement)
#

#6.
# word = input("Please enter a word ")
# converted_word = list(word.lower())
# lengthened_word = []

# lengthened_vowels = {"a" : "aaa", "e" : "eee", "i" : "iii", "o" : "ooo", "u" : "uuu"}
# for letter in converted_word:
#     if letter in lengthened_vowels:
#         letter = lengthened_vowels[letter]
#         lengthened_word.append(letter)
#     else: 
#         lengthened_word.append(letter)
# result = "".join(lengthened_word)
# print(result)

#7.
alphabet = "abcdefghijklmnopqrstuvwxyz"
scrambled_phrase = "lbh zhfg hayrnea jung lbh unir yrnearq"
key = 13
result = ""

for letter in scrambled_phrase:
    if letter not in alphabet:
        unknown_phrase = letter
    if letter in alphabet:
        search_letter_location = alphabet.find(letter)
        search_2 = (search_letter_location + key) % 26
        unknown_phrase = alphabet [search_2]
    result += unknown_phrase
print(result)
