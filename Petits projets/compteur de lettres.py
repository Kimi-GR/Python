
def numbuers(mot):
    nbr_voyelle=0
    for letter in mot:
        if letter in ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']:
            nbr_voyelle=nbr_voyelle+1
    return nbr_voyelle
    
    
        



mot=input("entrer un mot :") 
a=numbuers(mot)
print("dans ",mot," il y a ",a," lettre(s)")
