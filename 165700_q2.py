# Class representing a student
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Dictionary to store assignments and grades

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' with grade {grade} added for {self.name}.")

    def display_grades(self):
        if not self.assignments:
            print(f"{self.name} has no grades recorded.")
        else:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")

# Class representing an instructor
class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # List to store students in the course

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student '{student.name}' added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                return
        print(f"Student with ID {student_id} not found in the course.")

    def display_all_students_and_grades(self):
        if not self.students:
            print("No students enrolled in the course.")
        else:
            print(f"Students and grades for course '{self.course_name}':")
            for student in self.students:
                print(f"\nStudent: {student.name} (ID: {student.student_id})")
                student.display_grades()

# Sample students
student1 = Student("John Doe", "S001")
student2 = Student("Jane Smith", "S002")

# Sample instructor
instructor = Instructor("Dr. Alice", "Introduction to Programming")

# Interactive menu function
def menu():
    while True:
        print("\nCourse Management System Menu")
        print("1. Add Student")
        print("2. Assign Grade to Student")
        print("3. Display All Students and Grades")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter the student's name: ")
            student_id = input("Enter the student's ID: ")
            new_student = Student(name, student_id)
            instructor.add_student(new_student)

        elif choice == '2':
            student_id = input("Enter the student ID to assign a grade: ")
            assignment_name = input("Enter the assignment name: ")
            grade = input("Enter the grade: ")
            try:
                grade = float(grade)
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid grade input. Please enter a numeric value.")

        elif choice == '3':
            instructor.display_all_students_and_grades()

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")

# Run the menu function to start the program
menu()
