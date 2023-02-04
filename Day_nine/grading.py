student_score = {
    'Allen': 56,
    'Alice': 90,
    'Ben': 99,
}

student_grade = {}

for student in student_score:
    score = student_score[student]
    if score > 90:
        student_score[student] = "Outstanding"
    elif score > 80:
        student_score[student] = "Exceed Expectations"
    elif score > 70:
        student_score[student] = 'Acceptable'
    else:
        student_score[student] = "Fail"     


print(student_score)               