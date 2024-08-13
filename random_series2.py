def generate_series(n):
    series = []
    for i in range(1, n + 1):
        term = i * (i**2 + 1)
        series.append(term)
    return series
result_series = generate_series(6)
print(result_series)
