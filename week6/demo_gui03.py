from tkinter import *
from tkinter import messagebox as mb
from base_gui import BaseGUI

class DemoApp03(BaseGUI):
    def __init__(self):
        super().__init__(title="Demo GUI 03", width=400, height=300)
    
    # override the _create_widgets method from BaseGUI
    def _create_widgets(self):
        lbl_stays = Label(self.window, text="Stays:")
        lbl_stays.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        self.stays = StringVar()
        txt_stays = Entry(self.window, width=20, textvariable=self.stays)
        txt_stays.grid(row=0, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        lbl_price = Label(self.window, text="Price:")
        lbl_price.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        self.price = StringVar()
        txt_price = Entry(self.window, width=20, textvariable=self.price)
        txt_price.grid(row=1, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        lbl_weekend = Label(self.window, text="Weekend:")
        lbl_weekend.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        self.weekend = IntVar()
        self.weekend.set(0)  # default value for weekend is No (0)
        rd_weekend_yes = Radiobutton(self.window, text="Yes", variable=self.weekend, value=1)
        rd_weekend_yes.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        rd_weekend_no = Radiobutton(self.window, text="No", variable=self.weekend, value=0)
        rd_weekend_no.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        lbl_breakfast = Label(self.window, text="Breakfast:")
        lbl_breakfast.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        self.breakfast = BooleanVar()
        self.breakfast.set(False)
        chk_breakfast = Checkbutton(self.window, text="Breakfast", variable=self.breakfast)
        chk_breakfast.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        self.airport_transfer = BooleanVar()
        self.airport_transfer.set(False)
        chk_airport_transfer = Checkbutton(self.window, text="Airport Transfer", 
                                                        variable=self.airport_transfer)
        chk_airport_transfer.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        btn_calculate = Button(self.window, text="Calculate Bill", command=self.__btn_calculate_click)
        btn_calculate.grid(row=5, column=1, padx=5, pady=5, sticky=W)
    
    def __btn_calculate_click(self):
        try:
            stays = int(self.stays.get())
            price = float(self.price.get())

            total = stays * price
        except ValueError:
            mb.showerror("Input Error", "Please enter valid numbers for stays and price.")
            return

        weekend = self.weekend.get()    # 1 for Yes, 0 for No
        if weekend == 1:
            total *= 1.2    # 20% surcharge for weekend stays
        
        breakfast = self.breakfast.get()
        if breakfast:
            total += 5 * stays
        
        airport_transfer = self.airport_transfer.get()
        if airport_transfer:
            total += 20
        
        message = f"Total Bill: ${total:.2f}"
        mb.showinfo("Total Bill", message)


if __name__ == "__main__":
    app = DemoApp03()
    app.run()