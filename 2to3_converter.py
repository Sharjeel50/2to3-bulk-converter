import sys
import subprocess
import tkinter as tk
from tkinter import filedialog
from subprocess import Popen, PIPE

class bulk_2to3_converter:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x350") 
        self.ListBox = tk.Listbox(self.master, width=70, height=15)
        self.ListBox.pack()
        self.Convert = tk.Button(self.master, text="Convert", command=self.ConvertFiles).pack()
        self.Files = tk.Button(self.master, text="Files", command=self.FindFiles).pack()
        
        self.Path_2to3 = sys.executable[:-11] + "Scripts"

    def ConvertFiles(self):
        for i, data in enumerate(self.ListBox.get(0, 'end')):
            cmdCommand = '''cd "{}" && 2to3.exe -w "{}"'''.format(self.Path_2to3, data)
            print(cmdCommand)
            process = subprocess.Popen(
                cmdCommand, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            print(output, error)

    def FindFiles(self):
        files = filedialog.askopenfilenames()
        for i in list(files):
            self.ListBox.insert('end', i)

def main():
    root = tk.Tk()
    a = bulk_2to3_converter(root)
    root.mainloop()
    

if __name__ == '__main__':
    main()
