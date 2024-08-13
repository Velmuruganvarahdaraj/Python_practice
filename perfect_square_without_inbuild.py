def perfect_square(num):
    if num < 0:
        return False
    for i in range(1, num + 1):
        if i * i == num:
            return True
        elif i * i > num:
            return False
    return False
numbers = [1, 2, 3, 4, 5, 16, 18, 25, 30, 36]
perfect_squares = [num for num in numbers if perfect_square(num)]
print("Perfect squares in the list:", perfect_squares)
