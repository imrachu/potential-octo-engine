from tkinter import *
import math
top=Tk()
E=Entry(top,width=35,bg='lightblue')
E.grid(row=0,column=0,columnspan=6)
x=0
y=0
ch=""
def one():
    a=E.get()
    b=len(a)
    E.insert(b,"1")
def two():
    a=E.get()
    b=len(a)
    E.insert(b,"2")
def three():
    a=E.get()
    b=len(a)
    E.insert(b,"3")
def four():
    a=E.get()
    b=len(a)
    E.insert(b,"4")
def five():
    a=E.get()
    b=len(a)
    E.insert(b,"5")
def six():
    a=E.get()
    b=len(a)
    E.insert(b,"6")
def seven():
    a=E.get()
    b=len(a)
    E.insert(b,"7")
def eight():
    a=E.get()
    b=len(a)
    E.insert(b,"8")
def nine():
    a=E.get()
    b=len(a)
    E.insert(b,"9")
def zero():
    a=E.get()
    b=len(a)
    E.insert(b,"0")
def dec():
    a=E.get()
    b=len(a)
    E.insert(b,".")

def plus():
    global x
    global ch
    a=E.get()
    ch="+"
    x=float(E.get())
    b=len(a)
    E.delete(0,b)

def sub():
    global x
    global ch
    a=E.get()
    ch="-"
    x=float(E.get())
    b=len(a)
    E.delete(0,b)

def mul():
    global x
    global ch
    a=E.get()
    ch="*"
    x=float(E.get())
    b=len(a)
    E.delete(0,b)
def div():
    global x
    global ch
    a=E.get()
    ch="/"
    x=float(E.get())
    b=len(a)
    E.delete(0,b)
def mod():
    global x
    global ch
    a=E.get()
    ch="%"
    x=float(E.get())
    b=len(a)
    E.delete(0,b)

def del1():
    a=E.get()
    b=len(a)
    E.delete(0,b)
def del2():
    a=E.get()
    b=len(a)
    E.delete(b-1,b)

def root():
    global x
    global ch
    a=E.get()
    ch="&"
    x=float(E.get())
    b=len(a)
    E.delete(0,b)

def sqre():
    global x
    global ch
    a=E.get()
    ch="^"
    x=float(E.get())
    b=len(a)
    E.delete(0,b)

def equal():
    global x
    global y
    global ch
    a=E.get()
    y=float(E.get())
    b=len(a)
    E.delete(0,b)
    if(ch=="+"):
        x=x+y
        E.insert(0,x)
    elif(ch=="-"):
        x=x-y
        E.insert(0,x)
    elif(ch=="*"):
        x=x*y
        E.insert(0,x)
    elif(ch=="/"):
        x=x/y
        E.insert(0,x)
    elif(ch=="%"):
        x=x%y
        E.insert(0,x)
    elif(ch=="&"):
        y=0.5
        x=x**y
        E.insert(0,x)
    elif(ch=="^"):
        x=x**y
        E.insert(0,x)

b1=Button(top,text="=",width=10,command=equal)
b1.grid(row=4, column=4,columnspan=2)
b2=Button(top,text='AC',width=10,command=del1)
b2.grid(row=1, column=4,columnspan=2)
b3=Button(top,text='C',width=10,command=del2)
b3.grid(row=2, column=4,columnspan=2)
b4=Button(top,text="+",width=3,command=plus,font=(times,20))
b4.grid(row=4, column=3)
b5=Button(top,text="x",width=3,command=mul)
b5.grid(row=2, column=3)
b6=Button(top,text="-",width=3,command=sub)
b6.grid(row=3, column=3)
b7=Button(top,text="÷",width=3,command=div)
b7.grid(row=1, column=3)
b8=Button(top,text="%",width=3,command=mod)
b8.grid(row=4, column=2)
b9=Button(top,text="7",width=3,command=seven)
b9.grid(row=1, column=0)
b10=Button(top,text="8",width=3,command=eight)
b10.grid(row=1, column=1)
b11=Button(top,text="9",width=3,command=nine)
b11.grid(row=1, column=2)
b12=Button(top,text="4",width=3,command=four)
b12.grid(row=2, column=0)
b13=Button(top,text="5",width=3,command=five)
b13.grid(row=2, column=1)
b14=Button(top,text="6",width=3,command=six)
b14.grid(row=2, column=2)
b15=Button(top,text="1",width=3,command=one)
b15.grid(row=3, column=0)
b16=Button(top,text="2",width=3,command=two)
b16.grid(row=3, column=1)
b17=Button(top,text="3",width=3,command=three)
b17.grid(row=3, column=2)
b18=Button(top,text="0",width=3,command=zero)
b18.grid(row=4, column=0)
b19=Button(top,text=".",width=3,command=dec)
b19.grid(row=4, column=1)
b20=Button(top,text="√",width=4,command=root)
b20.grid(row=3, column=4)
b21=Button(top,text="x²",width=4,command=sqre)
b21.grid(row=3, column=5)

top.mainloop()