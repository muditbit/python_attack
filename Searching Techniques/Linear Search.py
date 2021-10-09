''' This is basic method of Linear Search

Time Complexity = O(n) Worst Case
                  O(1) Best Case
                  O(n/2) Average Case
                  '''

def linearSearch(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

arr = list(map(int,input().split()))
print('Array Stored')

item =  int(input())
res = linearSearch(arr,item)
if res == -1:
    print("Oh snap Item Not found in array")
else:
    print(f"Ohh here it is at position {res+1}")