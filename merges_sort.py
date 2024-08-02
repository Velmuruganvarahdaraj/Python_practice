def mergesort(a):
    if len(a) > 1:
        mid = len(a) // 2
        l = a[:mid]
        r = a[mid:]
        mergesort(l)
        mergesort(r)
        i = j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            a[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            a[k] = r[j]
            j += 1
            k += 1
a = []
n = int(input("Enter the number of elements: "))
for _ in range(n):
    a.append(int(input()))
mergesort(a)
print("Sorted array:", a)
