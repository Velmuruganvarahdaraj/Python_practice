def count_repeated_characters(comp_string):
    if not comp_string:
        return 0
    char_frequency = {}
    for char in comp_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    count = 0
    for char, frequency in char_frequency.items():
        if frequency == 1:
            count += 1
    return count
comp_string = "alphaadida"
result = count_repeated_characters(comp_string)
print(result)
