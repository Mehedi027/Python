# def life_in_weeks(age):
#     years_left = 90 - age
#     weeks_left = years_left * 52
#     print(f"You have {weeks_left} weeks left.")
#
# age = int(input ("What is your current age"))
# life_in_weeks(age)

#how to use max function
#fruits = {"apple": 2, "Peer": 4, "Orange":9}
#max(fruits, key=fruits.get)

student_score = {
    'harry' : 88,
    'Ron' : 78,
    'Hermonie' : 95,
    'Draco' : 75,
    'Neville' : 60,
}

student_grades = {}
for key in student_score:
    if 91 < student_score[key] < 100:
        student_grades[key] = "Outstanding"
    elif 81 < student_score[key] < 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 < student_score[key] < 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)