class Student(object):
    def __init__(self, name, grade_point_average):
        self.name = name
        self.grade_point_average = grade_point_average

    def __lt__(self, other):
        return self.name < other.name


students = [Student('D', 3.5), Student(
    'C', 3.7), Student('A', 4.0), Student('B', 3.2)]
print([(student.name, student.grade_point_average) for student in sorted(students)])
students.sort(key=lambda student: student.grade_point_average)
print([(student.name, student.grade_point_average)
       for student in students])
