from admission import Admission
from highschool import HighSchoolStudent
from countryside import CountrysideStudent

class AdmissionProgram:
    def __init__(self):
        name = input("Enter admission officer's name: ")
        accept_grade = int(input("Enter the acceptance grade: "))
        self.admission = Admission(name, accept_grade)
    
    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = input("Enter your choice: ")
            if   choice == '1': self.__add_student()
            elif choice == '2': self.__show_all_students()
            elif choice == '3': self.__inform_student()
            elif choice == '4': running = False
            else: print("Invalid choice, please try again.")

    def __print_menu(self):
        print("\n--- Admission Program Menu ---")
        print("1. Add a student")
        print("2. Show all students")
        print("3. Inform a student about admission status")
        print("4. Exit")

    def __add_student(self):
        print("\n--- Add a Student ---")
        print("1. Regular student")
        print("2. Countryside student")
        choice = input("Choose student type (1 or 2): ")
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        avg_grade = float(input("Enter student's average grade: "))

        if choice == '2':
            addition = float(input("Enter countryside addition (0-20): "))
            student = CountrysideStudent(name, age, avg_grade, addition)
        else:
            student = HighSchoolStudent(name, age, avg_grade)

        self.admission.add_student(student)

    def __show_all_students(self):
        print("\n--- All Students ---")
        self.admission.show_all()

    def __inform_student(self):
        print("\n--- Inform a Student ---")
        index = int(input("Enter student index (0-based): "))
        self.admission.inform(index)

if __name__ == '__main__':
    program = AdmissionProgram()
    program.run()
    print("Thank you for using the Admission Program!")