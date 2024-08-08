print("Welcome to the pizza delivery")
bill = 0
size = input("What size pizza you want? S, M, or L  ")
pepperoni = input("Do you want pepperoni? Y or N  ")
extra_cheese = input("Do you want extra cheese? Y or N  ")

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
        print(f"Your bill is ${bill} with pepperoni")
    else :
        bill = 15
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is ${bill} with extra cheese")
    else:
        bill = 15

elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
        print(f"Your bill is ${bill} with pepperoni")
    else:
        bill = 20
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is ${bill} with extra cheese")
    else:
        bill = 20
        
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
        print(f"Your bill is ${bill} with pepperoni")
    else:
        bill = 25
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is ${bill} with extra cheese")
    else:
        bill = 25
        
final_bill = bill
if final_bill ==15 or final_bill == 20 or final_bill == 25:
    print(f"Your final bill is ${bill} \n you haven't added any toppings")
    
else:
    print(f"Your final bill is ${final_bill}")