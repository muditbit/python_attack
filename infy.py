# Print the frequency of each element
def countFrequency(string):
  # Write your code here
  l = list(string)
  s = list(set(l))
  for i in range(len(s)):
    print(s[i]+str(l.count(s[i])),end = " ")

if __name__=="__main__":
  string = input().strip();
  countFrequency(string);
