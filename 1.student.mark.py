students = []
courses = []
marks = {}
def add_students():
    count = int(input("enter the number of students: "))
    for _ in range(count):                                                                      
        student_id = input("input id: ")
        student_name = input("input name: ")
        dob = input("input date of birth: ")
        students.append( {"id" : student_id, "name" : student_name, "dob" : dob})

def add_cources():
    count = int(input("enter the number of cources: "))
    for _ in range(count):
        id = input("input cource id: ")
        name = input("input cource name: ")
        courses.append({"id":id, "name":name})

def input_marks():
    course_id = input("input cource id to input mark: ")
    found = False
    for cource in courses:
        if (cource["id"]==course_id):
            found = True
            break
    if found == False:
        print("course not found")
        return
    if course_id not in marks:
        marks[course_id] = {}
    student_id = input("input student id to enter mark (type 0 to enter mark for all students): ")
    if ( student_id == "0"):
        for student in students:
            mark = input(f"enter mark for student {student["name"]} , (id: {student["id"]}): ")
            marks[course_id][student["id"]] = mark
    else:
        found = False
        for student in students:
            if student["id"] == student_id:
                mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
                marks[course_id][student["id"]] = mark
                found = True
                break
        if not found:
            print(f"Student ID {student_id} not found!")
def list_students():
    print("\nStudents:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def list_courses():
    print("\nCourses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def show_marks():
    course_id = input("Enter course ID to view marks: ")
    if course_id not in marks:
        print("No marks available for this course!")
        return
    
    print(f"\nMarks for course {course_id}:")
    for student_id, mark in marks[course_id].items():
        student_name = next(student["name"] for student in students if student["id"] == student_id)
        print(f"Student: {student_name} (ID: {student_id}), Mark: {mark}")
def main():
    while True:
        print("1. Add students")
        print("2. Add courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_students()
        elif choice == "2":
            add_cources()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()
    