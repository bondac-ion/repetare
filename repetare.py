x=[]
n=0
while n<5:
    i=int(input("Dati un numar:"))
    x.extend([i])
    n+=1

y=x
suma_3componen=x[0]+x[1]+x[2]
print("Suma primelor 3 componente este =",suma_3componen)
print("Suma tuturor componentelor este =",sum(y))
produsul=1
for i in range(0,len(x)):
    produsul=produsul*x[i]

print("Produsul este =",produsul)
print("Valoarea absoluta a componentei 3 este =",abs(y[2]))
print("Suma primelor componente a listelor este =",x[0]+y[0])
