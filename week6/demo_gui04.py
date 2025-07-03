from tkinter import *
from tkinter import messagebox as mb
from base_gui import BaseGUI
from fruit import Fruit  
from tkinter.filedialog import askopenfilename, asksaveasfilename
import csv

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

        btn_save = Button(self.window, text="Save", command=self.__btn_save_click)
        btn_save.grid(row=4, column=1, padx=5, pady=5, sticky=E)

        lbl_fruit = Label(self.window, text="Fruit:")
        lbl_fruit.grid(row=1, column=2, padx=5, pady=5, sticky=E)

        self.fruit = StringVar()
        txt_fruit = Entry(self.window, width=20, textvariable=self.fruit)
        txt_fruit.grid(row=1, column=3, columnspan=3, padx=5, pady=5, sticky=W)

        lbl_quantity = Label(self.window, text="Quantity:")
        lbl_quantity.grid(row=2, column=2, padx=5, pady=5, sticky=E)

        self.quantity = StringVar()
        txt_quantity = Entry(self.window, width=20, textvariable=self.quantity)
        txt_quantity.grid(row=2, column=3, columnspan=3, padx=5, pady=5, sticky=W)

        lbl_price = Label(self.window, text="Price:")
        lbl_price.grid(row=3, column=2, padx=5, pady=5, sticky=E)

        self.price = StringVar()
        txt_price = Entry(self.window, width=20, textvariable=self.price)
        txt_price.grid(row=3, column=3, columnspan=3, padx=5, pady=5, sticky=W)

        btn_add = Button(self.window, text="Add", command=self.__btn_add_click)
        btn_add.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        btn_edit = Button(self.window, text="Edit", command=self.__btn_edit_click)
        btn_edit.grid(row=4, column=4, padx=5, pady=5, sticky=W)

        btn_del = Button(self.window, text="Del", command=self.__btn_del_click)
        btn_del.grid(row=4, column=5, padx=5, pady=5, sticky=W)
    
    def __btn_add_click(self):
        name = self.fruit.get()
        if not name:  # check if name is empty
            mb.showerror("Error", "Fruit name cannot be empty!")
            return
        try:
            quantity = int(self.quantity.get())
            price = float(self.price.get())
        except ValueError as e:  # check if quantity or price is not a number
            mb.showerror("Error", "Quantity and Price must be numbers!")
            return

        f = Fruit(name, quantity, price)  # create a fruit object
        self.fruits.append(f)  # add fruit to the list
        self.lst_fruits.insert(END, str(f))  # add fruit to the listbox

        mb.showinfo("Success", "Fruit added successfully!")

    def __btn_edit_click(self):
        try:
            selected_index = self.lst_fruits.curselection()[0]
            fruit = self.fruits[selected_index]  # get the selected fruit
            # get new values from the entry fields
            name = self.fruit.get()
            quantity = int(self.quantity.get())
            price = float(self.price.get())
        except IndexError:  # no fruit selected
            mb.showerror("Error", "No fruit selected!")
            return
        except ValueError:  # invalid input for quantity or price
            mb.showerror("Error", "Quantity and Price must be numbers!")
            return
        # update the fruit object
        fruit.name = name
        fruit.quantity = quantity
        fruit.price = price
        # update the listbox
        self.lst_fruits.delete(selected_index)
        self.lst_fruits.insert(selected_index, str(fruit))
        mb.showinfo("Success", "Fruit updated successfully!")

    def __btn_del_click(self):
        # get the selected index
        try:
            selected_index = self.lst_fruits.curselection()[0]
        except IndexError:  # no fruit selected
            mb.showerror("Error", "No fruit selected!")
            return

        # delete the selected fruit from the list and listbox
        del self.fruits[selected_index]  # remove from the list
        self.lst_fruits.delete(selected_index)  # remove from the listbox

        # show a success message
        mb.showinfo("Success", "Fruit deleted successfully!")

    def __btn_load_click(self):
        fruit_file = askopenfilename(filetypes=[("CSV files", "*.csv"),   # file type for csv
                                                ("All files", "*.*")])    # all other types
        if not fruit_file:
            mb.showerror("Error", "No file selected!")
            return
        self.fruits = []    # clear the list of fruits
        self.lst_fruits.delete(0, END)  # clear the listbox
        with open(fruit_file, mode='r') as fr:
            reader = csv.reader(fr)
            next(reader)    # skip the header row
            for row in reader:
                name = row[0].strip()  # get the fruit name
                quantity = int(row[1].strip())
                price = float(row[2].strip())
                # create a fruit object
                fruit = Fruit(name, quantity, price)
                # add the fruit to the list & listbox
                self.fruits.append(fruit)
                self.lst_fruits.insert(END, str(fruit))  # insert fruit to listbox
        
        mb.showinfo("Success", "Fruits loaded successfully!")

    def __btn_save_click(self):
        fruit_file = asksaveasfilename(defaultextension=".csv",             # default file extension
                                       filetypes=[("CSV files", "*.csv"),   # file type for csv
                                                  ("All files", "*.*")])    # all other types
        # check if a file was selected
        if not fruit_file: 
            mb.showerror("Error", "No file selected!")
            return
        
        with open(fruit_file, mode='w', newline='') as fw:
            writer = csv.writer(fw)
            # write header
            writer.writerow(["Fruit", "Quantity", "Price"])
            # write data
            for fruit in self.fruits:
                writer.writerow([fruit.name, fruit.quantity, fruit.price])
        
        mb.showinfo("Success", "Fruits saved successfully!")

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