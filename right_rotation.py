a=int(input())
s=[]
for i in range(a):
    c=[]
    for j in range(a):
        c.append(int(input()))
    s.append(c)
for i in range(a-1,-1,-1):
    for j in range(a):
        print(s[j][i],end=' ')
    print()