''' This is an application of Divide and Conquer Here also time complexity is O(logn) 
but worst case would be when the desired element is either not in the array or at begining or end of the array
Only problem with binary search is it need a sorted array to perform its operation'''

def DAC_Binary_search(arr,i,j,item):
    if i==j:
        if arr[i]==item:
            return i
        else:
            return -1
    else:
        mid = (i+j)//2
        if arr[mid]==item:
            return mid
        elif item < arr[mid]:
            return DAC_Binary_search(arr,i,mid-1,item)
        else:
           return DAC_Binary_search(arr,mid+1,j,item)

arr = list(map(int,input().split()))
i =0
j = len(arr)-1
print("Array Stored\n")
arr.sort()
print("Array Sorted\n",arr)

item = int(input("Entered desired element:\n"))
res = DAC_Binary_search(arr,i,j,item)


if res!=-1:
    print("After sorting Element found at index:",res,"and Position:",res+1)
else:
    print("Oh Snap Element not in the array")
