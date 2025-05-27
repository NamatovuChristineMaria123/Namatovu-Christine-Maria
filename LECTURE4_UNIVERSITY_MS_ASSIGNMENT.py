
class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}, ID: {self.id_number}')


class Student(Person):
    def __init__(self, name, age, id_number, course, grades=None):
        super().__init__(name, age, id_number)
        self.course = course
        self.grades = grades if grades else []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f'Added grade {grade} for {self.name}')

    def calculate_gpa(self):
        if not self.grades:
            return 0
        gpa = sum(self.grades) / len(self.grades)
        return round(gpa, 2)

    def display_info(self):
        super().display_info()
        print(f'Course: {self.course}, GPA: {self.calculate_gpa()}')


class Lecturer(Person):
    def __init__(self, name, age, id_number, department, salary):
        super().__init__(name, age, id_number)
        self.department = department
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f'Department: {self.department}, Salary: Shs{self.salary}')


class Staff(Person):
    def __init__(self, name, age, id_number, role, working_hours):
        super().__init__(name, age, id_number)
        self.role = role
        self.working_hours = working_hours

    def display_info(self):
        super().display_info()
        print(f'Role: {self.role}, Working Hours: {self.working_hours}')




student1 = Student("Christine Maria", 22, "STU2300", "Computer Science", [3.5, 3.7, 4.0])
lecturer1 = Lecturer("Dr. Jeff", 35, "LEC2001", "Networks", 750000)
staff1 = Staff("Nassiwa Hafswa", 38, "STF001", "Administrator", "9am-5pm")

# Using methods

print("Student Info:")
student1.display_info()
student1.add_grade(3.9)
print(f'Updated GPA: {student1.calculate_gpa()}')

print("\nLecturer Info:")
lecturer1.display_info()

print("\nStaff Info:")
staff1.display_info()
