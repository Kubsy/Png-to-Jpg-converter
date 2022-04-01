from tkinter import *
from tkinter import filedialog

Window = Tk()
Window.resizable(False, False)
Window.title("PNGtoJPG")

class app():

    def __init__(self, parent):
        self.createWidgets(parent)
    
    def createWidgets(self, main):
        mainFrame = Frame(main)

        self.Heading = Label(mainFrame, text="Welcome to the \n PNG to JPG converter!", font="Bold", pady=10).grid(row=0, column=1)
        self.Convert = Button(mainFrame, text="Convert to JPG", pady=5).grid(row=1, column=2)
        self.importJPGButton = Button(mainFrame, text="Import a PNG image", pady=5, command=self.getImage).grid(row=1, column=0)

        mainFrame.pack()

    def getImage(self):
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))

    def convert(self):
        pass

p = app(Window)
Window.mainloop()
        
