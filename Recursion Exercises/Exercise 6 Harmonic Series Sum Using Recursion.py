def h_series_sum(n):
    if n < 1:
        return 0
    else: 
        return 1/n + h_series_sum(n-1)
    
print(h_series_sum(4))