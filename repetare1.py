zi=["Luni","Marti","Miercuri","Joi","Vineri","Sambata","Duminica"]
n=0
venit=[]
while n<7:
    i=int(input("Dati o suma:"))
    venit.extend([i])
    n+=1

print("Venitul saptamanal al intreprinderii este =",sum(venit))
print("In medie pe zi revin",round(sum(venit)/7,2))
i=venit.index(max(venit))
print("Ziua cu venitul maxim este",zi[i])
i=venit.index(min(venit))
print("Ziua cu cel mai mic venit este",zi[i])