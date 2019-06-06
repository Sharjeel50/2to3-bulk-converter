import sys
import tkinter as tk
from tkinter import filedialog


class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x300")
        self.ListBox = tk.Listbox(self.master, width = 70, height = 15)
        self.ListBox.place( x=350, y=150, anchor="center")
        self.Convert = tk.Button(self.master, text="Quit", command = self.ConvertFiles ).place( x=250, y=200, anchor="center" )
        self.Files = tk.Button(self.master, text = "Files", command = self.findFiles ).place( x=200, y=150, anchor="center" )
        self.OutputLocation = tk.Button(self.master, text = "Output", command = self.outputLocation ).place(x = 130, y = 230, anchor = "center")
        self.Path_2to3 = sys.executable + "\\Scripts\\2to3.py"
        
        
    def ConvertFiles(self):
        pass

    def findFiles(self):
        files = filedialog.askopenfilenames()
        for i in list(files):
            self.ListBox.insert('end', i)

    def outputLocation(self):
        endpoint = filedialog.askdirectory()


def main():
    root = tk.Tk()
    a = MainMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
