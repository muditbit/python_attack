n = int(input())
l = list(map(int, input().split()))
print(len(l))

s=set(l)

s= list(s)
print(len(s))
for i in range(len(s)):
    c= 0
    for j in range(len(l)):
        if s[i]==l[j]:
            c = c+1
        else:
            c=c

    if c==1:
        room = l[i]
        break

print(room)
