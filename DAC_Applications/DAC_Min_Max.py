def DAC_min_max(arr,i,j):
    if i==j:
        max= min = arr[i]
        return max,min
    elif i==(j-1):
        if arr[i]>arr[j]:
            max = arr[i]
            min = arr[j]
        else:
            max = arr[j]
            min = arr[i]

        return max,min
    else:
        k = (i+j)//2
        max1,min1 = DAC_min_max(arr,i,k)
        max2,min2 = DAC_min_max(arr,k+1,j)
        if max1>max2:
            max = max1
        else:
            max= max2
        if min1>min2:
            min = min2
        else:
            min = min1
        return max,min

    
arr = list(map(int,input().split()))
i = 0
j = len(arr)-1
max,min = DAC_min_max(arr,i,j)
print(f"Maximum {max}\nMinimum {min}")
