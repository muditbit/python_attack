'''This application of Divide and Conquer where we can find the value of a^n in
O(logn) time thus this will take less tie than traditional method'''

def DAC_power_of_a(a,n):
    if n==0:
        return 1
    if n==1:
        return a
    else:
        if n%2==0:
            mid = n//2
            b = DAC_power_of_a(a,mid)
            return b*b
        else:
            mid = n//2
            b = DAC_power_of_a(a,mid)
            return a*b*b
            
    
a = int(input("Enter the base value:\n"))
n =  int(input("Enter the power:\n"))
print(DAC_power_of_a(a,n))