from tkinter import *

def addit():
	num1=int(e1.get())
	num2=int(e2.get())
	sum=(num1+num2)
	e3=Label(text="sum %d" %sum,bg="white",bd=15,padx=10)
	e3.pack()

root=Tk(className="add")
root.geometry("750x550")

root.title("ADD TWO NUMBERS")
lbl1=Label(root,text="number1")
e1=Entry(root,bd=8)
lbl1.pack()
e1.pack()

lbl2=Label(root,text="number2")
e2=Entry(root,bd=8)
lbl2.pack()
e2.pack()

add=Button(root,text="Add",command=addit)
add.pack()

root.mainloop()
"""

from tkinter import*
from functools import partial


def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(bd=20,text="Result is %d" % result)
    return

root = Tk(className='Simple Calculator')
root.geometry('400x200+100+200')

number1 = StringVar()
number2 = StringVar()

labelTitle = Label(root, text="Simple Calculator").grid(row=0, column=2)

labelNum1 = Label(root, text="Enter first number :").grid(row=1, column=0)
entryNum1 = Entry(root, textvariable=number1).grid(row=1, column=2)

labelNum2 = Label(root, text="Enter second number :").grid(row=2, column=0)
entryNum2 = Entry(root, textvariable=number2).grid(row=2, column=2)

labelResult =Label(root,bd=15)
labelResult.grid(row=7, column=2,padx=5)



call_result = partial(call_result, labelResult, number1, number2)
buttonCal = Button(root, text="Calculate", command=call_result).grid(row=3, column=0)
root.mainloop()"""