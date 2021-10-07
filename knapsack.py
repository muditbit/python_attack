
def knapSack(W, wt, val, n): 

	
	if n == 0 or W == 0 : 
		return 0

	
	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1) 

	 
	else: 
		return max( 
			val[n-1] + knapSack( 
				W-wt[n-1], wt, val, n-1), 
				knapSack(W, wt, val, n-1)) 

 


n = int(input("Enter the no. of Element:"))
val=[]
wt=[]
for i in range(n):
    item = int(input("Enter Profit No.:"))
    weight = int(input("Enter Weight of Item:"))
    val.append(item)
    wt.append(weight)
 
W = int(input("Enter weight uphold by bag:"))
 
print("max profit would be",knapSack(W, wt, val, n)) 


