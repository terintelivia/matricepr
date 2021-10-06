m=[[15,26,32,78,41],
  [17,29,38,14,10],
  [9,13,34,25,85],
  [2,54,25,65,11],
  [19,33,21,17,45]]

suma=[]
for i in range(len(m)):
    suma.append(sum(m[i]))
print("Suma elementelor de pe fiecare linie este=",suma)

s=[]
coloana=[]
for j in range(len(m[0])):
    for rind in m:
        coloana.append(rind[j])
    s.append(sum(coloana))
print("Suma elementelor de pe fiecare coloana este=",s)

dprincipala=[]
for i in range(len(m)):
    for j in range(len(m[0])) :
        if i==j :
            dprincipala.append(m[i][j])
print("Diagonala principala este:",dprincipala)

dsecundara=[] 
for i in range(len(m)):
    for j in range(len(m[0])) :
        n=5
        if i+j==n-1:
            dsecundara.append(m[i][j])
print("Diagonala secundara este:",dsecundara) 