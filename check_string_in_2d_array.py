def find_string_in_2d_array(array, target):
    rows = len(array)
    cols = len(array[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if array[i][j] == target:
                return True

    return False
array = [
    ["apple", "banana" ],
    ["date", "elderberry" ],
    ["grape", "honeydew" ]
]
target_string = input()
is_found = find_string_in_2d_array(array, target_string)
print(is_found)  

