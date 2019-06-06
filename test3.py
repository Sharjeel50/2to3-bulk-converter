from tkinter import * 
import tkinter, tkinter.constants, tkinter.filedialog, tkinter.messagebox
import os, sys



class FileZap():
    def __init__(self, root):

        def getDir():
            dir = tkinter.filedialog.askdirectory(initialdir="C:/")
            self.user1.delete(0,END)
            self.user1.insert(0,dir)
            files = (file for file in os.listdir(dir)
                if os.path.isfile(os.path.join(dir, file)))
            for file in files:
                self.listbox1.insert(0,file)

        def selectAdd():
            selection1 = self.listbox1.curselection()
            for i in selection1:
                selectedFiles = self.listbox1.get(i)
                self.listbox2.insert(0, selectedFiles)

        root.title("Test_App 1.0")
        root.geometry("860x450")    
        self.listbox1 = Listbox(root, width=50, selectmode="multiple")
        self.listbox1.grid(row=2, column=2)
        self.scrollbar = Scrollbar(orient=VERTICAL, command=self.listbox1.yview)
        self.listbox1.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=2, column=3, sticky="ns")
        self.listbox2 = Listbox(root, width=50)
        self.listbox2.grid(row=2, column=4)
        self.label1 = Label(root, text="Select a folder: ")
        self.label1.grid(row=1, column=1)
        self.user1 = Entry(root, width="50")
        self.user1.grid(row=1, column=2)
        self.browse = Button(root, text="Browse", command=getDir)
        self.browse.grid(row=1, column=3)
        self.button2 = Button(root, text="Add to Selection", command=selectAdd)
        self.button2.grid(row=3, column=3)

        self.quit = Button(root, text="Exit", command=root.quit)
        self.quit.grid(row=8, column=4)


root = tkinter.Tk()
file_zap = FileZap(root)
root.mainloop()
