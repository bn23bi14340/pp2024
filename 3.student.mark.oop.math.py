import math
import numpy as np
class student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0
        self.mark = np.array([])
    def __str__(self):
        return f"name: {self.name}, student ID: {self.student_id}, date of birth: {self.dob}, GPA: {self.gpa}"
class course:
    def __init__(self,course_id, name):
        self.course_id = course_id
        self.name = name
    def __str__(self):
        return f"course ID: {self.course_id}, name: {self.name}"
class school:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    def add_student(self):
        count = int(input("enter number of students: "))
        for _ in range(count):
            student_id = input("student ID: ")
            name = input("name: ")
            dob = input("enter date of birth: ")
            self.students.append(student(student_id,name,dob))
    def add_course(self):
        count = int(input("enter number of courses: "))
        for _ in range(count):
            course_id = input("course ID: ")
            name = input("course name: ")
            self.courses.append(course(course_id,name))
    def input_marks(self):
        course_id = input ("enter course ID: ")
        found = False
        for c in self.courses:
            if c.course_id == course_id:
                found = True
                break
        if found == False:
            return
        if course_id not in self.marks:
            self.marks[course_id] = {}
        student_id = input("enter student ID to enter mark (type 0 for all student): ")
        found = False
        if student_id == "0":
            for s in self.students:
                mark = float(input(f"enter mark for {s.name} (id: {s.student_id}): "))
                self.marks[course_id][s.student_id] = math.floor(mark*10)/10
                s.mark = np.append(s.mark, mark)
        else:
            for s in self.students:
                if s.student_id == student_id:
                    found = True
                    mark = float(input(f"enter mark for {s.name} (id: {s.student_id}): "))
                    self.marks[course_id][s.student_id] = math.floor(mark*10)/10
                    s.mark = np.append(s.mark, mark)
                    break
            if found == False:
                print("student not found")
    def cal_gpa(self):
        student_id = input("enter student id to calculate GPA (type 0 for all student): ")
        found = False
        if student_id == "0":
            for s in self.students:
                if len(s.mark) == 0:
                    print(f"Student {s.name} (id: {s.student_id}) has no mark yet")
                    continue
                for i in range(len(s.mark)):
                    s.gpa = s.gpa + s.mark[i]
                s.gpa = s.gpa / len(s.mark)
        else:
            for s in self.students:
                if s.student_id == student_id:
                    found = True
                    if len(s.mark) == 0:
                        print(f"Student {s.name} (id: {s.student_id}) has no mark yet")
                        return
                    for i in range(len(s.mark)):
                        s.gpa = s.gpa + s.mark[i]
                    s.gpa = s.gpa / len(s.mark)
                    break
            if found == False:
                print("student not found")
                return
        print("calculate completed")
        return
    def list_students(self):
        self.students.sort(key=lambda s: s.gpa, reverse=True)
        print("\nstudents: ")
        for s in self.students:
            print(s)
    def list_courses(self):
        print("\ncourses: ")
        for c in self.courses:
            print(c)
    def show_marks(self):
        course_id = input("enter course ID: ")
        if course_id not in self.marks:
            print("no marks for this course")
            return
        print(f"marks for course {course_id}:")
        for student_id, mark in self.marks[course_id].items():
            student = next((s for s in self.students if s.student_id == student_id), None)
            if student:
                print(f"Student: {student.name} (ID: {student.student_id}), Mark: {mark}")
    
    def menu(self):
        while True:
            print("\n1. Add students")
            print("2. Add courses")
            print("3. Input marks for a course")
            print("4. Calculate GPA")
            print("5. List students")
            print("6. List courses")
            print("7. Show marks for a course")
            print("8. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_course()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.cal_gpa()
            elif choice == "5":
                self.list_students()
            elif choice == "6":
                self.list_courses()
            elif choice == "7":
                self.show_marks()
            elif choice == "8":
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    s = school()
    s.menu()