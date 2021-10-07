# Python3 program for the above approach

# Function to find the minimum
# value of XOR of AND and OR of
# any pair in the given array


def maxAndXor(arr, n):

	ans = float('inf')

	# Sort the array
	arr.sort()

	# Traverse the array arr[]
	for i in range(n - 1):

		# Compare and Find the minimum
		# XOR value of an array.
		ans = min(ans, arr[i] ^ arr[i + 1])

	# Return the final answer
	return ans


# Driver Code
if __name__ == '__main__':

	# Given array
	arr = [528,783,525,711,551,220,265,766,430,99]
	N = len(arr)

	# Function Call
	print(maxAndXor(arr, N))

# This code is contributed by Shivam Singh
