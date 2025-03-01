from math import *
print("entrez une fonction de la forme f(x)=ax²+bx+c :")

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
discriminant=((b**2)-(4*a*c))
print("discriminant = ",discriminant)
if discriminant>0:
    x1=((-1*b)-sqrt(discriminant))/(2*a)
    x2=((-1*b)+sqrt(discriminant))/(2*a)
    print("les solutions sont x1=",x1," et x2=",x2  )
    print("la forme factorisée est :",a,"(x-","(",x1,")",")","(x-","(",x2,")",")")
    
if discriminant<0:
    x1=(((-1)*b)-(1j*(sqrt((-1)*discriminant))))/(2*a)
    
    x2=((-1*b)+1j*(sqrt(-1*discriminant)))/(2*a)
    print("les solutions sont x1=",x1," et x2=",x2  )
    print("la forme factorisée est :",a,"(x-","(",x1,")",")","(x-","(",x2,")",")")
if discriminant==0:
    x0=-b/(2*a)
    print("la solutions est x0=",x0 )
    print("la forme factorisée est :(x-","(",x0,")",")²")

