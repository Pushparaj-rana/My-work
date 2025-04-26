def sum_of_list(arr,n):
    if n <= len(arr)-1:
        if n == 0:
            return arr[n]
        return arr[n] + sum_of_list(arr, n-1)
    else:
        return "invalid n value"

if  __name__ == '__main__':
    arr = [2,3,11,4,5,6,8,4,12]
    print(sum_of_list(arr,8))

