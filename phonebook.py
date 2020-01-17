import pickle  
import os.path

if os.path.isfile("phonebook.pickle"):
    with open ("phonebook.pickle", "rb") as fh:
        phonebook_dictionary = pickle.load(fh)
else:
    phonebook_dictionary = {}

print("""Electronic Phone Book
==========================

1. Look up an entry

2. Set an entry

3. Delete an entry

4. list all entries

5. Quit
""")
while True:
    user_action = int(input("What would you like to do (1-5)? "))
    if user_action == 1:
        entry_search = input("what is the name of the person you'd like to look up? ")
        searching = phonebook_dictionary.get(str(entry_search))
        print(searching)
    elif user_action == 2:
        entered_name = input("What is the name of the person you would like to add to the phonebook? ")
        entered_phonenumber = input("What is the phone number of the person you'd like to add to the phonebook? ")
        phonebook_dictionary[entered_name] = entered_phonenumber
    elif user_action == 3:
        delete_entry = input("What is the name of the person you'd like to delete from the phonebook? ")
        del phonebook_dictionary[delete_entry]
        print("Your entry has been deleted")
    elif user_action == 4:
        print(phonebook_dictionary)
    elif user_action == 5:
        with open('phonebook.pickle', 'wb') as fh:
            pickle.dump(phonebook_dictionary, fh)
        print("Closing the program!")
        break    
    else:
        print("Please try again")


