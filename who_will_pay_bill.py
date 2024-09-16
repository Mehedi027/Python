import random
names = input("enter your names separtating by comma")
names  = []
count = len(names)
choice = random.randint(0,count-1)

print(f"{names[choice]} is going to buy the meal today!")