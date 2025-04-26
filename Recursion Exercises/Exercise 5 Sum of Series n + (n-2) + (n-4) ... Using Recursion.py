def sum_of_series(n):
    #sum = 0
    if n > 0:
        m = n-2
        return n + sum_of_series(m)
    else:
        return 0
    #return sum
print(sum_of_series(5))