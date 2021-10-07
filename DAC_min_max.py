def DAC_Min_Max(arr,i,j):
    
    
    if i==j:
        mx = mn = arr[i]
        return mx,mn
    if i==(j-1):
        if arr[i]<arr[j]:
            mx = arr[j]
            mn = arr[i]
        else:
            mx =arr[i]
            mn = arr[j]
        return mx,mn
    else:
        mid = (i+j)//2
        mx1,mn1 = DAC_Min_Max(arr,i,mid)
        mx2,mn2 = DAC_Min_Max(arr,mid+1,j)
        if mx1<mx2:
            mx = mx2
        else:
            mx = mx1

        if mn1<mn2:
            mn = mn1
        else:
            mn = mn2
        return mx,mn

arr = list(map(int,input().split()))
i = 0
j = len(arr)-1
mn,mx = DAC_Min_Max(arr,i,j)
print(mn,mx)
        
