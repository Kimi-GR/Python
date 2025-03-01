from tkinter import*
import string
v=0
#fenetre
window=Tk()
window.geometry("400x500")
window.maxsize(400,500)
window.minsize(400,500)
window.title("calculatrice")
window.config(background='#67EDDB')

ecran=Entry(window,bg='white',fg='black',font=("Terminal",50))
ecran.pack(fill=Y,padx=10,pady=10)
#fonction
def bouton_clik(number):
    current=ecran.get()
    ecran.delete(0,END)
    ecran.insert(0,str(current)+str(number))
def button_equal():
    number=ecran.get()
    ecran.delete(0,END)
    ecran.insert(0,eval(number))
def bouton_retour():
    ecran.delete(0,END)




#bouton
un_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "1",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('1'))
un_button.place(x=0,y=110)
deux_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "2",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('2'))
deux_button.place(x=90, y=110)
trois_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "3",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('3'))
trois_button.place(x=180,y=110)

quatre_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "4",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('4'))
quatre_button.place(x=0,y=200)
cinq_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "5",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('5'))
cinq_button.place(x=90,y=200)
six_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "6",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('6'))
six_button.place(x=180,y=200)

sept_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "7",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('7'))
sept_button.place(x=0,y=290)

huit_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "8",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('8'))
huit_button.place(x=90,y=290)
neuf_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "9",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('9'))
neuf_button.place(x=180,y=290)
zero_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "0",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('0'))
zero_button.place(x=0,y=400)

plus_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "+",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('+'))
plus_button.place(x=300,y=190)
moins_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "-",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('-'))
moins_button.place(x=300,y=280)
egal_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "=",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:button_equal())
egal_button.place(x=300,y=400)

fois_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "x",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('*'))
fois_button.place(x=90,y=400)
diviser_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "/",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_clik('/'))
diviser_button.place(x=180,y=400)
retour_button=Button(window, width=7, height=5,  font=("Terminal",12), text= "<-",bg='#01AC95',fg='white' ,bd=4,highlightthickness=0,command=lambda:bouton_retour())
retour_button.place(x=300,y=100)





#afficher
window.mainloop()
