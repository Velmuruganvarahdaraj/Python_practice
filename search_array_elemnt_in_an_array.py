def search(a,b):
    for i in range(len(a)):
        if a[i] ==b:
            return " is found "
    return f"not found"
arr = [10, 20, 30, 40, 50]
search_element= 30
result = search(arr,search_element)
print(result)
