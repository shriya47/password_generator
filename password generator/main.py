from tkinter import *
import string
from random import randint

root=Tk()
root.title("Password Generator")


def new_rand():
    pw_entry.delete(0, END)

    pw_length=int(my_entry.get())
    mypass=''
    
    for x in range(pw_length):
        mypass += chr(randint(33,126))

    pw_entry.insert(0, mypass)

lf = LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

my_entry=Entry(lf,font=("Helvetica",24))
my_entry.pack(pady=20, padx=20)

pw_entry=Entry(root,text='',font=("Helvetica",24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20, padx=20)

my_frame=Frame(root)
my_frame.pack(pady=20)

my_button= Button(my_frame, text="Generate Strong Password", command= new_rand)
my_button.grid(row=0, column=0, padx=10)

root.mainloop()