'''Question:
Input:- A sorted array of n-element and an item t(say)
Output:- Find any 2 element such that (a+b)==t
'''

'''This problem can be solved using Linear Search method in Time Complexity of O(n^2)
Using Binary Search O(logn)
Using Greedy approach we can solve it using O(n)

Here we are going to perform Greedy approach
'''

def greedy_approach(arr,i,j,t):
    while i!=j:
        if (arr[i]+arr[j])==t:
            return arr[i],arr[j]

        else:
            if (arr[i]+arr[j])>t:
                j -= 1
            else:
                i += 1

arr = list(map(int,input("Enter the sorted array:\n").split()))
t = int(input('Specify the condition:\n'))

i = 0
j = len(arr)-1
print("The elements are:\n",greedy_approach(arr,i,j,t))
