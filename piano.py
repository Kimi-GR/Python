from tkinter import*
import winsound
from random import *
 
window = Tk()
window.title("Piano")
window.geometry("700x400")
window.minsize(700,400)
window.maxsize(700,400)
window.config(background='#27AC88')

def do():
    winsound.PlaySound('do.wav',winsound.SND_ASYNC)
do=Button( cursor="dot",bg='#ffffff',fg='black',bd=3,command=do,highlightthickness=0,relief='solid')
do.place(x=0,y=0,width=100,height=400)
def re():
    winsound.PlaySound('re.wav',winsound.SND_ASYNC)
re=Button( cursor="dot",bg='#ffffff',fg='black',bd=3,command=re,highlightthickness=0,relief='solid')
re.place(x=100,y=0,width=100,height=400)
def mi():
    winsound.PlaySound('mi.wav',winsound.SND_ASYNC)
mi=Button( cursor="dot",bg='#ffffff',fg='black',bd=3,command=mi,highlightthickness=0,relief='solid')
mi.place(x=200,y=0,width=100,height=400)
def fa():
    winsound.PlaySound('fa.wav',winsound.SND_ASYNC)
fa=Button( cursor="dot",bg='#ffffff',fg='black',bd=3,command=fa,highlightthickness=0,relief='solid')
fa.place(x=300,y=0,width=100,height=400)
def sol():
    winsound.PlaySound('sol.wav',winsound.SND_ASYNC)
sol=Button( cursor="dot",bg='#ffffff',fg='black',bd=3,command=sol,highlightthickness=0,relief='solid')
sol.place(x=400,y=0,width=100,height=400)
def la():
    winsound.PlaySound('la.wav',winsound.SND_ASYNC)
la=Button( cursor="dot",bg='#ffffff',fg='black',bd=3,command=la,highlightthickness=0,relief='solid')
la.place(x=500,y=0,width=100,height=400)
def si():
    winsound.PlaySound('si.wav',winsound.SND_ASYNC)
si=Button( cursor="dot",bg='#ffffff',fg='black',bd=3,command=si,highlightthickness=0,relief='solid')
si.place(x=600,y=0,width=100,height=400)

def n1():
    winsound.PlaySound('n1.wav',winsound.SND_ASYNC)
n=Button( cursor="dot",bg='#000000',fg='black',command=n1,bd=3,highlightthickness=0,relief='sunken')
n.place(x=55,y=0,width=70,height=275)
def n2():
    winsound.PlaySound('n2.wav',winsound.SND_ASYNC)
o=Button( cursor="dot",bg='#000000',fg='black',command=n2,bd=3,highlightthickness=0,relief='sunken')
o.place(x=175,y=0,width=70,height=275)
def n3():
    winsound.PlaySound('n3.wav',winsound.SND_ASYNC)
p=Button( cursor="dot",bg='#000000',fg='black',command=n3,bd=3,highlightthickness=0,relief='sunken')
p.place(x=355,y=0,width=70,height=275)
def n4():
    winsound.PlaySound('n4.wav',winsound.SND_ASYNC)
q=Button( cursor="dot",bg='#000000',fg='black',command=n4,bd=3,highlightthickness=0,relief='sunken')
q.place(x=575,y=0,width=70,height=275)

def n5():
    winsound.PlaySound('n5.wav',winsound.SND_ASYNC)
r=Button( cursor="dot",bg='#000000',command=n5,fg='black',bd=3,highlightthickness=0,relief='sunken')
r.place(x=465,y=0,width=70,height=275)

def dom():
    winsound.PlaySound('do.wav',winsound.SND_ASYNC)
    color=['#f43207','#F54B85','#8fdf0c','#fcd83b','#bf3ca7','#b80766','#b3ec48']
    shuffle(color)
    a=color[0]
    do.config(bg=a)
def rem():
    winsound.PlaySound('re.wav',winsound.SND_ASYNC)
    color=['#f43207','#F54B85','#8fdf0c','#fcd83b','#bf3ca7','#b80766','#b3ec48']
    shuffle(color)
    a=color[0]
    re.config(bg=a)
def mim():
    winsound.PlaySound('mi.wav',winsound.SND_ASYNC)
    color=['#f43207','#F54B85','#8fdf0c','#fcd83b','#bf3ca7','#b80766','#b3ec48']
    shuffle(color)
    a=color[0]
    mi.config(bg=a)
def fam():
    winsound.PlaySound('fa.wav',winsound.SND_ASYNC)
    color=['#f43207','#F54B85','#8fdf0c','#fcd83b','#bf3ca7','#b80766','#b3ec48']
    shuffle(color)
    a=color[0]
    fa.config(bg=a)
def solm():
    winsound.PlaySound('sol.wav',winsound.SND_ASYNC)
    color=['#f43207','#F54B85','#8fdf0c','#fcd83b','#bf3ca7','#b80766','#b3ec48']
    shuffle(color)
    a=color[0]
    sol.config(bg=a)
def lam():
    winsound.PlaySound('la.wav',winsound.SND_ASYNC)
    color=['#f43207','#F54B85','#8fdf0c','#fcd83b','#bf3ca7','#b80766','#b3ec48']
    shuffle(color)
    a=color[0]
    la.config(bg=a)
def sim():
    winsound.PlaySound('si.wav',winsound.SND_ASYNC)
    color=['#f43207','#F54B85','#8fdf0c','#fcd83b','#bf3ca7','#b80766','#b3ec48']
    shuffle(color)
    a=color[0]
    si.config(bg=a)


def colormode():
    do.config(command=dom)
    re.config(command=rem)
    mi.config(command=mim)
    fa.config(command=fam)
    sol.config(command=solm)
    la.config(command=lam)
    si.config(command=sim)

def doc():
    winsound.PlaySound('do.wav',winsound.SND_ASYNC)
def rec():
    winsound.PlaySound('re.wav',winsound.SND_ASYNC)
def mic():
    winsound.PlaySound('mi.wav',winsound.SND_ASYNC)
def fac():
    winsound.PlaySound('fa.wav',winsound.SND_ASYNC)
def solc():
    winsound.PlaySound('sol.wav',winsound.SND_ASYNC)
def lac():
    winsound.PlaySound('la.wav',winsound.SND_ASYNC)
def sic():
    winsound.PlaySound('si.wav',winsound.SND_ASYNC)

def normalmode():
    do.config(command=doc ,bg='#ffffff')
    re.config(command=rec ,bg='#ffffff')
    mi.config(command=mic ,bg='#ffffff')
    fa.config(command=fac ,bg='#ffffff')
    sol.config(command=solc ,bg='#ffffff')
    la.config(command=lac ,bg='#ffffff')
    si.config(command=sic ,bg='#ffffff')


menu_bar=Menu(window)
file_menu=Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Mode Multicolor",font=("open sans",12,),background='#4FDAE0',command=colormode)
file_menu.add_command(label="Mode Classic",font=("open sans",12,),background='#FFFFFF',command=normalmode)
menu_bar.add_cascade(label="Paramètres",menu=file_menu)
window.config(menu=menu_bar)

window.mainloop()
