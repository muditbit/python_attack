def poly(n,arr):
    #arr =[]
    i=0
    j=0
    while j<n:
        if i%3==0 or i%10==3:
            #arr.append(i)
            i += 1
            #j += 1
        else:
            arr.append(i)
            i +=1
            j += 1
    return arr[-1]
            
test_case = int(input())
arr = []
for _ in range(test_case):
    n = int(input())
    if len(arr)<n:
        res = poly(n,arr)
        print(res)

    else:
        print(arr[n-1])
