from tkinter import *
from tkinter import messagebox as mb
from base_gui import BaseGUI
from fruit import Fruit  
class DemoApp04(BaseGUI):
    def __init__(self):
        super().__init__(title="Demo GUI 04", width=600, height=300)

    def _create_widgets(self):
        lbl_fruits = Label(self.window, text="List of fruits:")
        lbl_fruits.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        btn_load = Button(self.window, text="Load", command=self.__btn_load_click)
        btn_load.grid(row=0, column=1, padx=5, pady=5, sticky=E)

        self.lst_fruits = Listbox(self.window, width=30, height=10, selectmode=SINGLE, 
                                                                    exportselection=FALSE)
        self.lst_fruits.grid(row=1, column=0, columnspan=2, rowspan=3, padx=5, pady=5, sticky=W)
        self.lst_fruits.bind("<<ListboxSelect>>", self.__lst_fruits_selected)

        lbl_fruit = Label(self.window, text="Fruit:")
        lbl_fruit.grid(row=1, column=2, padx=5, pady=5, sticky=E)

        self.fruit = StringVar()
        txt_fruit = Entry(self.window, width=15, textvariable=self.fruit)
        txt_fruit.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        lbl_quantity = Label(self.window, text="Quantity:")
        lbl_quantity.grid(row=2, column=2, padx=5, pady=5, sticky=E)

        self.quantity = StringVar()
        txt_quantity = Entry(self.window, width=15, textvariable=self.quantity)
        txt_quantity.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        lbl_price = Label(self.window, text="Price:")
        lbl_price.grid(row=3, column=2, padx=5, pady=5, sticky=E)

        self.price = StringVar()
        txt_price = Entry(self.window, width=15, textvariable=self.price)
        txt_price.grid(row=3, column=3, padx=5, pady=5, sticky=W)

    def __btn_load_click(self):
        # create some fruits
        apple = Fruit("Apple", 10, 1.5)
        banana = Fruit("Banana", 20, 0.5)
        orange = Fruit("Orange", 15, 1.0)
        mango = Fruit("Mango", 5, 2.0)
        # add fruits to a list
        self.fruits = [apple, banana, orange, mango]
        # clear the listbox to insert fruits
        self.lst_fruits.delete(0, END)
        for fruit in self.fruits:
            self.lst_fruits.insert(END, str(fruit))

    def __lst_fruits_selected(self, event):
        # get selected index
        index = self.lst_fruits.curselection()[0]
        # get the selected fruit
        fruit = self.fruits[index]
        self.fruit.set(fruit.name)
        self.quantity.set(fruit.quantity)
        self.price.set(fruit.price)

if __name__ == "__main__":
    app = DemoApp04()
    app.run()