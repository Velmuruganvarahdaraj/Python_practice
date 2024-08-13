def newman_conway(n):
    if n < 1:
        return 0
    p = [0] * (n + 1)
    p[0] = 1      
    for i in range(1, n + 1):
        p[i] = p[i - 1]
        if i >= 2:
            p[i] += p[i - 2]
        if i >= 5:
            p[i] += p[i - 5]
        if i >= 7:
            p[i] += p[i - 7]   
    return p[n]
n = 10
print(f"Number of partitions for {n} is: {newman_conway(n)}")
