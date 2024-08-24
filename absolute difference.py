def findtotalsum(arr,pos):
  c1 = 0
  c2 = 0
  for i in range(len(arr)):
    if i == pos:
      c1 += arr[i] - arr[i+1]
      c2 += arr[i] - arr[i-1]
  return c1 + c2
arr = [11,22,12,24,13,26,14]
pos = 5
print(findtotalsum(arr,pos))