matrix =[]
for i in range(int(input())):
    
            
        name = input()
        score = float(input())
        matrix.append([name,score])

matrix.sort()
print(matrix)

