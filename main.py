import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("HaLake Desktop")

root.state('zoomed')
root.configure(background='black')
root.attributes("-alpha",0.85)
root.attributes('-transparent', 0.85)

text = Text(root)
text.insert(INSERT, "Hello, world!\n")
text.insert(END, "This is a phrase.\n")
text.insert(END, "Bye bye...")

for i in range(1000):
    text.insert(INSERT, "Hello, world!\n")
    text.insert(END, "This is a phrase.\n")
    text.insert(END, "Bye bye...")

text.pack(expand=1, fill=BOTH)

# adding a tag to a part of text specifying the indices
text.tag_add("start", "1.7", "1.13")
text.tag_config("start", background="black", foreground="yellow")

root.mainloop()
