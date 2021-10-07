def distribute(n,l,p):
  # Complete the function
  count = n
  while count!=0:
    if p<l:
      count -=1
      p += 1
    else:
      p = 0
      count -= 1
      p +=1
     
  return p-1


if __name__ == "__main__":
  n = int(input().strip());
  l = int(input().strip());
  p = int(input().strip());
  print(distribute(n,l,p));
