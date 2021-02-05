num = int(input())

students_dict = {}

for _ in range(num):
    student_name, student_grade = input().split()
    student_grade = float(student_grade)
    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(f"{student_grade:.2f}")

for student in students_dict.keys():
    average_grade = sum(float(el) for el in students_dict[student]) / len(students_dict[student])
    print(f"{student} -> {' '.join(students_dict[student])} (avg: {'{0:.2f}'.format(average_grade)})")
