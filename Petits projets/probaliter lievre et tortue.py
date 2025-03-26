from random import randint


lievre=0
gagner=0
tortue=0
t=0

for i in range (1000):
    l=randint(1,6)
    print(l)
    if l==6:
        print("le lievre gagne")
        lievre=lievre+1
    
        gagner=1
    else:
        t=0
        t=t+1
        print("la tortue avance de "+(str(t))+" case(s)")
        if t==6:
            print("la tortue gagne") 
        gagner=1 
        tortue=tortue+1
print(tortue/1000)        
print(lievre/1000)

