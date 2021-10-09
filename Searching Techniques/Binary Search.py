''' This is iterative binary search method 
Time Complexity = O(logn)
There is one constraint that is it uses sorted array thus time complexity also depends on 
Sorting algorithm we use

'''



def binary_search(arr, x):
    
	low = 0
	high = len(arr) - 1
	mid = 0
    
	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1


# Test array
arr = list(map(int,input().split()))
arr.sort()

print("Array Stored\n")
print("Array sorted")
x = int(input())

# Function call
result = binary_search(arr, x)
print("After Sorting :",arr)


if result != -1:
	print("Here we got it at index", str(result))
else:
	print("Sorry but there is no match ")
