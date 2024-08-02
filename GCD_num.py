n1=int(input())
n2=int(input())
n1,n2=n2,n1
while n2!=0:
    n1,n2=n2,n1%n2
print(n1)