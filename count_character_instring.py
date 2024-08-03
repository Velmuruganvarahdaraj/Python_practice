def count_characters(s):
    count = 0
    for char in s:
        count += 1
    return count
input_string = "I'm a CSE Student"
character_count = count_characters(input_string)
print(f"The number of characters in the string is: {character_count}")
