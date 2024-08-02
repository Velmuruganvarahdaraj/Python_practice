def friends_pairing(n):
    if n <= 2:
        return n
    a = [0] * (n + 1)
    a[1] = 1
    a[2] = 2
    for i in range(3, n + 1):
        a[i] = a[i - 1] + (i - 1) * a[i - 2]
    return a[n]
n = int(input())
print(f"Number of ways to pair {n} friends: {friends_pairing(n)}")
