t=[]
n=0
while n<24:
    i=int(input("Dati o temperatura:"))
    t.extend([i])
    n+=1

s=t.copy()
print("Temperatura medie este",round(sum(t)/24,2))
print("Maximul temperaturii este",max(t),",iar minimumul este",min(t))
x=t.count(max(t))
v=[]
y=x
for i in range(0,len(t)):
    if x==1:
        v.extend([t.index(max(t))])
    else:
        if y!=0:
            v.extend([t.index(max(t))])
            t[t.index(max(t))]=0
            y=y-1
        else:
            break

maxime=""
for i in range(0,len(v)):
    maxime=maxime+" "+"ora"+" "+str(v[i]+1)

if x>1:
    print("Orele cu temperatura maxima sunt",maxime)
else:
    print("Ora cu temperatura maxima este",maxime)

x=s.count(min(s))
w=[]
y=x
for i in range(0,len(s)):
    if x==1:
        w.extend([s.index(min(s))])
    else:
        if y!=0:
            w.extend([s.index(min(s))])
            s[s.index(min(s))]=max(s)
            y=y-1
        else:
            break

minime=""
for i in range(0,len(w)):
    minime=minime+" "+"ora"+" "+str(w[i]+1)

if x>1:
    print("Orele cu temperatura minima sunt",minime)
else:
    print("Ora cu temperatura minima este",minime)
