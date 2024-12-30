from domain.course import course
from domain.student import student
import math
import numpy as np
students = []
courses = []
marks = {}
def add_student():
        count = int(input("enter number of students: "))
        for _ in range(count):
            student_id = input("student ID: ")
            name = input("name: ")
            dob = input("enter date of birth: ")
            students.append(student(student_id,name,dob))
def add_course():
        count = int(input("enter number of courses: "))
        for _ in range(count):
            course_id = input("course ID: ")
            name = input("course name: ")
            courses.append(course(course_id,name))
def input_marks():
        course_id = input ("enter course ID: ")
        found = False
        for c in courses:
            if c.course_id == course_id:
                found = True
                break
        if found == False:
            return
        if course_id not in marks:
            marks[course_id] = {}
        student_id = input("enter student ID to enter mark (type 0 for all student): ")
        found = False
        if student_id == "0":
            for s in students:
                mark = float(input(f"enter mark for {s.name} (id: {s.student_id}): "))
                marks[course_id][s.student_id] = math.floor(mark*10)/10
                s.mark = np.append(s.mark, mark)
        else:
            for s in students:
                if s.student_id == student_id:
                    found = True
                    mark = float(input(f"enter mark for {s.name} (id: {s.student_id}): "))
                    marks[course_id][s.student_id] = math.floor(mark*10)/10
                    s.mark = np.append(s.mark, mark)
                    break
            if found == False:
                print("student not found")
def cal_gpa():
        student_id = input("enter student id to calculate GPA (type 0 for all student): ")
        found = False
        if student_id == "0":
            for s in students:
                if len(s.mark) == 0:
                    print(f"Student {s.name} (id: {s.student_id}) has no mark yet")
                    continue
                for i in range(len(s.mark)):
                    s.gpa = s.gpa + s.mark[i]
                s.gpa = s.gpa / len(s.mark)
        else:
            for s in students:
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