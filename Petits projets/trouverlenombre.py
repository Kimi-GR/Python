from random import randint


a=randint (0,80)

b=int(input("entrer un nombre : "))

if a==b:
    print("bravo")
elif b>a-11 and b<a+11:
    print("bravo")
    print(a)
else:
    print("perdu")
    print(a)