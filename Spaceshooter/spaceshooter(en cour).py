import tkinter as tk

root = tk.Tk()

root.configure(background='white')
root.attributes('-transparentcolor', 'white')
root.title("SPACE SHOOTER")
root.geometry("600x400")
root.resizable(False,False)
missiles=[]
tirer=0

label = tk.Label(root,height=2,width=4, bg='orange')
label.place(x=275, y=350)
def gauche(event):
    x=label.winfo_x()
    label.place(x=x-10,y=350)
def droite(event):
    x2=label.winfo_x()
    label.place(x=x2+10,y=350)
root.bind("<Left>",gauche)
root.bind("<Right>",droite)
def shoot(event):
    x3=label.winfo_x()
    projectile=tk.Label(root,width=1,height=2,bg='black')
    projectile.place(x=x3,y=360)
    missiles.append(projectile)
root.bind("<a>",shoot)
nbr=1

    

def tir():
    global missiles
    if missiles==[]:
        tirer=0
    if missiles!=[]:
        az=len(missiles)
        
        global projectile
        global nbr
        indice=az-1
        

        for i in range(az):
            print(az)
            print(indice)
            anim=missiles[indice]
            x=anim.winfo_x()
            y=anim.winfo_y()
            anim.place(x=x,y=y-10)
            indice+=1
            nbr+=1 
            tirer=1
    if tirer==1:
        pass
    else:
        pass
    
    root.after(50,tir)
tir()



root.mainloop()
