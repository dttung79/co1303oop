from tkinter import *
from tkinter import messagebox as mb
from base_gui import BaseGUI
from student import Student, NameValueError, AgeValueError, GPAValueError
from tkinter.filedialog import asksaveasfilename as open_save

class StudentGUI(BaseGUI):
    def __init__(self):
        super().__init__(title="Student Management", width=300, height=200)
    
    # override _create_widgets method
    def _create_widgets(self):
        lbl_title = Label(self.window, text="Add Student Dialog")
        lbl_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=EW)

        lbl_name = Label(self.window, text="Name:")
        lbl_name.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        self.name_var = StringVar()
        txt_name = Entry(self.window, textvariable=self.name_var)
        txt_name.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        lbl_age = Label(self.window, text="Age:")
        lbl_age.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        self.age_var = IntVar()
        txt_age = Entry(self.window, textvariable=self.age_var)
        txt_age.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        lbl_gpa = Label(self.window, text="GPA:")
        lbl_gpa.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        self.gpa_var = DoubleVar()
        txt_gpa = Entry(self.window, textvariable=self.gpa_var)
        txt_gpa.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        btn_submit = Button(self.window, text="Submit", command=self.add_student)
        btn_submit.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky=E)
    
    def add_student(self):
        name = self.name_var.get()
        age = self.age_var.get()
        gpa = self.gpa_var.get()

        try:
            student = Student(name, age, gpa)
            
            file_name = open_save(filetypes=[("CSV files", "*.csv")])
            with open(file_name, 'a') as file:
                file.write(f"\n{student.name},{student.age},{student.gpa}")
                mb.showinfo("Success", "Student added successfully!")
        except NameValueError as ne:
            mb.showerror("Name Error", str(ne))
        except AgeValueError as ae:
            mb.showerror("Age Error", str(ae))
        except GPAValueError as ge:
            mb.showerror("GPA Error", str(ge))
        except Exception as e:
            mb.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    gui = StudentGUI()
    gui.run()