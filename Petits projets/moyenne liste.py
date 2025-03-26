n=int(input("combien de valeurs?: "))
s=0
for i in range(1,n+1):
    note=float(input("entrer vos valeurs : "))
    s=s+note
print(s/n)

