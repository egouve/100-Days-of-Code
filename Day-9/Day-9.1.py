#Criar um dicionário que substitua as notas por:

#Scores 91 - 100: Grade = "Outstanding"

#Scores 81 - 90: Grade = "Exceeds Expectations"

#Scores 71 - 80: Grade = "Acceptable"

#Scores 70 or lower: Grade = "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = 'Outstanding'
    elif student_scores[student] > 80 and student_scores[student] <= 90:
        student_grades[student] = 'Exceeds Expectations'
    elif student_scores[student] > 70 and student_scores[student] <= 80:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)