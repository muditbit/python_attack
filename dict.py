# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
key = []
value = []
for i in range(n):
    
    string = input()
    l = string.split()
    key.append(l[0])
    value.append(int(l[1]))
    

class my_dictionary(dict): 

    # __init__ function 
    def __init__(self): 
        self = dict() 
        
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

# Main Function 
dict_obj = my_dictionary() 


for i in range(n):
    dict_obj.add(key[i],value[i])

search =[]
for i in range(n):
    inp = input()
    search.append(inp)


for i in range(n):
    key = search[i]
    if key in dict_obj:
        print(str(key) + '=' + str(dict_obj[key]))
    else:
        print('Not Found')
#print(dict_obj)
