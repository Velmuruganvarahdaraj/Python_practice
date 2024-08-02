def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
input_string = input(" ")
if is_palindrome(input_string):
    print("is a palindrome.")
else:
    print("is not a palindrome.")
