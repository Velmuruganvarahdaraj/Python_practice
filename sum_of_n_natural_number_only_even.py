def sum_evenum(n):
    t = n * (n + 1) // 2
    print(f"Sum of the first {n} natural numbers: {t}")
    print("Even numbers from 1 to", n, ":")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
n =int(input())
sum_evenum(n)
