
# implementation of quick sort in python using hoare partition scheme

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
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+= 1

        while end>=0 and elements[end] > pivot:
            end -= 1
        if start < end:
            swap (start,end,elements)
    swap(end,pivot_index,elements)

    return end



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