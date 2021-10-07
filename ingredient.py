def find_max(arr):
    incl = 0
    excl = 0
    for i in arr:
        new_excl = excl if excl>incl else incl
        incl = excl + i
        excl = new_excl
    return(excl if excl>incl else incl)

arr = list(map(int,input().split()))
print(find_max(arr))
