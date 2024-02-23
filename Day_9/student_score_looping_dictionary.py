student_score = {
    "Dillep" : 78,
    "Harshith": 67,
    "Divya": 89,
    "Archana": 79
}

student_grade = {}
for student in student_score:
    score = student_score[student]
    
    if score >= 85:
        student_grade[student] = "outstanding"
    elif score >75 and score <85:
        student_grade[student] = "avg"
        
    else:
        student_grade[student] = "Need to improve"
    
   




print(student_grade)