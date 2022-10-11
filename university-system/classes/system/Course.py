class Course:
    def __init__(self, name, number_of_hours, teacher):
        self.name = name
        self.number_of_hours = number_of_hours
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_course_info(self):
        return {
            "name": self.name,
            "number_of_hours": self.number_of_hours
        }

    def get_students(self):
        return self.students

    def get_teacher(self):
        return self.teacher
