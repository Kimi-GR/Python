def get_voyelles_numbuers(mot):
    nbr_voyelle=0
    for letter in mot:
        if letter in ['a','e','i','o','u','y']:
            nbr_voyelle=nbr_voyelle+1
    return nbr_voyelle
    
    
        



mot=input("entrer un mot :") 
a=get_voyelles_numbuers(mot)
print("dans ",mot," il y a ",a," voyelle(s)")