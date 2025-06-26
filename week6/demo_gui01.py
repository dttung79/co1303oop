from tkinter import *
from tkinter import messagebox as mb

class DemoApp01:
    def __init__(self):
        # create window
        self.__create_window()
        # create widgets
        self.__create_widgets()

    def __create_window(self):
        self.window = Tk()
        self.window.title("Demo GUI 01")
        self.window.geometry("400x300")

    def __create_widgets(self):
        # create a label
        self.lbl_hello = Label(self.window, text="Hello, World!")
        self.lbl_hello.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        # create a text box
        self.txt_hello = Entry(self.window, width=30)
        self.txt_hello.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        # create a button
        self.btn_hello = Button(self.window, text="Click Me", command=self.__btn_hello_click)
        self.btn_hello.grid(row=2, column=0, padx=5, pady=5, sticky=W)

    # event handler for button click (name of widget + _ + name of event)
    def __btn_hello_click(self):
        # get text from label
        message = self.lbl_hello.cget("text")
        mb.showinfo("Information", message)
        # set text in text box
        self.txt_hello.delete(0, END)       # delete current text (from 0 to END)
        self.txt_hello.insert(0, message)   # insert new text (at position 0)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = DemoApp01()
    app.run()