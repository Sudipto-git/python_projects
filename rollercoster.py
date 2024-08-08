print("welcome to the safari rollarcoster")

height = int(input("what is your height in cm?  "))
bill = 0

if height > 120:
    print("you can ride the rollercoster")
    age = int(input("what is your age?  "))
    if age<12:
        bill = 5
        print("please pay $5")
    elif age<=18:
        bill = 7
        print("please pay $7")
    else:
        bill = 12
        print("please pay $12")
        
    wants_to_take_photo = input("do you want to take a photo? Y or N  ")
    if wants_to_take_photo == "Y":
        bill += 3
        print("please pay $3")
        
    print(f"your final bill is ${bill}")
    
else:
    print("sorry, you can't ride the safari rollercoster")