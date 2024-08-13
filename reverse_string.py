def reverse_string(s):#reverse_string_preserve_whitespace
    n = [c for c in s if not c.isspace()]
    n.reverse()
    index = 0
    result = list(s)
    for i in range(len(result)):
        if not result[i].isspace():
            result[i] = n[index]
            index += 1
    return ''.join(result)
input_string = "hello world"
reversed_string = reverse_string(input_string)
print(f"Original string: '{input_string}'")
print(f"Reversed string: '{reversed_string}'")
