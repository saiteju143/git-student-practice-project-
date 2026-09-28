students=[]
def add_student(name):
    if not name.strip():
        print("student name cannot be empty")
        return
    if name in students:
        print("students cannot be duplicated")
        return
    students.append(name)
def show_students():
    print("Students:")
    for student in students:
        print(student)

add_student("sai")
add_student("teju")
add_student("teju")

show_students()