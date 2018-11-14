from tkinter import *
from tkinter import messagebox
root=Tk(className='message')

def msg():
	messagebox.showinfo("Say Hello", "Hello World\n welcome to tkinter")

def anser():
	ans=messagebox.askquestion("question","are you mad")
	if ans=='yes':
		messagebox.showerror("warnig","you are mad")
		print("yes you are mad ")
	else:
		messagebox.showwarning("warnig","you are not mad")
		print("so you are not mad right")

btn=Button(root,text="pop up",command=msg)
btn.pack()
bt=Button(root,text="true" or false,command=anser)
bt.pack()

root.mainloop()