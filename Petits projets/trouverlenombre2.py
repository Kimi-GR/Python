from random import randint


a=randint(0,100)

chance=0
u=-1

while u!=a and chance<8:
    u=int(input("entrer un nombre : "))
    chance=chance+1
    if u<a:
        print("trop petit")
        print(str(chance)," chances utilisee(s) sur 8")
        
    if u>a:
        print("trop grand")
        print(str(chance)," chances utilisee(s) sur 8")
        

if u==a:
    print("bravo tu as trouver")
else:
    print("perdu")
    print("la bonne réponse était ",str(a))
