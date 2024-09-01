import random
letters  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
print("Welcome to the password Generator")
number_of_letters  = int(input("How many letters would you like to your password\n"))
number_of_symbnols = int(input("How many symbol would you like to your password\n"))
number_of_numbers = int(input("How many numbers would you like to your password\n"))
password_list = []



for  char in range(0, number_of_letters):
       password_list.append(random.choice(letters))

for  char in range(0, number_of_symbnols):
       password_list.append(random.choice(symbols))

for  char in range(0, number_of_numbers):
       password_list.append(random.choice(numbers))

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your New password is: {password}")

