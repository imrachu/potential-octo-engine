from tkinter import *
top=Tk()
top.title("Notepad By- Rachit")
yscrollbar=Scrollbar(top)
xscrollbar=Scrollbar(top,orient=HORIZONTAL)
yscrollbar.pack(side=RIGHT,fill=Y)
xscrollbar.pack(side=BOTTOM,fill=X)
t=Text(top,height=100,width=200,wrap=NONE,yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)
t.pack(side=LEFT,fill=BOTH)

xscrollbar.config(command=t.xview)
yscrollbar.config(command=t.yview)
m=Menu(top)
f1=Menu(m)
f1.add_command(label="New")
f1.add_command(label="Open...")
f1.add_command(label="save")
f1.add_command(label="Save as...")
f1.add_separator()
f1.add_command(label="Page Setup...")
f1.add_command(label="Print...")
f1.add_separator()
f1.add_command(label="Exit",command=top.destroy)
m.add_cascade(label="File",menu=f1)
f2=Menu(m)
f2.add_command(label="Undo")
f2.add_separator()
f2.add_command(label="Cut")
f2.add_command(label="Copy")
f2.add_command(label="Paste")
f2.add_command(label="Delete")
f2.add_separator()
f2.add_command(label="Find")
f2.add_command(label="Replace")
m.add_cascade(label="Edit",menu=f2)
f5=Menu(m)
f5=Menu(m)
f5.add_command(label="Word Wrap")
f5.add_command(label="Font")
m.add_cascade(label="Format",menu=f5)
f3=Menu(m)
f3.add_command(label="Status Bar")
m.add_cascade(label="View",menu=f3)
f4=Menu(m)
f4.add_command(label="View Help")
f4.add_separator()
f4.add_command(label="About Notepad")
m.add_cascade(label="Help",menu=f4)
top.config(menu=m)

top.mainloop()