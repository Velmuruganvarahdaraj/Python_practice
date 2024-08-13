def taylor_series(x,n):
    term =1.0
    result =1.0
    for i in range (1,n):
        term = term * x / i
        result += term
    return  result
x_val=int(input())
n_term=(int(input()))
t_series=taylor_series(x_val,n_term)
print(f"Taylor series approximation of e^{x_val} with {n_term} terms: {t_series}")