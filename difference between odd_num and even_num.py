def diff_odd_evennum(size,arr):
    odd=0
    even=0
    for num in arr:
        if num%2 == 0:
            even+=1
        else:
            odd =odd+ 1
        return odd - even
size=5
numbers=[1,2,3,5,6] 
result = diff_odd_evennum(size, numbers)
print(result)


