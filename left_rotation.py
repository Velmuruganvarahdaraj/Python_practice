"""def left_rotate(lst, k):
    k = k % len(lst) 
    return lst[k:] + lst[:k]
lst = [1, 2, 3, 4, 5]
k = 2  
left_rotated_list = left_rotate(lst, k)
print("Left rotated list:", left_rotated_list)
"""
def left(a,n):
    temp=a[0]
    for i in range(0,n-1):
        a[i]=a[i+1]
    a[n-1]=temp
def rot(a,n,k):
    for i in range(k):
        left(a,n)
a=list(map(int,input().split()))
n=len(a)
k=int(input())
rot(a,n,k)
print(a)
