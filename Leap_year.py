leapyear = int(input("Enter Year to check LeapYear"))
if (leapyear % 4 == 0 and leapyear % 100 != 0) or (leapyear % 400 == 0):
    print(leapyear,"is a leap year")
else:
    print(leapyear,"is not a leap year")
