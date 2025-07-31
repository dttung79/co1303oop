from highschool import HighSchoolStudent

class Admission:
    # static variable for accept_grade
    accept_grade = 60
    def __init__(self, name, accept_grade):
        self.name = name
        self.__students = []
        Admission.accept_grade = accept_grade
    
    @property
    def name(self):
        return self.__name  # private attribute
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be empty")
        self.__name = value  # private attribute
    
    def add_student(self, s):
        self.__students.append(s)

    def show_all(self):
        for s in self.__students:
            print(s)

    def inform(self, index):
        student = self.__students[index]
        print(f'Hi {student.name}\nI am {self.name}, the admission officer.')
        if student.is_accepted(Admission.accept_grade):
            print(f'I am happy to inform that you are accepted to our school.')
        else:
            print(f'Sorry, you are not accepted to our school.')


if __name__ == '__main__':
    johh = Admission('John', 70)
    print(f'Admission name: {johh.name}, Accept grade: {johh.accept_grade}')

    paul = Admission('Paul', 80)
    print(f'Admission name: {paul.name}, Accept grade: {paul.accept_grade}')
    print(f'Admission name: {johh.name}, Accept grade: {johh.accept_grade}')