n = 2
S = 'Hacker'
E =[]
O = []
H = list(S)
for i in range(len(H)):
    if i%2==0:
        E.append(H[i])
    else:
         O.append(H[i])
Estr = ''.join(E)
Ostr = ''.join(O)
print(Estr,end=' ')
print(Ostr)

