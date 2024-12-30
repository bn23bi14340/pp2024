class course:
    def __init__(self,course_id, name):
        self.course_id = course_id
        self.name = name
    def __str__(self):
        return f"course ID: {self.course_id}, name: {self.name}"