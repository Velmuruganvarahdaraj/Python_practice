def sum_of_square(n):
    num = 0
    while n > 0:
        d = n % 10
        num += d * d
        n //= 10
    return num

def happy_num(n):
    s = set()
    while n != 1 and n not in s:
        s.add(n)
        n = sum_of_square(n)
    return n == 1

number = int(input("Enter a number: "))
if happy_num(number):
    print(f"{number} is a Happy Number!")
else:
    print(f"{number} is not a Happy Number.")
