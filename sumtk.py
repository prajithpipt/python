from tkinter import *

root=Tk(className='addition')
def add(event):
	n1=int(num1.get())
	n2=int(num2.get())
	sum=n1+n2
	res.delete(0,"end")
	res.insert(0,sum)


Label(root,text="enter first number :").grid(row=0,sticky=W,padx=5)
num1=Entry(root).grid(row=0,column=1,sticky=E,padx=5)

Label(root,text="enter second number :").grid(row=1,sticky=W,padx=5)
num2=Entry(root).grid(row=1,column=1,sticky=E,padx=5)

btn=Button(root,text="add").grid(row=3)
btn.bind("<Button-1>",add)


res=Entry(root).grid(row=5,sticky=E)

root.mainloop()