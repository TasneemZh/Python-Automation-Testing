class Student:
    def __init__(self, name, student_id, major, dob):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.dob = dob
        self.courses = []

    def register_course(self, course):
        course.add_student(self)
        self.courses.append(course)

    def get_student_info(self):
        return {
            "name": self.name,
            "major": self.major,
            "student_id": self.student_id,
            "dob": self.dob
        }

    def get_registered_courses(self):
        reg_courses = []
        course_students = []
        for course in self.courses:
            for student in course.students:
                course_students.append({
                    "name": student.name,
                    "student_id": student.student_id
                })

        for course in self.courses:
            reg_courses.append({
                "name": course.name,
                "number_of_hours": course.number_of_hours,
                "teacher": {"name": course.teacher.name, "teacher_id": course.teacher.teacher_id},
                "students": course_students
            })
        return reg_courses
