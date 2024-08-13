def print_subarrays(arr):
    n = len(arr)
    for start in range(n):
        for end in range(start + 1, n + 1):
            print(arr[start:end])
array = [1, 2, 3]
print_subarrays(array)
