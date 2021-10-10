'''
Question:
Input:- A sorted array of n-dsitinct element
Output:- Find any element a[i] where a[i]==i


This can be solved in 2 ways one is linear search and another is binary search with worst cases O(n) and O(logn) respectively'''

def linear_method(arr,i,j):
    count=0
    while count<len(arr):
        if arr[count]==count:
            return count
            break
            
        else:
            count += 1
    return "Not Found"
        
def binary_method(arr,i,j):
    if i==j:
        if arr[i]==i:
            return i
        else:
            return "Not Found"
    else:
        mid = (i+j)//2
        if arr[mid]==mid:
            return mid
        elif arr[mid]>mid:
            return binary_method(arr,i,mid-1)
        else:
            return binary_method(arr,mid+1,j)

arr = list(map(int,input("Enter array in sorted way (increasing):\n").split()))

i = 0
j=len(arr)-1

print('Using Linear Search Method we get the answer in O(n) time complexity as:',linear_method(arr,i,j))
print('Using Binary Search Method we get the answer in O(logn) time complexity as:',binary_method(arr,i,j))