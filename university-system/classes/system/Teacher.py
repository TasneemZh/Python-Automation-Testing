class Teacher:
    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def get_teacher_info(self):
        return {
            "name": self.name,
            "id": self.teacher_id
        }

    def get_courses(self):
        course_names = []
        for course in self.courses:
            course_names.append(course.name)  # might not work
        return course_names
