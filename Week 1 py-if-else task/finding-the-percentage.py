def average_marks(student_marks, query_name):
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print("{:.2f}".format(average))

if __name__ == '__main__':
    n = int(input("Enter number of Students: "))
    student_marks = {}
    print(f"Enter {n} student names and their marks: ")

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the name of student to query: ")
    average_marks(student_marks, query_name)