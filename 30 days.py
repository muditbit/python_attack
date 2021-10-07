b = bin(int(input()))
b = str(b)

li = list(b)
li = li[2:]
print(li)
count =0
new =0
whole = []
new =[]
for i in range(len(li)):
   if li[i]=='1':
       a = int(li[i])
       whole.append(a)
   else:
       a=0
       count = len(whole)
       break
print(count)
