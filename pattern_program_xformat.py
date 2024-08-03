def x_pattern(s):
    n = len(s)
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print(s[j], end="")
            else:
                print(" ", end="")
        print()

x_pattern("Program")
