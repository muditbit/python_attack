n = int(input())
a=[]
for i in range(n):
    item = input()
    a.append(item)
a = list(a)
#print(a)
a.sort(reverse=True)
#print(a)
b = list(a[:4])
#print(b)
result = 1
for i in range(4):
    result = result* int(b[i])
print(result)
