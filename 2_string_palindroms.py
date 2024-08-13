def palindrome(s):
    s = ''.join(s.split()).lower()
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True
string1 = "hello"
string2 = "madam"
result1 = palindrome(string1)
result2 = palindrome(string2)
print(f"Is '{string1}' a palindrome? {result1}")
print(f"Is '{string2}' a palindrome? {result2}")

