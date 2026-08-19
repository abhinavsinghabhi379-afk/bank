import tkinter as tk

root=tk.Tk()
root.minsize(500,600)
root.title("Abhinav Singh")
label=tk.Label(root,text="UserName:",bg='red').grid(column=1,row=1)
name=tk.StringVar()
entry=tk.Entry(root,bg="yellow",textvariable=name).grid(column=1,row=2)

root.mainloop()