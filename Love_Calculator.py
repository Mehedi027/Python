print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# names = ["name1", "name2"]
total1 = 0
total2 = 0
t = "true"
l = "love"
for letter in name1:
    if letter in t:
        total1 += 1
    if letter in l:
        total2 += 1

for letter in name2:

    if letter in t:
        total1 += 1
    if letter in l:
        total2 += 1
sum = (total1 * 10 + total2)
if 10 > sum > 90:
    print(f'Your score is {sum}, you go together like coke and mentos.')
elif 40 >= sum <= 50:
    print(f'Your score is {sum}, you are alright together.')
else:
    print(f'Your score is {sum}.')