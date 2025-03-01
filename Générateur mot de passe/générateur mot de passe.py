from random import *
from tkinter import *
import string
#fonction bouton

def mdp():
    min=7
    max=13
    all_chars=string.ascii_letters+string.punctuation+string.digits
    password="".join(choice(all_chars)for x in range(randint(min,max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    
    


#crée la fnetre
window = Tk()
window.title("generateur de mot de passe")
window.geometry("719x450")
window.minsize(719,450)
window.config(background='#27AC88')
#frame
frame=Frame(window,bg='#27AC88')
#frame2
right_frame=Frame(frame,bg='#27AC88')
#cree une image
width=300
heigth=300
image=PhotoImage(file="cadenas.png").zoom(18).subsample(32)
canvas=Canvas(frame,width=width, height=heigth,bg='#27AC88' ,bd=0,highlightthickness=0)
canvas.create_image(width/2, heigth/2 ,image=image)
canvas.grid(row=0,column=0,sticky=W)

width = 300
height = 300
image1 = PhotoImage(file="bouton-de-lecture.png").zoom(32).subsample(200)
#afficher texte
label_title=Label(right_frame, text="mot de passe", font=("Ubuntu",35),bg='#27AC88',fg='white')
label_title.pack()



#enter
password_entry=Entry(right_frame, font=("Ubuntu",20),bg='#27AC88',fg='white')
password_entry.pack()
#bouton
generate_password_button=Button(right_frame, image=image1,bg='#27AC88',fg='white', command=mdp,bd=0,highlightthickness=0)


generate_password_button.pack()





#afficher la frame
right_frame.grid(row=0,column=1, sticky=W)
frame.pack(expand=YES)

menu_bar=Menu(window)
file_menu=Menu(menu_bar, tearoff=0)
file_menu.add_command(label="quitter",font=("Ubuntu",12,),background='red',command=window.quit)
file_menu.add_command(label="nouveau",command=mdp,font=("Ubuntu",12,),background='green')
menu_bar.add_cascade(label="fichier",menu=file_menu)
window.config(menu=menu_bar)
#afficher
window.mainloop()
