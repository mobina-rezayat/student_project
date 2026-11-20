from student.grades import average, max_grade, min_grade
from student.status import student_status
name = input("Enter student name: ")
grades = []
n = int(input("How many grades? "))
for i in range(n):
    x = float(input("Enter grade: "))
    grades.append(x)
avg = average(grades)
maximum = max_grade(grades)
minimum = min_grade(grades)
status = student_status(avg)
print("Student:", name)
print("Grades:", grades)
print("Average:", avg)
print("Max:", maximum)
print("Min:", minimum)
print("Status:", status)
