


from tkinter import*
from tkinter.ttk import*
from time import strftime


root=Tk()
root.title('horloge digitale')
label= Label(root, font=('aerial',30),background='blue',foreground='white')
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
label.pack(anchor='center')
time()
mainloop()

