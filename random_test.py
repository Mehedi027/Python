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



# student_score = {
#     'harry' : 88,
#     'Ron' : 78,
#     'Hermonie' : 95,
#     'Draco' : 75,
#     'Neville' : 60,
# }
#
# student_grades = {}
# for key in student_score:
#     if 91 < student_score[key] < 100:
#         student_grades[key] = "Outstanding"
#     elif 81 < student_score[key] < 90:
#         student_grades[key] = "Exceeds Expectations"
#     elif 71 < student_score[key] < 80:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
#
# print(student_grades)


#joining function
# def function1(text):
#     return text + text
#
# def function2(text):
#     return text.title()
#
# output = function2(function1("hello"))
# print(output)



#use of **return**
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did no provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name  = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is yopur last name?")))