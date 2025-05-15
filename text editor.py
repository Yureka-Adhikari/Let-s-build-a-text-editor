from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfilename, asksaveasfilename

root = Tk()
root.geometry('200x150')

def save():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    
    file = asksaveasfile(filetypes= files, defaultextension= files)
    
btn = Button(root, text="Save", command= lambda: save())
btn.pack(side=TOP)

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    root.title(f"Codingal's Text Editor - {filepath}")
    
    
txt_edit = Text(root)
btn = Button(root, text="Open", command= lambda: open_file())
btn.pack(side=TOP)

mainloop()