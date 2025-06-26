from tkinter import *
from abc import ABC, abstractmethod

class BaseGUI(ABC):
    def __init__(self, title="Base GUI", width=400, height=300):
        self._create_window(title, width, height)
        self._create_widgets()

    # protected method to create the main window
    def _create_window(self, title, width, height):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

    # abstract method to create widgets, must be implemented by subclasses
    @abstractmethod
    def _create_widgets(self):
        pass

    def run(self):
        self.window.mainloop()