from tkinter import*
from time import *
from random import *
 
window = Tk()
window.title("BadUI")
window.geometry("700x400")
window.minsize(700,400)
window.maxsize(700,400)
window.config(background='#2C2D43')



def le():
    root=Toplevel(window)
    root.geometry('180x180')
    root.minsize(180,180)
    root.maxsize(180,180)
    root.title("key")
    root.config(background='#2C2D43')
    leter=["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]
    shuffle(leter)
    x=leter[0]
    
    def command():
        entre.configure(state="normal")
        texte_actuel = entre.get()
        textenouveau=texte_actuel+x
        entre.delete(0,"end")
        entre.insert(0,textenouveau)
        entre.configure(state="readonly")
        
    
    a=Button(root,text=x,font=("Ubuntu",50),bg='#585971',fg='white',command=command,relief='raised',border=20,width=3,height=1,cursor="hand2")
    a.place(x=10,y=10)

    
    root.mainloop()


entre=Entry(font=("Ubuntu",15),bg='#2C2D43',fg='black',state="readonly")
entre.place(x=200,y=280,width=300)
consigne=Label(font=("",15),bg='#2C2D43',fg='white',text="cliquez ici 👆 pour faire apparaître une lettre")
consigne.place(x=150,y=200)

bouton=Button(text="+",font=("Ubuntu",50),bg='#585971',fg='white',command=le,relief='raised',border=20,width=3,height=1,cursor="hand2")
bouton.place(x=270,y=20)


def va():
    bouton.destroy()
    consigne.destroy()
    r=entre.get()
    entre.destroy()
    validerbouton.destroy()
    bravo=Label(font=("",50),bg='#2C2D43',fg='white',text= r)
    bravo.pack(pady=60)

validerbouton=Button(text="Valider !",font=("Ubuntu",15),bg='#2C2D43',fg='#D0D7D0',command=va,relief='flat',cursor="hand2")
validerbouton.place(x=300,y=330)







window.mainloop()
