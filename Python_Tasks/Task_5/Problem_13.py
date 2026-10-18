## Problem 13: Nested lists

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input().strip()
        grade = float(input())
        students.append([name, grade])

    grades = sorted({student[1] for student in students})
    second_lowest = grades[1]
    names = [student[0] for student in students if student[1] == second_lowest]
    for name in sorted(names):
        print(name)
