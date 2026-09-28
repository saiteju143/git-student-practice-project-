students=[]
def add_student(name):
    students.append(name)
def show_students():
    print("Students:")
    for student in students:
        print(student)
def search_student(name):
    for student in students:
        if student.lower()==name.lower():
            return student
    return None

add_student("Teju")
add_student("Rahul")
add_student("Anita")

show_students()

result=search_student("teju")
if result:
    print("Student found:",result)
else:
    print("student not found")


