print("Welcome to the rollercoster")
height = int(input("what is your height in CM?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoster")
    Age = int(input("What is your age?"))

    if Age < 12:
        bill = 5
        print("Please pay 5 Euro")
    elif Age >= 12 and Age <= 18:
        bill = 7
        print("Please pay 7 Euro")
    else:
            
        if Age <= 45  and Age <= 55:
            bill = 0
            print("Thank you for your visit you do not have to pay")
        else:
            bill = 12
            print("Please pay 12 Euro")

    Photo = input("Do you need a photo during ride?")
    if Photo == "yes":
       print("Your total bill is:", bill + 3, "Euro")
    else:
        print("No extra charge please pay only", bill, "Euro")
else:
    print("You are too short to ride the rollercoster")
