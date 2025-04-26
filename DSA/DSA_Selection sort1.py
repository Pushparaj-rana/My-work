def selection_sort(arr):
    size =  len(arr)
    for i in range(size - 1):
        min_value_index = i
        for j in range(min_value_index + 1,size):
            if arr[j] < arr[min_value_index]:
                min_value_index = j
        if i!= min_value_index:        
            arr[i], arr[min_value_index] = arr[min_value_index], arr[i]


if __name__ == '__main__':
    print("Main block is running!")
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]


    for elements in tests:
        selection_sort(elements)
        print(f"Sorted list: {elements}")