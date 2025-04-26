def quick_sort(elements,start,end):
    if start<end:
        pi = partition(elements,start,end)
        quick_sort(elements,start,pi-1)
        quick_sort(elements,pi+1,end)

def swap(a,b,arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements,start,end):
    pivot_index = end
    pivot = elements[end]
    i = start - 1
    for j in range(start,end):
        if elements[j] <= pivot:
            i += 1
            swap(i,j,elements)
    swap(pivot_index,i + 1,elements)
    return i + 1


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]

    quick_sort(elements,0,len(elements)-1)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')