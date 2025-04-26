def shell_sort(arr):
    size = len(arr)
    gap = size//2
   
    while gap>0:
        for i in range(gap,size):
            anchor = arr[i]    
            j = i
            
            while j>=gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap//2
    return arr
    
def new_arr(arr):
    arr = shell_sort(arr)
    new_arr = []
    size = len(arr)
    i = j = 0
    while j < size:
        j = i+1
        while j < size and arr[i] != arr[j]:
            new_arr.append(arr[i])
            j += 1
            i += 1
        
        while j < size and arr[i] == arr[j]:
             j+=1
        new_arr.append(arr[i])
        i = j
    arr.clear()  # Clears the all original list
    arr.extend(new_arr)  # Adds elements from 'new_arr' to the original list

  
   


if __name__ == '__main__':
    tests = [[2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3],
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]
    #elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
    #sort_arr = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3, 9, 9, 11, 11, 1, 0, 44]
    for elements in tests:
        shell_sort(elements)
        print(elements)

    print("\n")
    #shell_sort(sort_arr)
    #print(sort_arr)

    #print(new_arr(sort_arr))
    for elements in tests:
        new_arr(elements)
        print(elements)
    