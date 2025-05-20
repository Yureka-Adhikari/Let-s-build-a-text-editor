from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')
root.title('Interest Calculator')
root.configure(background="#5D1C16")

lbl1 = Label(root, text="Principal (deposit) :", fg="#F3C8D9", bg="#5D1C16")
lbl2 = Label(root, text="Time period (years) :",  fg="#F3C8D9", bg="#5D1C16")
lbl3 = Label(root, text="Rate of interest :", fg="#F3C8D9",bg="#5D1C16")
lbl4 = Label(root, text="Number of times :", fg="#F3C8D9",bg="#5D1C16")

e1 = Entry(root, text="principal")
e2 = Entry(root, text="time")
e3 = Entry(root, text="rate")
e4 = Entry(root, text="no.of times")

lbl1.place(x=75, y=100 )
lbl2.place(x=75, y=130 )
lbl3.place(x=75, y=160 )
lbl4.place(x=75, y=190 )

e1.place(x=190, y=100 )
e2.place(x=190, y=130 )
e3.place(x=190, y=160)
e4.place(x=190, y=190)

def calculation():
    try:
        global principal
        global time
        global rate

        principal = int(e1.get())
        time = int(e2.get())
        rate = int(e3.get())
        n = int(e4.get())
            
        s_i = (principal*time*rate)/100
        
        c_i = principal * (1 + (rate / 100) / n) ** (n * time)
        
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        
        text_box = Text(root, height=70, width=45, wrap = WORD)
        text_box.pack(pady=10)
        text_box.delete(1.0, END)
        
        text = f"For \n principal : {principal} \n time: {time} \n rate: {rate} \n number of times : {n}\n"
        simple= f"Simple Interest is : {s_i}\n"
        compound= f"Compound Interest is: {c_i}"
        
        text_box.insert(END, text)
        text_box.insert(END, simple)
        text_box.insert(END, compound)
        
        text_box.place(x=20, y=250)
           
    except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

button1 = Button(root,
                 text= "Calculate",
                 command= calculation,
                 bg= "brown",
                 fg= "white")
button1.place(x=190, y=220)

root.mainloop()