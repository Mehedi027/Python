""" weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi < 18.5:
    print(" underweight")
elif  bmi >= 25:
    print(" overweight")
else:
    print(" normal weight") """

""" weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi < 18.5:
    print(" underweight")
elif  bmi < 25:
    print(" normal weight")
else:
    print(" Overweight") """

height = float(input())
weight = int(input())
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif  bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print("clinically obese")