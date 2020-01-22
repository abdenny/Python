########Med Problems
# bill_ammount = input("What was your total bill ammount? ")
# service_quailty = input("Level of service? (Good, Fair, or Poor)")
# tip_ammount = ""

# if service_quailty.lower() == "good":
#     tip_ammount = float(bill_ammount)* .2
# elif service_quailty.lower() == "fair":
#     tip_ammount = float(bill_ammount)* .2
# elif service_quailty.lower() == "poor":
#     tip_ammount = float(bill_ammount)* .2
# total = float(tip_ammount) + float(bill_ammount)
# num_of_guest = int(input("How many guests?"))
# price_per_person = total / num_of_guest
# price_per_person = str(round(price_per_person, 2))
# print(f"The price per person is ${price_per_person}")


# initial_coins = 0
# while True:
#     more = input(f"You have {initial_coins} coins, would you like another? Enter yes or no.")
#     if more.lower() == "yes":
#         initial_coins += 1
#         print(initial_coins)
#     if more.lower() == "no":
#         print("bye")


# org_list = [1, 1, 1, 4, 7, 6, 5, 8, 9, 9, 3, 5, 6]
# new_list =[]
# for index in org_list:
#     if index not in new_list:
#         new_list.append(index)
# print(new_list)

# to_be_leeted = input("Enter the text you'd like to be transformed ").upper()
# leet_list = list(to_be_leeted)
# new_leet = []
# for letters in leet_list:
#     if letters == "A":
#         new_leet.append(4)
#     elif letters == "E":
#         new_leet.append(3)
#     elif letters == "G":
#         new_leet.append(6)   
#     elif letters == "I":
#         new_leet.append(1)   
#     elif letters == "O":
#         new_leet.append(0)   
#     elif letters == "S":
#         new_leet.append(5)   
#     elif letters == "T":
#         new_leet.append(7) 
#     else:
#         new_leet.append(letters)     
# leet = "".join(str(x) for x in new_leet)
# print(leet)