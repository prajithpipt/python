from tkinter import *
from tkinter import ttk
root=Tk(className='inser number')

label=Label(root,text="enter name :").grid(row=0,sticky=W,padx=4)
Entry(root).grid(row=0,column=1,sticky=E,padx=4)

btn=Button(root,text='click me').grid(row=2)

root.mainloop()