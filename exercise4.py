##### 1/17 HW
### Small Problems 
#1.
# phonebook_dict = {
#     "Alice" : "703-493-1834",
#     "Bob" : "857-384-1234",
#     "Elizabeth" : "484-594-2923"}

# print(phonebook_dict["Elizabeth"])
# phonebook_dict["Kareem"] = "938-489-1234"
# del(phonebook_dict["Alice"])
# phonebook_dict["Bob"] = "968-345-2345"
# print(phonebook_dict)

#2.
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }
# print(ramit['email'])
# print(ramit['interests'][0])
# for i in ramit["friends"]:
#     if i["name"] == "Jasmine":
#         print( i["email"])
# for n in ramit["friends"]:
#     if n["name"] == "Jan":
#         print(n["interests"][1])

# #3. ##### Need to finish
# def count_friends(in_dict):
#     if in_dict is dict:
#         in_dict[""]

###Med
# #1.
# letter_histogram = {}
# entered_word = input("Please enter a word... ")
# for repeats in entered_word:
#     if repeats not in letter_histogram:
#         letter_histogram[repeats] = 0
#     letter_histogram[repeats] += 1
# print(letter_histogram)

#2.
# sent_histogram = {}
# entered_sentence = input("Please enter a sentence... ")
# sent_to_words = entered_sentence.split()
# for repeats in sent_to_words:
#     if repeats not in sent_histogram:
#         sent_histogram[repeats] = 0
#     sent_histogram[repeats] += 1
# print(sent_histogram)

#3.
sent_histogram = {}
entered_sentence = input("Please enter a sentence... ")
sent_to_words = entered_sentence.split()
for repeats in sent_to_words:
    if repeats not in sent_histogram:
        sent_histogram[repeats] = 0
    sent_histogram[repeats] += 1
for key, value in sorted(sent_histogram.items(), key=lambda kv: kv[1], reverse=True):
    print("%s: %s" % (key, value))