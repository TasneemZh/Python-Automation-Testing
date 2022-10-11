from classes.system.Course import Course
from classes.system.Student import Student
from classes.system.Teacher import Teacher

if __name__ == '__main__':
    # Create 3 teachers, and print teacher info for each one
    teacher1 = Teacher("Sam", "1")
    teacher2 = Teacher("Jack", "2")
    teacher3 = Teacher("Ron", "3")
    print(teacher1.get_teacher_info())
    print(teacher2.get_teacher_info())
    print(teacher3.get_teacher_info())

    print("===================================")

    # Create 6 courses and assign 2 courses for each teacher
    course1 = Course("Math", "25", teacher1)
    course2 = Course("Arabic", "30", teacher1)
    course3 = Course("Science", "40", teacher3)
    course4 = Course("English", "65", teacher3)
    course5 = Course("Hebrew", "10", teacher2)
    course6 = Course("Poems", "5", teacher2)

    teacher1.add_course(course1)
    teacher1.add_course(course2)
    teacher3.add_course(course3)
    teacher3.add_course(course4)
    teacher2.add_course(course5)
    teacher2.add_course(course6)

    # Print course information for each course
    print(course1.get_course_info())
    print(course2.get_course_info())
    print(course3.get_course_info())
    print(course4.get_course_info())
    print(course5.get_course_info())
    print(course6.get_course_info())

    print("===================================")

    # Print course names for each teacher
    print(teacher1.get_courses())
    print(teacher2.get_courses())
    print(teacher3.get_courses())

    # Create 5 students
    student1 = Student("Fadia", "10", "Computer Science", "1999-09-10")
    student2 = Student("Rana", "11", "Networking", "1998-03-05")
    student3 = Student("Samia", "12", "Cyber Security", "1996-11-09")
    student4 = Student("Lama", "13", "Translator", "2000-01-17")
    student5 = Student("Sara", "14", "Computer Engineering", "1997-08-12")

    # Register each student in one or more courses
    student1.register_course(course1)
    student2.register_course(course3)
    student3.register_course(course5)
    student4.register_course(course2)
    student5.register_course(course4)

    print("===================================")

    # Print student info for each student
    print(student1.get_student_info())
    print(student2.get_student_info())
    print(student3.get_student_info())
    print(student4.get_student_info())
    print(student5.get_student_info())

    print("===================================")

    # Print registered courses for each student
    print(student1.get_registered_courses())
    print(student2.get_registered_courses())
    print(student3.get_registered_courses())
    print(student4.get_registered_courses())
    print(student5.get_registered_courses())
