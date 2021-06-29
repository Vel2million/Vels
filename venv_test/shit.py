class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        self.average_grade = self._get_average_grade()

    def _get_average_grade(self):
        return sum(self.grades) / len(self.grades)
        
    def introduce_self(self):
        print(f"Hello, my name is {self.name}")


student = Student("John", (90, 90, 93, 80, 78))

student.get_average_grade()