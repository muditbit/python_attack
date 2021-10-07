n = int(input())
marks ={}
for i in range(n):
    name, *line =input().split()
    scores =list(map(float, line))
    marks[name] = scores
query_name = input()
query_marks = marks[query_name]
d=float(sum(query_marks))
average = d/len(query_marks)
print("{:.2f}".format(average))
print(name[0])
