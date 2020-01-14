#1.
# bill_ammount = input("I hope you enjoyed your meal! How much was your total? ")
# service = input("Was your service good, fair, or bad?")

# if service == "good":
#     tip = float(bill_ammount) * .2
#     print(f"Tip ammount:{tip}")
# elif service == "fair":
#     tip = float(bill_ammount) * .15
#     print(f"Tip ammount:{tip}")
# elif service == "bad":
#     tip = float(bill_ammount) * .10
#     print(f"Tip ammount:{tip}")

# total_ammount = float(bill_ammount) + tip
# print("$"  + "%.2f" % total_ammount)

#2.
bill_ammount = input("I hope you enjoyed your meal! How much was your total? ")
service = input("Was your service good, fair, or bad?")

if service == "good":
    tip = float(bill_ammount) * .2
    print(f"Tip ammount:{tip}")
elif service == "fair":
    tip = float(bill_ammount) * .15
    print(f"Tip ammount:{tip}")
elif service == "bad":
    tip = float(bill_ammount) * .10
    print(f"Tip ammount:{tip}")

total_ammount = float(bill_ammount) + tip
print("$"  + "%.2f" % total_ammount)

ammount_of_people =input("How many people dined today?")
ammount_per_person = total_ammount / int(ammount_of_people)
print("The ammount per person is :$"  + "%.2f" %ammount_per_person)