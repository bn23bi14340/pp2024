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