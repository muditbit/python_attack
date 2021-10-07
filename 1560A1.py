arr = []
i = 0
while len(arr)<=1000:
    for i in range(0,2000):
        if i%3!=0 and i%10!=3:
            arr.append(i)
        
print(arr)
