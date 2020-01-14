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

# ammount_of_people =input("How many people dined today?")
# ammount_per_person = total_ammount / int(ammount_of_people)
# print("The ammount per person is :$"  + "%.2f" % ammount_per_person)

#3.
# initial_coins = 0 
# while True:
#     print(f"You have {initial_coins} coins")
#     more = input("do you want another?")
#     if more == "yes":
#         initial_coins += 1
#     if more == "no":
#         print("Bye")
#         break

#4. 
# width = int(input("width?"))
# height = int(input("height?"))
# print("*" * width)
# for i in range((height-2)):
#     print("*" + " " * (width -2) + "*")
# print("*" * width)

#5.
# n=7
# for i in range(n):
#     print(' '*n, end= '') 
#     print('* '*(i)) 
#     n-=1

6.
for i in range (1,11):
    for n in range (1,11):
        result = i * n
        print(str(i) + "   " + "X    "+str(n) + "=" + str(result))

