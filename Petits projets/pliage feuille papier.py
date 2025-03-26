p=float(input("entrer une taille de papier: "))
h=float(input("entrer une hauteur: "))
n=0
while p<=h:
    n+=1
    p=p*2
    print(p,n)
print("pour atteindre ",str(p)," mm il faut plier le papier ",str(n)," fois")