def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l =[]
    for i in range(len(lst)):
        m = lst[i]

        remLst = lst[:i] + lst[i+1:]

        for p in permutation(remLst):
            l.append([m]+p)

    return l
data = [1,1,2]
data = list(data)
a =[]
for p in permutation(data):
    
    a.append(p)

print(a)
for i in range(len(a)):
    if sum(a[i])<=3:
        print(a[i])

   
