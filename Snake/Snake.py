#------------------------------------------THE SNAKE GAME BY KIMI-GR 30/06/2024---------------------------------------------------
from tkinter import *
import tkinter as tk
import random
import winsound
from time import*


musique1='musique menu.wav'
musique2='départ.wav'
musique3='musique snake.wav'
musique4='grandir.wav'
musique5='perdu.wav'
winsound.PlaySound(musique1, winsound.SND_FILENAME | winsound.SND_LOOP |winsound.SND_ASYNC)
SCORE=0
b=-1
a=0
c=2
en_marche=1
root = tk.Tk()



root.geometry("600x690")
root.resizable(False,False)
root.title("The Snake Game")
root.configure(bg='#171414')

label_list = []
oeil=[]
oeil2=[]
pomme_position = tk.Label(root, width=2, height=1, bg="#D53434",bd=2)
new_label = tk.Label(root, width=2, height=1, bg="#71D74E",bd=2)
squarer = tk.Frame(root, width=12, height=12, bg="white")
squarerr =tk.Frame(root, width=7, height=7, bg="black")
labeltext=Label(root,text="The Snake Game",font=("Terminal",47),bg='#171414',fg='lightgreen')
labeltext.place(relx=0.5,rely=0.25,anchor="center")
labeltext1=Label(root,font=("Terminal",100,"bold"),bg='#171414',fg='lightgreen')
presstostart=Label(root,text="PRESS TO PLAY",font=("terminal",20),bg='#171414',fg='white')
presstostart.place(relx=0.5,rely=0.63,anchor="center")
presstostar1t=Label(root,text="By Kimi",font=("Terminal",20),bg='#171414',fg='white')
presstostar1t.place(relx=0.5,rely=0.34,anchor="center")
pox=[]   
poy=[]
xxx=0
yyy=0
for i in range (25):
    xxx+=23
    pox.append(xxx)
for i in range (29):
    yyy+=23
    poy.append(yyy)



i=4
def musique():
    winsound.PlaySound(musique2, winsound.SND_FILENAME | winsound.SND_ASYNC)
    text3()
def text3():
    
    global i
    global presstostart
    global presstostar1t
    presstostart.destroy()
    presstostar1t.destroy()
    labeltext.destroy()
    bouton.destroy()
    
    
        
    if i>1:
        labeltext1.config(text=i-1)
        labeltext1.place(relx=0.5,rely=0.25,anchor="center")
    
    if i==1:
        labeltext1.config(text="GO!")
        labeltext1.place(relx=0.5,rely=0.5,anchor="center")
    if i<1:
        game()
    if i>0:
        i-=1

        root.after(1000,text3)
def game():
    winsound.PlaySound(musique3, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
    global labeltext
    global labeltext1
    labeltext1.destroy()
    bouton.destroy()
    labeltext.destroy()
    
    
    global new_label
    global pomme_position
    global b
    labelmenu=tk.Label(root,width=300,height=1,bg='#9B0000')
    labelmenu.pack()
    score=tk.Label(root,font=("Terminal",15),text="score :",fg='white',bg="#9B0000")
    score.place(x=10,y=-3)
    score1=tk.Label(root,font=("Terminal",12),text=SCORE,fg='white',bg="#9B0000")
    score1.place(x=68,y=-0.5)
    snake=tk.Label(root,text="SNAKE",font=("terminal",12),fg='white',bg="#9B0000")
    snake.place(relx=0.5,rely=0.0151,anchor="center")

    def bas(event):
        global a
        global c
        if c!=4:
            a=1
            c=1
        return a
    def haut(event):
        global a
        global c
        if c!=1:
            a=2
            c=4
        return a
    def droite(event):
        global a
        global c
        if c!=3:
            a=0
            c=2
        return a
    def gauche(event):
        global a
        global c
        if c!=2:
            a=3
            c=3
        
        return a

    root.bind("<Up>",haut)
    root.bind("<Down>",bas)
    root.bind("<Left>",gauche)
    root.bind("<Right>",droite)


    x=0
    square = tk.Frame(root, width=12, height=12, bg="white")
    square.place(x=46, y=250)
    oeil.append(square)
    squar = tk.Frame(root, width=5, height=5, bg="black")
    squar.place(x=46+2, y=250+2.5)
    oeil2.append(squar)
    for i in range(3):
        
        corps = tk.Label(root, width=2, height=1, bg="#71D74E",bd=2)
        corps.place(x=x,y=250)
        label_list.append(corps)
        
        b+=1
        x+=23

    

    def create_label():

        global new_label
        global a
        global b
        global squarer
        global squarerr
        
        
        

        dep = label_list[b] # coordonnées premier
        x = dep.winfo_x()
        y = dep.winfo_y()
        new_label = tk.Label(root, width=2, height=1, bg="#71D74E",bd=2)
        
        if a==0:
            new_label.place(x=x+23,y=y)
            
        if a==1:
            new_label.place(x=x,y=y+23)
            
        if a==2:
            new_label.place(x=x,y=y-23)
            
        if a==3:
            new_label.place(x=x-23,y=y)
            


        label_list.append(new_label)
        label_to_remove = label_list.pop(0)  # dernier
        label_to_remove.destroy()  # Supprime le widget du label
        squarer = tk.Frame(root, width=12, height=12, bg="white")
        squarerr =tk.Frame(root, width=7, height=7, bg="black")
            
        if a==0:
            
            squarer.place(x=x+27,y=y+4)
            squarerr.place(x=x+30,y=y+6)
        if a==1:
            
            squarer.place(x=x+3,y=y+27)
            squarerr.place(x=x+4.5,y=y+30)
        if a==2:
            
            squarer.place(x=x+4,y=y-19)
            squarerr.place(x=x+6,y=y-19)
        if a==3:
            
            squarer.place(x=x-19,y=y+4)
            squarerr.place(x=x-23+5,y=y+6)
        oeil.append(squarer)
        oeil2.append(squarerr)
        squaretode = oeil.pop(0)
        squaretode.destroy()
        squaretodel = oeil2.pop(0)
        squaretodel.destroy()
        
        condition=1
        indice=1
        
        for i in range(b-2):
            partie=label_list[indice]
            xi=partie.winfo_x()
            yi=partie.winfo_y()
            indice+=1
            
            if (xi)==x and yi==y:
                winsound.PlaySound(None, winsound.SND_PURGE)
                winsound.PlaySound(musique5,winsound.SND_FILENAME | winsound.SND_ASYNC)
                label=tk.Label(root,font=("terminal",50),text="GAME OVER",width=20,height=10,fg='white',bg='#171414')
                label.place(relx=0.5,rely=0.5,anchor="center")
                bouton=Button(root,text="EXIT",font=("terminal",20,"bold"),border=0,bg='#171414',fg='red',command=root.quit)
                bouton.place(relx=0.5,rely=0.65,anchor="center")
                condition=2

        
        if x>=583 or y>=673 or x<0 or y<10:
            winsound.PlaySound(None, winsound.SND_PURGE)
            winsound.PlaySound(musique5,winsound.SND_FILENAME | winsound.SND_ASYNC)
            label=tk.Label(root,font=("terminal",50),text="GAME OVER",width=20,height=10,fg='white',bg='#171414')
            label.place(relx=0.5,rely=0.5,anchor="center")
            bouton=Button(root,text="EXIT",font=("terminal",20,"bold"),border=0,bg='#171414',fg='red',command=root.quit)
            bouton.place(relx=0.5,rely=0.65,anchor="center")
            condition=2
            
        
        if condition==1:
            root.after(120-SCORE,create_label)
            
        
            
            
        else:
            pass

    
    def pomme():
        global pox
        global poy
        random.shuffle(poy)
        random.shuffle(pox)
        yy=poy[0]
        xx=pox[0]
        

        pomme_position.place(x=xx,y=yy)


    def colision():
        
        global en_marche
        global a
        global b
        label_to_remove = label_list[b]
        global SCORE
        
        
        
       
        pommex = pomme_position.winfo_x()
        pommey = pomme_position.winfo_y()
        new_labelx=new_label.winfo_x()
        new_labely=new_label.winfo_y()
        x= label_to_remove.winfo_x()
        y= label_to_remove.winfo_y()
        
        
        if -20<pommex-new_labelx<20 and -20<pommey-new_labely<20:
            
            pomme()
            SCORE+=1
            score=tk.Label(root,font=("Terminal",15),text="score :",fg='white',bg="#9B0000")
            score.place(x=10,y=-3)
            score1=tk.Label(root,font=("Terminal",12),text=SCORE,fg='white',bg="#9B0000")
            score1.place(x=68,y=-0.5)
            pupille =tk.Frame(root, width=7, height=7, bg="black")
            oeilenplus = tk.Frame(root, width=12, height=12, bg="white")
            corpsenplus = tk.Label(root, width=2, height=1, bg="#71D74E",bd=2)
            if a==0:
                corpsenplus.place(x=x+23,y=y)
                
            if a==1:
                corpsenplus.place(x=x,y=y+23)
            if a==2:
                corpsenplus.place(x=x,y=y-23)
            if a==3:
                corpsenplus.place(x=x-23,y=y)

            label_list.insert(b+1,corpsenplus)
            b+=1
            if a==0:
            
                oeilenplus.place(x=x+27,y=y+4)
                pupille.place(x=x+30,y=y+6)
            if a==1:
                
                oeilenplus.place(x=x+3,y=y+27)
                pupille.place(x=x+4.5,y=y+30)
            if a==2:
                
                oeilenplus.place(x=x+4,y=y-19)
                pupille.place(x=x+6,y=y-19)
            if a==3:
                
                oeilenplus.place(x=x-19,y=y+4)
                pupille.place(x=x-23+5,y=y+6)
            oeil.append(oeilenplus)
            oeil2.append(pupille)
            squaretode = oeil.pop(0)
            squaretode.destroy()
            squaretodel = oeil2.pop(0)
            squaretodel.destroy()
            
        



        root.after(10,colision)
    pomme()

    root.after(120,create_label)
    root.after(10,colision)

bouton=Button(root,text="PLAY",font=("terminal",50,"bold"),border=0,width=6,background='lightgreen',activebackground='#171414',activeforeground='lightgreen',foreground='#171414',command=musique)
bouton.place(relx=0.5,rely=0.75,anchor="center")

root.mainloop()
