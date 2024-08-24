def perfect_cube(num):
    if num < 0:
        return False
    for i in range(1, num + 1):
        if i * i * i  == num:
            return True
        elif i * i  * i > num:
            return False
    return False
numbers = [1, 2, 3, 4, 5, 16, 18, 25, 30, 36] 
perfect_cube = [num for num in numbers if perfect_cube(num)]
print("Perfect cube in the list:", perfect_cube)
