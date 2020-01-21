# #### Notes 1/17
# my_dictionary = {

#     "hello" : "world",
#     "square_of_two" : 4,
#     0 : 1
# }
# # print(my_dictionary)

# # print(my_dictionary["hello"])

# # print(my_dictionary.get(4)) ####Returns none instead of an error because there is no 4 key

# # is_it_there = "wat" in my_dictionary  ####Checks if a key is being used
# # print(is_it_there)
# #################################################
# # keys = my_dictionary.keys()   ####the variable created is now a list
# # print(keys)    # can do the samd for values using .values()

# # for index in keys:    #### Now we can loop
# #     print(f"{index} : {my_dictionary[index]}")
# #################################################

# # .items() gives keys and values in a tuple
# for key, value in my_dictionary.items():  #iterates through (key :value)
#     print(f"{key}, {value}")

# contacts = [{
#     "first_name" : "Austin",
#     "last_name" : "Denny"
#     }, 
#     {
#     "first_name" : "John",
#     "last_name" : "Kearney" ,
#     "phone" : {     ##### Key with value of dictionary
#         "cell" : "333-333-3333",
#         "home" : "444-444-4444"
#     }                            
#     },  
#     {
#     "first_name" : "Sean",
#     "last_name" : "Page" 
#     }]

# print(contacts[1]) 

# print(contacts[1]["first_name"])

# print(contacts[1]["first_name"], contacts[2]["first_name"])

# print(contacts[1]["first_name"] + " " + contacts[1]["last_name"])

# print(contacts[1]["phone"]["cell"]) #### Going deeper inside of the same index location

# my_dictionary = {
# #     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# my_dictionary["theMeaningOfLife"] = "wat"
# wat = my_dictionary["theMeaningOfLife"]
# print(wat)


# # my_dictionary["newKeyName"] = "hello world"
# # print(my_dictionary)
#  with open('phonebook.pickle', 'wb') as fh:
#      pickle.dump(phonebook_dictionary, fh)
