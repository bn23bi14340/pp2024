from input import students, courses, marks 
def list_students():
        students.sort(key=lambda s: s.gpa, reverse=True)
        print("\nstudents: ")
        for s in students:
            print(s)
def list_courses():
        print("\ncourses: ")
        for c in courses:
            print(c)
def show_marks():
        course_id = input("enter course ID: ")
        if course_id not in marks:
            print("no marks for this course")
            return
        print(f"marks for course {course_id}:")
        for student_id, mark in marks[course_id].items():
            student = next((s for s in students if s.student_id == student_id), None)
            if student:
                print(f"Student: {student.name} (ID: {student.student_id}), Mark: {mark}")
