from tkinter import *
from tkinter import messagebox as mb

class DemoApp02:
    def __init__(self):
        # create window
        self.__create_window()
        # create widgets
        self.__create_widgets()

    def __create_window(self):
        self.window = Tk()
        self.window.title("Demo GUI 02")
        self.window.geometry("400x300")

    def __create_widgets(self):
        lbl_firstname = Label(self.window, text="First Name:")
        lbl_firstname.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.first_name = StringVar()    # create a StringVar to hold the first name
        # create a text box then bind it to the StringVar first_name
        txt_firstname = Entry(self.window, width=30, textvariable=self.first_name)   
        txt_firstname.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        lbl_lastname = Label(self.window, text="Last Name:")
        lbl_lastname.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
        self.last_name = StringVar()     # create a StringVar to hold the last name
        # create a text box then bind it to the StringVar last_name
        txt_lastname = Entry(self.window, width=30, textvariable=self.last_name)
        txt_lastname.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        btn_merge = Button(self.window, text="Merge", command=self.__btn_merge_click)
        btn_merge.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        lbl_fullname = Label(self.window, text="Full Name:")
        lbl_fullname.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.full_name = StringVar()      # create a StringVar to hold the full name
        txt_fullname = Entry(self.window, width=30, textvariable=self.full_name)
        txt_fullname.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    def __btn_merge_click(self):
        first_name = self.first_name.get()  # get what the user entered in the first name text box
        last_name = self.last_name.get()    # get what the user entered in the last name text box
        full_name = f"{first_name} {last_name}"
        self.full_name.set(full_name)       # set the full name in the full name text box

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = DemoApp02()
    app.run()