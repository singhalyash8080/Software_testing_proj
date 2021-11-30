
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class splash:
    def __init__(self):
      self.splashminw=Tk()
      self.splashminw.title("About")
      width = 1000
      height = 700
      self.splashminw.config(bg="#4267b2")
      screen_width = self.splashminw.winfo_screenwidth()
      screen_height = self.splashminw.winfo_screenheight()
      x = (screen_width / 2) - (width / 2)
      y = (screen_height / 2) - (height / 2)
      self.splashminw.geometry("%dx%d+%d+%d" % (width, height, x, y))
      self.splashminw.resizable(0,0)
      main=LabelFrame(self.splashminw, width=890, height=560,bg="snow",relief="sunken")
      main.place(x=55,y=70)
      photoframe = LabelFrame(main, width=420, height=444, bg="snow", relief="raised")
      photoframe.place(x=10, y=100)
      Label(main, text="Sales And Inventory Management System",font="roboto 32 bold underline",bg="snow").place(x=45, y=10)
      self.splashminw.after(1,lambda :self.splashminw.destroy())
      self.splashminw.mainloop()


