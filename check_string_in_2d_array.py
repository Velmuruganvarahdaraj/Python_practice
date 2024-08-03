def find_string_in_2d_array(array, target):
    for row in array:
        if target in row:
            return True
    return False
array = [
    ['vel', 'naveen', 'siva'],
    ['aswin', 'monish', 'nihal'],
    ['nafees', 'hari', 'thejesh']
]
target_string = 'vel'
if find_string_in_2d_array(array, target_string):
    print(f"'{target_string}' was found ")
else:
    print(f"'{target_string}' was not found")
