def find_difference(lst):
    even_sum = 0
    odd_sum = 0
    for i in range(len(lst)):
        if i % 2 == 0:  
            even_sum += lst[i]
        else:  
            odd_sum += lst[i]
    return odd_sum - even_sum
numbers = [10, 1, 4, 2, 7, 3]
difference = find_difference(numbers)
print("Difference between odd and even index elements:", difference)
