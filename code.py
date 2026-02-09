def fun(s):
  if s.strip("0") == "" or s.strip("1") == "":
    return s
 
  ans = ""
  n = len(s)
 
  for i in range(0, n):
    if s[0] == "0":
        ans = ans + "01"
    else:
        ans = ans + "10"
    
  
  return ans
 
tc = int(input())
 
while tc > 0:
   s = str(input())
   print(fun(s))
   tc = tc - 1