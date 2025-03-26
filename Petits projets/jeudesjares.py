from random import*
score=0
p=0
print("bonjour et bienvenue au jeu des jares ")
n=input("choisissez un niveau (1:facile  2:moyen  3:difficile): ")
while p==0:
    

    if n=="3":
        li=[1,0,1,0,1]
        shuffle(li)
        a=li[0]
        b=li[1]
        c=li[2]
        d=li[3]
        e=li[4]
        
    
        print("il y a trois jares infectées ")
        r=input("choisissez entre les jarres a,b,c,d ou e (ecrivez uniquement la lettre) : ")
        
    
        if r=="a":
            if a==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")

        if r=="b":
            if b==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
                
        if r=="c":
            if c==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="d":
            if d==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="e":
            if e==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="":
            print("perdu")
            p+=1
            print("votre score est de ",str(score))
 



    if n=="1":
        li=[1,0,0,0,0]
        shuffle(li)
        a=li[0]
        b=li[1]
        c=li[2]
        d=li[3]
        e=li[4]
        
    
        print("il y a une jare infectée ")
        r=input("choisissez entre les jarres a,b,c,d ou e (ecrivez uniquement la lettre) :")
        
    
        if r=="a":
            if a==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")

        if r=="b":
            if b==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="c":
            if c==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="d":
            if d==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="e":
            if e==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="":
            print("perdu")
            p+=1
            print("votre score est de ",str(score))

    if n=="2":
        li=[1,0,0,1,0]
        shuffle(li)
        a=li[0]
        b=li[1]
        c=li[2]
        d=li[3]
        e=li[4]
        
        
    
        print("il y a deux jares infectées ")
        r=input("choisissez entre les jarres a,b,c,d ou e (ecrivez uniquement la lettre): ")
        
    
        if r=="a":
            if a==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")

        if r=="b":
            if b==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="c":
            if c==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="d":
            if d==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="e":
            if e==1:
                print("perdu")
                p+=1
                print("votre score est de ",str(score))
            else:
                print("gagner")
                score+=1
                print(str(score)," pts")
        if r=="":
            print("perdu")
            p+=1
            print("votre score est de ",str(score))
if score>=10:
    print("tu es très fort a ce jeu !!!")
if score==0:
    print("nullll")
elif score>0 and score<6:
    print("pas mal")
elif score>=6 and score<=9:
    print("biennnn !!")    