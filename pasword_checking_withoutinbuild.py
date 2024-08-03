def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in password:
        ascii_value = ord(char)
        if 65 <= ascii_value <= 90: 
            has_upper = True
        elif 97 <= ascii_value <= 122: 
            has_lower = True
        elif 48 <= ascii_value <= 57:  
            has_digit = True
        elif 33 <= ascii_value <= 47 or 58 <= ascii_value <= 64 or \
             91 <= ascii_value <= 96 or 123 <= ascii_value <= 126: 
            has_special = True
    return has_upper and has_lower and has_digit and has_special
password = input()
print(is_valid_password(password))  